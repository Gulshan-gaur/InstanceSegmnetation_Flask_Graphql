import sys
sys.path.insert(0,'../..')
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
#jwt_refresh_token_required, get_raw_jwt
from graphql import GraphQLError
from models.user import User
from ariadne import MutationType

mutation  =  MutationType()

@mutation.field("create_user")
def resolve_create_user(root, info, firstname,email, age):

    """Creates a user in the database."""
    if User.find_by_email({"email":email}):
       raise GraphQLError(message="user already exist",extensions={"code":404})
    else:
       user_context = {"firstname":firstname,"email":email,"age":age}
       try:
           newUser = User.create(user_context)
           access_token = create_access_token(identity = user_context['email'])
           refresh_token = create_refresh_token(identity = user_context['email'])
           payload = {
               'access_token':access_token,
               'refresh_token':refresh_token
           }
           return payload
       except:
           raise GraphQLError("somthing went wrong!")
