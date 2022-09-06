from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
#jwt_refresh_token_required, get_raw_jwt
from graphql import GraphQLError
from models.user import User
from ariadne import MutationType
import bcrypt

#mutation  =  MutationType()

#@mutation.field("create_user")
def resolve_login_user(root, info,email,password):

    """Creates a user in the database."""
    oldUser = User.find_by_email({"email":email})
    if oldUser:    
        hashedPassword = oldUser["password"]
        if bcrypt.checkpw(password.encode("utf-8"), hashedPassword):
            access_token = create_access_token(identity = oldUser['email'])
            refresh_token = create_refresh_token(identity = oldUser['email'])
            payload = {
               'access_token':access_token,
               'refresh_token':refresh_token
               }
            return payload
        else:
            raise GraphQLError(message="password not Matching",extensions={"code":404})
    else:
       raise GraphQLError("User not Register",extensions = {"code":404})
           
