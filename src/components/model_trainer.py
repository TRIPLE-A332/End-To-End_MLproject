import os
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object , evaluate_models

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

from  sklearn.metrics import (
    r2_score , 
    mean_squared_error , 
    root_mean_squared_error,
    mean_absolute_error
)

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifact" , "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_conig = ModelTrainerConfig()

    def initiate_model_trainer(self , training_array , test_array ):
        try:
            logging.info("Splitting train test input data")

            X_train , y_train , X_test , y_test = (
                training_array[:,:-1],
                training_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            
            models = {
                "Lineear Regression" : LinearRegression(),
                "Support Vector Regression" : SVR(),
                "knn" : KNeighborsRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Random Forest" : RandomForestRegressor(),
                "XGBoost" : XGBRegressor(),
                "CatBoost" : CatBoostRegressor(verbose=False),
                "AdaBoost" : AdaBoostRegressor(),
                "Gradient Boost" : GradientBoostingRegressor()
            }

            test_model_report:dict = evaluate_models(
                X_train=X_train , 
                y_train=y_train , 
                X_test=X_test , 
                y_test=y_test, 
                models=models
                )

            best_test_model_score = max(sorted(test_model_report.values()))

            best_test_model_name = list(test_model_report.keys())[
                list(test_model_report.values()).index(best_test_model_score)
            ]
            best_model = models[best_test_model_name]

            if best_test_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info("best model found")

            save_object(
                file_path = self.model_trainer_conig.trained_model_file_path ,
                obj= best_model
            )

            predicted = best_model.predict(X_test)
            r2score = r2_score(y_test , predicted)

            return r2score


        except Exception as e:
            raise CustomException(e,sys)