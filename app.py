import streamlit as st

# Symptom-disease mapping
symptom_disease_map = {
    'fever': ['Flu', 'COVID-19'],
    'cough': ['Cold', 'Flu', 'COVID-19'],
    'headache': ['Migraine', 'Tension Headache'],
    'sore throat': ['Strep Throat', 'Cold'],
    'fatigue': ['Anemia', 'Thyroid Issues'],
}

def suggest_diseases(symptoms):
    possible_diseases = set()
    for symptom in symptoms:
        if symptom in symptom_disease_map:
            possible_diseases.update(symptom_disease_map[symptom])
    return list(possible_diseases)

st.title("Medical AI Agent")
st.write("Enter your symptoms to get possible diseases.")

input_symptoms = st.multiselect(
    "Choose your symptoms:",
    options=symptom_disease_map.keys()
)

if input_symptoms:
    diseases = suggest_diseases(input_symptoms)
    if diseases:
        st.write("Possible diseases based on your symptoms:", ', '.join(diseases))
    else:
        st.write("No possible diseases found.")
