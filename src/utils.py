import os
import sys
import numpy as np
import pandas as pd
import pickle 
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(x_train, y_train, x_test, y_test, models, params):
    try:
        report = {}

        for model_name, model_value in models.items():
        
            model = model_value
            param = params.get(model_name, {})
            logging.info(f'{model} Training Started with {param}')
            grid = GridSearchCV(model, param, cv = 3)
            grid.fit(x_train, y_train)
            model.set_params(**grid.best_params_)
            model.fit(x_train, y_train)
            logging.info(f'{model} Training Over')
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score
        return report 
    
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try: 
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)