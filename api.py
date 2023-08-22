import json
#import requests
import urllib.request

def lambda_handler(event, context):
    url = "https://ij92qpvpma.execute-api.eu-west-1.amazonaws.com/candidate-email_serverless_lambda_stage/data"
    headers = { "Content-Type" : "application/json", "X-Siemens-Auth" : "test"}
    payload = {
    "subnet_id": "subnet-0531d09d8f4122ce7",
    "name": "vinay patange",
    "email": "vinaydp78@gmail.com"
    } # replace with your request parameters
    
    response = urllib.request.post(url, headers=headers, data=json.dumps(payload))
    return {
        "statusCode": response.status_code,
        "body": response.json()
    }
    
    #conn = http.client.HTTPSConnection("https://ij92qpvpma.execute-api.eu-west-1.amazonaws.com/candidate-email_serverless_lambda_stage/data")
    #conn.request("POST", "/endpoint", body=payload, headers=headers)
    
    #response = conn.getresponse()
    #response_data = response.read().decode("utf-8")
    
    # Return the response data
    #return {
    #    "statusCode": response.status,
     #   "body": response.json()
    #}
    