import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_json
from pathlib import Path

# Initializes the class with ModelEvaluationConfig, which provides test data path, model path, and MLflow details.
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    # Computes Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R² Score for model evaluation.
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    

    # Loads the test dataset and trained model.Separates features (test_x) and target column (test_y).
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Connects to MLflow tracking server (DagsHub or local).
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

      
        # Runs model inference on test data. Computes evaluation metrics using eval_metrics().
        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Saving metrics as local. Saves the metrics as a JSON file.
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            # Logs the model parameters & evaluation metrics to MLflow.
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


            # Model registry does not work with file store. Registers the trained model in MLflow, allowing version tracking & deployment.
            if tracking_url_type_store != "file":  

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel") # If MLflow is remote (DagsHub) → Register as "ElasticnetModel"
            else:
                mlflow.sklearn.log_model(model, "model") # If local MLflow → Just log the model.



    
