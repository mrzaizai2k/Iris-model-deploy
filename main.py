# Import the necessary libraries
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, jsonify, request
import numpy as np
import pickle
import os

directory = 'model'
if not os.path.exists(directory):
    os.makedirs(directory)
    file = open('model/.gitignore.txt', 'w+')

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

# Save the trained model
with open('model/model.pkl', 'wb') as f:
    pickle.dump(clf, f)