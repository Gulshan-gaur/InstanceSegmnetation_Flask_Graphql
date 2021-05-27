from ariadne import QueryType, MutationType
from flask_jwt_extended import jwt_required

@jwt_required()
def resolve_hello(root,info,name):
    return f'Hello {name}!'
