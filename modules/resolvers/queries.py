from flask_jwt_extended import jwt_required, get_jwt_identity
from graphql import GraphQLError
#from bson.objectid import ObjectId
from models.user import User

#@jwt_required()
def resolve_hello(root,info,name):
    return f'Hello {name}!'

@jwt_required()
def resolve_user_data(root,info,email):
    search_user = User.find_by_email({"email":email})
    if not search_user:
        raise GraphQLError(message="user does not exist",extensions={"code":404})
    else:
        payload = {
            "firstname":search_user['firstname'],
            "email": search_user['email'],
            "age":search_user['age']          
        }
    
    return payload

@jwt_required()
def resolve_own_data(root,info,user):
    identity= get_jwt_identity()
    search_user = User.find_by_email({"email":identity})
    if search_user:
        payload = {
            "id": search_user['_id'],
            "firstname":search_user['firstname'],
            "email": search_user['email'],
            "age":search_user['age']          
        }
    
        return payload
    else:
        raise GraphQLError(message="Something Went Wrong",extensions={"code":404})
            
