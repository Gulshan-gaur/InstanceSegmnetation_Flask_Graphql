import sys
sys.path.insert(0,'../..')
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
#jwt_refresh_token_required, get_raw_jwt
from graphql import GraphQLError
from models.user import User
import bcrypt


def resolve_create_user(root, info, firstname,email, password,age):

    """Creates a user in the database."""
    old_user = User.find_by_email({"email":email})
    if not old_user:
        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        user_context = {"firstname":firstname,"email":email,"password":password,"age":age}
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

    else:
        if old_user["email"]==email:   
           raise GraphQLError(message="user already exist",extensions={"code":404})
       
