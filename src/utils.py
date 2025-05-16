
import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import r2_score


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        print(e)


def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train, y_train)

            # Predict
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Evaluate
            train_r2 = r2_score(y_train, y_train_pred)
            test_r2 = r2_score(y_test, y_test_pred)

            # Save score to report
            report[list(models.keys())[i]]= test_r2

        return report

    except Exception as e:
        print(e)
        return None  # Prevent crashing if something goes wrong


import pickle

def load_object(filepath):
    try:
        with open(filepath, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise Exception(f"Error loading the transformer or model: {e}")

