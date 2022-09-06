from graphql import GraphQLError
from models.model import predict 

def resolve_imagePrediction(root,info,valInput):
    payload = {
     "prediction" : str(predict(valInput)[0]),
     "message" : "Wine Quality is good"   
    }
    
    return payload
 

