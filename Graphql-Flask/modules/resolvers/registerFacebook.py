import sys
sys.path.insert(0,'../..')
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
#jwt_refresh_token_required, get_raw_jwt
from graphql import GraphQLError
from models.user import User