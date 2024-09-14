import streamlit as st

# Expanded Symptom-Disease mapping
symptom_disease_map = {
    'fever': ['Flu', 'COVID-19', 'Malaria', 'Typhoid'],
    'cough': ['Cold', 'Flu', 'COVID-19', 'Bronchitis', 'Whooping Cough'],
    'headache': ['Migraine', 'Tension Headache', 'Sinusitis', 'Cluster Headache'],
    'sore throat': ['Strep Throat', 'Cold', 'Tonsillitis', 'Laryngitis'],
    'fatigue': ['Anemia', 'Thyroid Issues', 'Chronic Fatigue Syndrome', 'Fibromyalgia'],
    'nausea': ['Gastritis', 'Food Poisoning', 'Pregnancy', 'Stomach Ulcer'],
    'dizziness': ['Vertigo', 'Low Blood Pressure', 'Dehydration', 'Inner Ear Infection'],
    'shortness of breath': ['Asthma', 'COPD', 'Heart Failure', 'Pulmonary Embolism'],
    'chest pain': ['Angina', 'Heart Attack', 'Pneumonia', 'Acid Reflux'],
    'abdominal pain': ['Appendicitis', 'Irritable Bowel Syndrome', 'Gallstones', 'Pancreatitis'],
    'muscle pain': ['Muscle Strain', 'Rheumatoid Arthritis', 'Lupus', 'Myositis'],
    'rash': ['Allergic Reaction', 'Eczema', 'Psoriasis', 'Chickenpox'],
    'runny nose': ['Cold', 'Sinusitis', 'Allergic Rhinitis', 'Flu'],
    'swollen lymph nodes': ['Mononucleosis', 'HIV', 'Lymphoma', 'Tonsillitis'],
}

def suggest_diseases(symptoms):
    possible_diseases = set()
    for symptom in symptoms:
        if symptom in symptom_disease_map:
            possible_diseases.update(symptom_disease_map[symptom])
    return list(possible_diseases)

st.title("🩺 Medical AI Agent")
st.write("Enter your symptoms to get possible diseases.")

input_symptoms = st.multiselect(
    "Choose your symptoms:",
    options=symptom_disease_map.keys(),
    format_func=lambda x: x.capitalize()  # Capitalize symptom names
)

if input_symptoms:
    diseases = suggest_diseases(input_symptoms)
    if diseases:
        st.markdown(
            f"<div style='background-color:#d1e7dd;padding:10px;border-radius:5px;color:#0f5132;'>Possible diseases based on your symptoms: <strong>{', '.join(diseases)}</strong></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background-color:#f8d7da;padding:10px;border-radius:5px;color:#721c24;'>No possible diseases found.</div>",
            unsafe_allow_html=True
        )
else:
    st.write("Please select some symptoms to get suggestions.")
