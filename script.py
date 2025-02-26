import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Load datasets
symptoms_df = pd.read_csv('datasets/symptoms_df.csv')
description_df = pd.read_csv('datasets/description.csv')
precautions_df = pd.read_csv('datasets/precautions_df.csv')
medications_df = pd.read_csv('datasets/medications.csv')
workout_df = pd.read_csv('datasets/workout_df.csv')
diets_df = pd.read_csv('datasets/diets.csv')
training_df = pd.read_csv('datasets/Training.csv')

# Prepare symptom dictionary
print(symptoms_df.head())  # Debugging: Check if headers are correct

# Verify if correct column exists, otherwise fix it
if 'Symptom' in symptoms_df.columns:
    symptoms_dict = {symptom: index for index, symptom in enumerate(symptoms_df['Symptom'])}
else:
    print("⚠️ Error: 'Symptom' column not found in CSV. Check dataset headers!")

# Train a basic model using Decision Tree
X = training_df.iloc[:, :-1]
y = training_df.iloc[:, -1]
model = DecisionTreeClassifier()
model.fit(X, y)

# Function to get disease prediction
def get_predicted_value(symptoms):
    # Ensure the input vector has the same number of features as the trained model
    input_vector = np.zeros(len(symptoms_df))  # Create a zero vector of correct length

    for symptom in symptoms_df:
        if symptom in symptoms_df:  # Check if symptom exists in dictionary
            input_vector[symptoms_df[symptom]] = 1  # Set the corresponding index to 1

    input_vector = np.array(input_vector).reshape(1, -1)  # Reshape to match model input
    prediction = model.predict(input_vector)  # Make prediction

    return prediction[0]  # Return predicted disease

# Function to get disease description
def get_description(disease):
    return description_df.loc[description_df['Disease'] == disease, 'Description'].values[0]

# Function to get precautions
def get_precautions(disease):
    return precautions_df.loc[precautions_df['Disease'] == disease].values.tolist()[0][1:]

# Function to get medications
def get_medications(disease):
    return medications_df.loc[medications_df['Disease'] == disease].values.tolist()[0][1:]

# Function to get workouts
def get_workouts(disease):
    return workout_df.loc[workout_df['Disease'] == disease].values.tolist()[0][1:]

# Function to get diet recommendations
def get_diets(disease):
    return diets_df.loc[diets_df['Disease'] == disease].values.tolist()[0][1:]
