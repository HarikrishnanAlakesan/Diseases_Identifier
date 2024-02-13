import pandas as pd

# Create a list of dictionaries representing the dataset
data = [
    {'Symptom': 'Fever', 'Disease': 'Flu', 'Therapist': 'General Practitioner'},
    {'Symptom': 'Cough', 'Disease': 'Common Cold', 'Therapist': 'General Practitioner'},
    {'Symptom': 'Shortness of Breath', 'Disease': 'Asthma', 'Therapist': 'Pulmonologist'},
    {'Symptom': 'Headache', 'Disease': 'Migraine', 'Therapist': 'Neurologist'},
    {'Symptom': 'Fatigue', 'Disease': 'Chronic Fatigue Syndrome', 'Therapist': 'Rheumatologist'},
    {'Symptom': 'Chest Pain', 'Disease': 'Heart Attack', 'Therapist': 'Cardiologist'},
    {'Symptom': 'Nausea', 'Disease': 'Gastroenteritis', 'Therapist': 'Gastroenterologist'},
    {'Symptom': 'Joint Pain', 'Disease': 'Rheumatoid Arthritis', 'Therapist': 'Rheumatologist'},
    {'Symptom': 'Muscle Weakness', 'Disease': 'Muscular Dystrophy', 'Therapist': 'Physical Therapist'},
    {'Symptom': 'Difficulty Breathing', 'Disease': 'Chronic Obstructive Pulmonary Disease (COPD)', 'Therapist': 'Pulmonologist'},
    {'Symptom': 'Dizziness', 'Disease': 'Vertigo', 'Therapist': 'Ear, Nose, and Throat (ENT) Specialist'},
    {'Symptom': 'Sore Throat', 'Disease': 'Strep Throat', 'Therapist': 'General Practitioner'},
    {'Symptom': 'Back Pain', 'Disease': 'Herniated Disc', 'Therapist': 'Orthopedic Specialist'},
    {'Symptom': 'Abdominal Pain', 'Disease': 'Appendicitis', 'Therapist': 'General Surgeon'},
    {'Symptom': 'Frequent Urination', 'Disease': 'Urinary Tract Infection (UTI)', 'Therapist': 'Urologist'},
    {'Symptom': 'Constipation', 'Disease': 'Irritable Bowel Syndrome (IBS)', 'Therapist': 'Gastroenterologist'},
    {'Symptom': 'Blurred Vision', 'Disease': 'Diabetes', 'Therapist': 'Endocrinologist'},
    {'Symptom': 'Memory Loss', 'Disease': 'Alzheimer\'s Disease', 'Therapist': 'Neurologist'},
    {'Symptom': 'Skin Rash', 'Disease': 'Eczema', 'Therapist': 'Dermatologist'},
    {'Symptom': 'Chest Tightness', 'Disease': 'Anxiety', 'Therapist': 'Psychiatrist'},
    {'Symptom': 'Frequent Headaches', 'Disease': 'Tension Headaches', 'Therapist': 'Neurologist'},
    {'Symptom': 'Insomnia', 'Disease': 'Sleep Apnea', 'Therapist': 'Sleep Specialist'},
    {'Symptom': 'Rapid Heartbeat', 'Disease': 'Atrial Fibrillation', 'Therapist': 'Cardiologist'},
    {'Symptom': 'Bloating', 'Disease': 'Irritable Bowel Syndrome (IBS)', 'Therapist': 'Gastroenterologist'},
    {'Symptom': 'Frequent Nosebleeds', 'Disease': 'Nasal Polyps', 'Therapist': 'Ear, Nose, and Throat (ENT) Specialist'},
    {'Symptom': 'Unexplained Weight Loss', 'Disease': 'Hyperthyroidism', 'Therapist': 'Endocrinologist'},
    {'Symptom': 'Joint Swelling', 'Disease': 'Osteoarthritis', 'Therapist': 'Rheumatologist'},
    {'Symptom': 'Hair Loss', 'Disease': 'Alopecia', 'Therapist': 'Dermatologist'},
    {'Symptom': 'Frequent Infections', 'Disease': 'Immunodeficiency Disorders', 'Therapist': 'Immunologist'},
    {'Symptom': 'Numbness or Tingling', 'Disease': 'Peripheral Neuropathy', 'Therapist': 'Neurologist'},
    {'Symptom': 'Throat Clearing', 'Disease': 'Laryngopharyngeal Reflux (LPR)', 'Therapist': 'Gastroenterologist'},
    {'Symptom': 'Chest Discomfort', 'Disease': 'Angina', 'Therapist': 'Cardiologist'},
    {'Symptom': 'Sensitivity to Light', 'Disease': 'Migraine', 'Therapist': 'Neurologist'},
    {'Symptom': 'Painful Periods', 'Disease': 'Endometriosis', 'Therapist': 'Gynecologist'},
    {'Symptom': 'Loss of Appetite', 'Disease': 'Depression', 'Therapist': 'Psychiatrist'},
    {'Symptom': 'Difficulty Swallowing', 'Disease': 'Esophageal Stricture', 'Therapist': 'Gastroenterologist'},
    {'Symptom': 'Tremors', 'Disease': 'Parkinson\'s Disease', 'Therapist': 'Neurologist'},
    {'Symptom': 'Yellowing of Skin', 'Disease': 'Jaundice', 'Therapist': 'Hepatologist'},
    {'Symptom': 'Frequent Thirst', 'Disease': 'Diabetes', 'Therapist': 'Endocrinologist'},
    {'Symptom': 'Calf Pain with Walking', 'Disease': 'Peripheral Artery Disease (PAD)', 'Therapist': 'Vascular Specialist'},
    {'Symptom': 'Difficulty Concentrating', 'Disease': 'Attention Deficit Hyperactivity Disorder (ADHD)', 'Therapist': 'Psychiatrist'},
    {'Symptom': 'Cold Hands and Feet', 'Disease': 'Raynaud\'s Disease', 'Therapist': 'Rheumatologist'},
]

# Convert the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(data)

# Save the extended dataset to an Excel file
#df.to_excel('symptoms_diseases_therapists_dataset.xlsx', index=False)
df.to_csv('symptoms_diseases_therapists_dataset.csv', index=False)

