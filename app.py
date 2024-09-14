import streamlit as st

# Expanded Symptom-Disease mapping
symptom_disease_map = {
    'fever': ['Flu', 'COVID-19', 'Malaria'],
    'cough': ['Cold', 'Flu', 'COVID-19', 'Bronchitis'],
    'headache': ['Migraine', 'Tension Headache', 'Sinusitis'],
    'sore throat': ['Strep Throat', 'Cold', 'Tonsillitis'],
    'fatigue': ['Anemia', 'Thyroid Issues', 'Chronic Fatigue Syndrome'],
    'nausea': ['Gastritis', 'Food Poisoning', 'Pregnancy'],
    'dizziness': ['Vertigo', 'Low Blood Pressure', 'Dehydration'],
    'shortness of breath': ['Asthma', 'COPD', 'Heart Failure'],
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
            f"<div style='background-color:#d4edda;padding:10px;border-radius:5px;'>Possible diseases based on your symptoms: <strong>{', '.join(diseases)}</strong></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background-color:#f8d7da;padding:10px;border-radius:5px;'>No possible diseases found.</div>",
            unsafe_allow_html=True
        )
else:
    st.write("Please select some symptoms to get suggestions.")
