# Expert System for diagnosing diseases
# Use if-else statements or similar to differentiate btwn similar diseases

# The expert system
# Dict of lists of symptoms
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

def mediexpert():
    '''
    Medical expert system for diagnosing diseases
    '''
    print("Welcome to the Medical Expert System!")
    print("Please answer the following with 'y' or 'n':\n")
    symptoms = []
    asked = set()
    for disease, symlist in medical_expert.items():
        for symptom in symlist:
            if symptom not in asked:
                asked.add(symptom)
                ans = input(f"Do you have {symptom}? ").strip().lower()
                if ans == 'y':
                    symptoms.append(symptom)

    scores = {}
    for disease, symlist in medical_expert.items():
        match_count = len(set(symlist) & set(symptoms))
        scores[disease] = match_count

    best_disease = max(scores, key=scores.get)
    
    if scores[best_disease] == 0:
        print("\nDiagnosis: Symptoms do not match any known disease in the system.")
        print("You are probably healthy, have a nice day!")
    else:
        print(f"\nDiagnosis: You may have {best_disease.upper()} based on your symptoms.")
        print(f"Matching symptoms: {scores[best_disease]} out of {len(medical_expert[best_disease])}")
        print("Please refer to a certified medical expert in that field")

if __name__ == "__main__":
    mediexpert()