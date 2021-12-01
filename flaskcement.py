import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd


import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "_y1ceQWhf3ynP-jFc-gxoYPTSN75Fp0b6zhD0CepNoOs"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__) 
#model = pickle.load(open('cement.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html') 
@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('index1.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')
@app.route('/predict',methods=['POST','GET'])

def index():
            
    input_features = [float(x) for x in request.form.values()]
    print(input_features)
    features_value = [np.array(input_features)]
   # print(features_value)
    features_name = ['Cement', 'Blast Furnace Slag', 'Fly Ash', 'Water', 
                     'Superplasticizer','Coarse Aggregate', 'Fine Aggregate','Age']
    x = pd.DataFrame(features_value, columns=features_name)
    x_log=np.log(x)
        
   # prediction=model.predict(x_log)
   # print('prediction is', prediction)
        
        
    

    payload_scoring = {"input_data": [{"field": [["Cement","Blast Furnace Slag","Fly Ash","Water","Superplasticizer","Coarse Aggregate","Fine Aggregate","Age","Concrete compressive strength"]], "values":[ input_features]}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/96e55673-4865-4a04-b9c3-256fac49ffa9/predictions?version=2021-11-27', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    
    pred= response_scoring.json()
    print(pred)
    
    output = pred['predictions'][0]['values'][0][0]
    print(output)
    #print(response_scoring.json()['predictions'][0]['values'][0][0])
    
    return render_template('result2.html',prediction_text= output)

if __name__ == "__main__":
   # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=False)
    #app.run('0.0.0.0',8080) 