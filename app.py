""""
This Flask-based web app serves three main functionalities:
✅ Home Page (/) – Displays a simple web UI
✅ Train Model (/train) – Runs the training pipeline
✅ Predict Values (/predict) – Takes user input & returns predictions
""""

from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page. When the user visits the root URL (/), it loads index.html (homepage).
def homePage():
    return render_template("index.html")

# Calls main.py, which likely contains the model training pipeline. Returns a success message upon completion.

@app.route('/train',methods=['GET'])  # route to train the pipeline 
def training():
    os.system("python main.py")
    return "Training Successful!" 

# Receives input from an HTML form (index.html). Extracts 11 numerical features related to wine quality prediction.
    
@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')

# Runs the Flask app on port 8080.0.0.0.0 allows external access (useful for Docker deployment).
if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)