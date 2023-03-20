# Import the necessary libraries
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import pickle


# Create a Flask app
app = Flask(__name__)
CORS(app)  # Add the CORS header

# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data
    data = request.json['data']
    data = np.array(data).reshape(1, -1)

    # Load the trained model and make a prediction
    with open('model/model.pkl', 'rb') as f:
        clf = pickle.load(f)
    prediction = clf.predict(data)[0]

    # Map the prediction to the class name
    if prediction == 0:
        class_name = 'setosa'
    elif prediction == 1:
        class_name = 'versicolor'
    else:
        class_name = 'virginica'

    # Return the prediction as a JSON object
    return jsonify({'prediction': class_name})

if __name__ == '__main__':
    app.run()
    # app.run(debug=True, host='0.0.0.0', port=5000)
