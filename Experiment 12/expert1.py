# Expert System for diagnosing diseases
# Asks only relevant questions (not all symptoms)

medical_expert = {
    'covid-19': ['fever', 'dry cough', 'tiredness', 'loss of taste or smell', 'difficulty breathing'],
    'flu': ['fever', 'chills', 'muscle aches', 'cough', 'fatigue'],
    'common_cold': ['sneezing', 'stuffy nose', 'sore throat', 'mild cough'],
    'dengue': ['high fever', 'severe headache', 'pain behind eyes', 'joint pain', 'rash'],
    'malaria': ['fever', 'chills', 'sweating', 'headache', 'nausea'],
    'typhoid': ['fever', 'abdominal pain', 'weakness', 'loss of appetite', 'constipation'],
    'pneumonia': ['fever', 'chest pain', 'cough with phlegm', 'difficulty breathing', 'fatigue'],
    'bronchitis': ['persistent cough', 'chest discomfort', 'fatigue', 'shortness of breath', 'mild fever'],
    'asthma': ['shortness of breath', 'chest tightness', 'wheezing', 'cough (night/morning)', 'fatigue'],
    'sinusitis': ['headache', 'facial pain', 'stuffy nose', 'postnasal drip', 'sore throat']
}

def get_best_symptom(candidates, asked):
    """
    Choose the symptom that appears in about half the diseases (best for splitting).
    """
    freq = {}
    for disease in candidates:
        for symptom in medical_expert[disease]:
            if symptom not in asked:
                freq[symptom] = freq.get(symptom, 0) + 1

    if not freq:
        return None

    # Best symptom is the one closest to splitting the list of diseases in half
    total = len(candidates)
    best_symptom = min(freq.keys(), key=lambda s: abs(freq[s] - total / 2))
    return best_symptom

def mediexpert():
    print("Welcome to the Medical Expert System!")
    print("Please answer the following with 'y' or 'n':\n")

    candidates = list(medical_expert.keys())
    symptoms_yes = set()
    symptoms_no = set()
    asked = set()

    while len(candidates) > 1:
        symptom = get_best_symptom(candidates, asked)
        if not symptom:
            break  # No new symptoms to ask

        asked.add(symptom)
        ans = input(f"Do you have {symptom}? ").strip().lower()
        if ans == 'y':
            symptoms_yes.add(symptom)
            # Keep only diseases that have this symptom
            candidates = [d for d in candidates if symptom in medical_expert[d]]
        else:
            symptoms_no.add(symptom)
            # Remove diseases that have this symptom
            candidates = [d for d in candidates if symptom not in medical_expert[d]]

    # Result interpretation
    if len(candidates) == 1:
        disease = candidates[0]
        print(f"\nDiagnosis: You may have {disease.upper()} based on your symptoms.")
        print("Please consult a certified medical expert for confirmation.")
    elif len(candidates) > 1:
        print("\nPossible diseases based on your answers:")
        for d in candidates:
            print(f"- {d}")
        print("Consider consulting a doctor for detailed diagnosis.")
    else:
        print("\nDiagnosis: Your symptoms do not match any known diseases.")
        print("You may be healthy or have a condition outside this system's scope.")

if __name__ == "__main__":
    mediexpert()
