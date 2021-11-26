# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:16:26 2021

@author: DELL
"""

import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Y5rmT3QmTz-Nt9TF3rtGQxfN_1lWe4Rw1J80wkOrjTpW"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["Cement","Blast Furnace Slag","Fly Ash","Water","Superplasticizer","Coarse Aggregate","Fine Aggregate","Age","Concrete compressive strength"]], "values": [[540,0,0,162,2.5,1040,676,28 ]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7968dedb-2c9d-4c66-9b1e-aa8175734aff/predictions?version=2021-10-26', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json()['predictions'][0]['values'][0][0])