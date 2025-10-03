import joblib
import pandas as pd
import numpy as np

model = joblib.load("xgb_model_joblib") 

age = int(input("Enter age: "))
bmi = float(input("Enter BMI: "))
children = int(input("Number of children: "))
sex = input("Sex (male/female): ").lower()
smoker = input("Smoker? (yes/no): ").lower()
region = input("Region (northeast/northwest/southeast/southwest): ").lower()

input_data = pd.DataFrame([{
    "age": age,
    "bmi": bmi,
    "children": children,
    "sex": sex,
    "smoker": smoker,
    "region": region
}])


log_prediction = model.predict(input_data)
prediction = np.exp(log_prediction)   

print(f"Estimated Medical Charges: {prediction[0]:,.2f} Dhs")
