import sys
sys.path.insert(0,'../..')
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
           return newUser
       except:
           raise GraphQLError("somthing went wrong!")
