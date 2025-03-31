import joblib  # Loads the trained model from a file.
import numpy as np # Handles numerical and tabular data.
import pandas as pd
from pathlib import Path # Works with file paths in a clean way.



class PredictionPipeline: 
    def __init__(self):
        #Loads the trained model from the artifacts/model_trainer/ directory. Uses joblib.load() to deserialize and load the model.Stores the model in self.model for making predictions.
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib')) 

    
    def predict(self, data):
        prediction = self.model.predict(data) # Takes input data.Uses the trained model (self.model.predict(data)) to make predictions.

        return prediction # Returns the predicted output.