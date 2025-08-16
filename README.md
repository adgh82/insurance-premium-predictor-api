# Flask API to Predict Premium Price of an Individual

## About the API
This API loads the pickle file generated during the machine learning model training using the insurance dataset. 
It scales the numerical input parameters and encodes the categorical features and then use the loaded model to predict the premium price of an individual

## API Specification
### Request
URI : /get-premium 

Method : POST

Content-type : application/json

Sample Request : 

{

    "age": 35,
    
    "height": 148,
    
    "weight": 32,
    
    "diabetic": 0,
    
    "bp": 1,
    
    "transplant" : 1,
    
    "chronic" : 1,
    
    "allergy": 0,
    
    "cancer": 1,
    
    "surgery": 1
    
}

### Response
Content-type : application/json

Sample Response : 

{

    "premium": 37093.98
    
}
