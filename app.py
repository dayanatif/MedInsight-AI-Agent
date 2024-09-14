import streamlit as st

# Expanded Symptom-Disease and Symptom-Health Tips mapping
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
    'joint pain': ['Arthritis', 'Gout', 'Bursitis', 'Rheumatism'],
    'chills': ['Flu', 'Malaria', 'Typhoid', 'Sepsis'],
    'sweating': ['Hyperhidrosis', 'Menopause', 'Infections', 'Endocrine Disorders'],
}

symptom_health_tips_map = {
    'fever': [
        'Stay hydrated by drinking plenty of fluids.',
        'Rest and avoid strenuous activities.',
        'Use a cool compress to reduce fever.'
    ],
    'cough': [
        'Drink warm liquids to soothe your throat.',
        'Gargle with salt water to relieve throat irritation.',
        'Use a humidifier to keep the air moist.'
    ],
    'headache': [
        'Try over-the-counter pain relievers like ibuprofen.',
        'Rest in a dark, quiet room.',
        'Practice relaxation techniques to reduce stress.'
    ],
    'sore throat': [
        'Drink warm tea with honey to soothe your throat.',
        'Avoid spicy or acidic foods that may irritate your throat.',
        'Use throat lozenges to relieve discomfort.'
    ],
    'fatigue': [
        'Get adequate sleep and maintain a regular sleep schedule.',
        'Eat a balanced diet rich in fruits and vegetables.',
        'Exercise regularly to boost energy levels.'
    ],
    'nausea': [
        'Sip clear fluids slowly and avoid greasy foods.',
        'Try ginger tea or peppermint to ease nausea.',
        'Rest and avoid sudden movements.'
    ],
    'dizziness': [
        'Sit or lie down immediately to prevent falling.',
        'Stay hydrated and avoid sudden changes in position.',
        'Eat small, frequent meals to maintain stable blood sugar levels.'
    ],
    'shortness of breath': [
        'Try to stay calm and take slow, deep breaths.',
        'Use a prescribed inhaler if you have one.',
        'Avoid triggers like smoke or strong odors.'
    ],
    'chest pain': [
        'Seek immediate medical attention if chest pain is severe or persistent.',
        'Avoid heavy meals and try to relax.',
        'If you have a history of heart problems, follow your doctor\'s advice closely.'
    ],
    'abdominal pain': [
        'Avoid heavy or spicy foods that may aggravate pain.',
        'Drink plenty of water and rest.',
        'Consider over-the-counter antacids or pain relievers if needed.'
    ],
    'muscle pain': [
        'Apply ice or heat to the affected area.',
        'Rest and avoid overusing the muscles.',
        'Consider over-the-counter pain relievers if necessary.'
    ],
    'rash': [
        'Avoid scratching the affected area to prevent further irritation.',
        'Use over-the-counter anti-itch creams.',
        'Keep the affected area clean and dry.'
    ],
    'runny nose': [
        'Use a saline nasal spray to relieve congestion.',
        'Drink plenty of fluids to stay hydrated.',
        'Avoid allergens and irritants that may worsen symptoms.'
    ],
    'swollen lymph nodes': [
        'Rest and drink plenty of fluids.',
        'Apply warm compresses to the swollen areas.',
        'Consult a healthcare provider for further evaluation if swelling persists.'
    ],
    'joint pain': [
        'Rest and avoid activities that exacerbate the pain.',
        'Apply heat or cold packs to the affected joints.',
        'Consider over-the-counter anti-inflammatory medications.'
    ],
    'chills': [
        'Wear warm clothing and stay in a warm environment.',
        'Drink warm fluids to help regulate body temperature.',
        'Rest and avoid exposure to cold temperatures.'
    ],
    'sweating': [
        'Wear breathable, loose-fitting clothing.',
        'Stay hydrated and avoid excessive heat.',
        'Consider using antiperspirants to manage excessive sweating.'
    ],
}

def suggest_diseases(symptoms):
    possible_diseases = set()
    for symptom in symptoms:
        if symptom in symptom_disease_map:
            possible_diseases.update(symptom_disease_map[symptom])
    return list(possible_diseases)

def provide_health_tips(symptoms):
    tips = []
    for symptom in symptoms:
        if symptom in symptom_health_tips_map:
            tips.extend(symptom_health_tips_map[symptom])
    return tips

# Streamlit app
st.set_page_config(page_title="Medical AI Agent", layout="wide")

st.markdown("<h1 style='text-align: center;'>🩺 Medical AI Agent</h1>", unsafe_allow_html=True)

st.write(
    "Enter your symptoms to get possible diseases and health tips. This tool provides both a list of potential "
    "diseases and helpful tips based on the symptoms you select. Please remember that this is for informational "
    "purposes only and should not be used as a substitute for professional medical advice."
)

# Symptom selection
input_symptoms = st.multiselect(
    "Choose your symptoms:",
    options=symptom_disease_map.keys(),
    format_func=lambda x: x.capitalize()  # Capitalize symptom names
)

# Display results
if input_symptoms:
    diseases = suggest_diseases(input_symptoms)
    tips = provide_health_tips(input_symptoms)
    
    if diseases:
        st.markdown(
            f"<div style='background-color:#d1e7dd;padding:20px;border-radius:10px;color:#0f5132;font-size:18px;'>"
            f"<strong>Possible diseases based on your symptoms:</strong> {', '.join(diseases)}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background-color:#f8d7da;padding:20px;border-radius:10px;color:#721c24;font-size:18px;'>"
            "No possible diseases found based on the selected symptoms.</div>",
            unsafe_allow_html=True
        )
    
    if tips:
        st.markdown(
            f"<div style='background-color:#e2e3e5;padding:20px;border-radius:10px;color:#383d41;font-size:18px;'>"
            f"<strong>Health tips for your symptoms:</strong><ul>"
            f"{''.join(f'<li>{tip}</li>' for tip in tips)}</ul></div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background-color:#e2e3e5;padding:20px;border-radius:10px;color:#383d41;font-size:18px;'>"
            "No health tips available for the selected symptoms.</div>",
            unsafe_allow_html=True
        )
else:
    st.write("Please select some symptoms to get suggestions.")

# Disclaimer
st.markdown(
    "<div style='position: fixed; bottom: 60px; width: 100%; text-align: center; color: #721c24; font-size: 16px;'>"
    "<strong>Disclaimer:</strong> This tool provides potential disease suggestions and health tips based on symptoms. "
    "It is not a substitute for professional medical diagnosis or treatment. Always consult a healthcare provider for medical advice.</div>",
    unsafe_allow_html=True
)

# Additional informational line
st.markdown(
    "<div style='position: fixed; bottom: 30px; width: 100%; text-align: center; color: #721c24; font-size: 16px;'>"
    "Please remember that this is for informational purposes only and should not be used as a substitute for professional medical advice.</div>",
    unsafe_allow_html=True
)
