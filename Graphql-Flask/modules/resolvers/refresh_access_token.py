from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from graphql import GraphQLError
from models.user import User

@jwt_required(refresh=True)
def resolve_access_token(root,info,refresh_token):
    identity= get_jwt_identity()
    access_token = create_access_token(identity=identity)
    payload = {
               'access_token':access_token,
               'message': "get access token"
           }
    
    return payload

@jwt_required(refresh=True)
def resolve_refresh_token(root,info,refresh_token):
    identity= get_jwt_identity()
    access_token = create_access_token(identity=identity)
    refresh_token = create_refresh_token(identity=identity)
    payload = {
               'access_token':access_token,
               'refresh_token':refresh_token,
               'message': "get access token"
           }
    
    return payload

