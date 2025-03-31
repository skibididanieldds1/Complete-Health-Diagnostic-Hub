from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the heart models
heart_models = {
    'Logistic Regression': joblib.load('models/heart/Logistic Regression.pkl'),
    'K-Nearest Neighbors': joblib.load('models/heart/K-Nearest Neighbors.pkl'),
    'Decision Tree': joblib.load('models/heart/Decision Tree.pkl'),
    'Random Forest': joblib.load('models/heart/Random Forest.pkl'),
    'Support Vector Machine': joblib.load('models/heart/Support Vector Machine.pkl'),
}

# Load the kidney models
kidney_models = {
    'Logistic Regression': joblib.load('models/kidney/Logistic Regression kidney.pkl'),
    'K-Nearest Neighbors': joblib.load('models/kidney/K-Nearest Neighbors kidney.pkl'),
    'Decision Tree': joblib.load('models/kidney/Decision Tree kidney.pkl'),
    'Random Forest': joblib.load('models/kidney/Random Forest kidney.pkl'),
    'Support Vector Machine': joblib.load('models/kidney/Support Vector Machine kidney.pkl'),
}

# Load the liver models
liver_models = {
    'Logistic Regression': joblib.load('models/liver/Logistic Regression liver.pkl'),
    'K-Nearest Neighbors': joblib.load('models/liver/K-Nearest Neighbors liver.pkl'),
    'Decision Tree': joblib.load('models/liver/Decision Tree liver.pkl'),
    'Random Forest': joblib.load('models/liver/Random Forest liver.pkl'),
    'Support Vector Machine': joblib.load('models/liver/Support Vector Machine liver.pkl'),
}

# Load the liver models
diabetes_models = {
    'Logistic Regression': joblib.load('models/diabetes/Logistic Regression diabetes.pkl'),
    'K-Nearest Neighbors': joblib.load('models/diabetes/K-Nearest Neighbors diabetes.pkl'),
    'Decision Tree': joblib.load('models/diabetes/Decision Tree diabetes.pkl'),
    'Random Forest': joblib.load('models/diabetes/Random Forest diabetes.pkl'),
    'Support Vector Machine': joblib.load('models/diabetes/Support Vector Machine diabetes.pkl'),
}
# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Heart test route
@app.route('/heart-test')
def heart_test():
    return render_template('heart-test.html')

# Kidney test route
@app.route('/kidney-test')
def kidney_test():
    return render_template('Kidney-Test.html')

# Liver test route
@app.route('/liver-test')
def liver_test():  # Renamed to liver_test to avoid conflicts
    return render_template('liver-test.html')  # Ensure correct file name

# diabetes test route
@app.route('/diabetes-test')
def diabetes_test():
    return render_template('diabetes-Test.html')

# Heart prediction route
@app.route('/predict-heart', methods=['POST'])
def predict_heart():
    model_name = request.form['model']
    print(f"Heart model selected: {model_name}")  # Debugging output

    # Extract features
    features = [float(request.form[col]) for col in ['cp', 'trestbps', 'chol', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']]
    print(f"Heart features extracted: {features}")  # Debugging output

    # Apply scaler and model
    scaler = joblib.load('models/heart/scaler.pkl')
    features = scaler.transform([features])
    prediction = heart_models[model_name].predict(features)[0]
    print(f"Heart prediction result: {prediction}")  # Debugging output

    return render_template('heart-result.html', model_name=model_name, prediction=prediction)

# Kidney prediction route
@app.route('/predict-kidney', methods=['POST'])
def predict_kidney():
    model_name = request.form['model']
    print(f"Kidney model selected: {model_name}")  # Debugging output

    # Extract features
    features = [float(request.form[col]) for col in ['blood_glucose_random', 'blood_urea', 'packed_cell_volume', 'serum_creatinine', 'red_blood_cell_count']]
    print(f"Kidney features extracted: {features}")  # Debugging output

    # Apply scaler and model
    scaler = joblib.load('models/kidney/scale kidney.pkl')
    features = scaler.transform([features])
    prediction = kidney_models[model_name].predict(features)[0]
    print(f"Kidney prediction result: {prediction}")  # Debugging output

    return render_template('Kidney-result.html', model_name=model_name, prediction=prediction)

# Liver prediction route
@app.route('/predict-liver', methods=['POST'])
def predict_liver():  # Renamed function to predict_liver to avoid conflicts
    model_name = request.form['model']
    print(f"Liver model selected: {model_name}")  # Debugging output

    # Extract features
    features = [float(request.form[col]) for col in ['Age', 'BMI', 'AlcoholConsumption', 'LiverFunctionTest']]
    print(f"Liver features extracted: {features}")  # Debugging output

    # Apply scaler and model
    scaler = joblib.load('models/liver/scale liver.pkl')
    features = scaler.transform([features])
    prediction = liver_models[model_name].predict(features)[0]
    print(f"Liver prediction result: {prediction}")  # Debugging output

    return render_template('liver-result.html', model_name=model_name, prediction=prediction)

# diabetes prediction route
@app.route('/predict-diabetes', methods=['POST'])
def predict_diabetes():
    model_name = request.form['model']
    print(f"diabetes model selected: {model_name}")  # Debugging output

    # Extract features
    features = [float(request.form[col]) for col in ['Age','BMI','Glucose','Insulin']]
    print(f"diabetes features extracted: {features}")  # Debugging output

    # Apply scaler and model
    scaler = joblib.load('models/diabetes/scale diabetes.pkl')
    features = scaler.transform([features])
    prediction = diabetes_models[model_name].predict(features)[0]
    print(f"diabetes prediction result: {prediction}")  # Debugging output

    return render_template('diabetes-result.html', model_name=model_name, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
