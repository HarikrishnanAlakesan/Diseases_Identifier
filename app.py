from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def predict_disease_and_therapist(input_sentence, dataset_path='dis.csv'):
    df = pd.read_csv(dataset_path)
    symptom = extract_symptom(input_sentence, df)
    match = df[df['Symptom'].str.lower() == symptom.lower()]

    if not match.empty:
        predicted_disease = match['Disease'].iloc[0]
        suggested_therapist = match['Therapist'].iloc[0]
        return predicted_disease, suggested_therapist
    else:
        return 'Unknown Disease', 'Unknown Therapist'

def extract_symptom(input_sentence, df):
    words = input_sentence.split()

    # Iterate through words and check if any matches a symptom in the dataset
    for i, word in enumerate(words):
        if i < len(words) - 1:
            # Combine current word and the next word with a white space
            combined_word = f"{word} {words[i + 1]}"
            match = df[df['Symptom'].str.lower() == combined_word.lower()]
            if not match.empty:
                return combined_word

        # Check the current word alone
        match = df[df['Symptom'].str.lower() == word.lower()]
        if not match.empty:
            return word

    # If no match found, return the last word (fallback)
    return words[-1]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input_sentence = request.form['user_input_sentence']
        result = predict_disease_and_therapist(user_input_sentence)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
