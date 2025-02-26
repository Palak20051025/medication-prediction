from flask import Flask, render_template, request
import pandas as pd
from script import get_predicted_value, get_description, get_precautions, get_medications, get_workouts, get_diets

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/developer')
def developer():
    return render_template('developer.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_symptoms = request.form.get('symptoms', '').split(',')

        if not user_symptoms or user_symptoms == ['']:
            return render_template('index.html', message="Please enter symptoms")

        predicted_disease = get_predicted_value(user_symptoms)
        dis_des = get_description(predicted_disease)
        my_precautions = get_precautions(predicted_disease)
        medications = get_medications(predicted_disease)
        workout = get_workouts(predicted_disease)
        my_diet = get_diets(predicted_disease)

        return render_template(
            'index.html',
            predicted_disease=predicted_disease,
            dis_des=dis_des,
            my_precautions=my_precautions,
            medications=medications,
            workout=workout,
            my_diet=my_diet
        )

if __name__ == '__main__':
    app.run(debug=True)
