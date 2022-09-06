import sys
sys.path.insert(0,'../..')
import requests
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from graphql import GraphQLError
from models.user import User


def resolve_facebook(root,info,input):
	userToken = input["accessToken"]
	clientId = "379818356688158"
	clientSecret = "00f3347cba5844ca985c3c07156918e2"
	appLink = 'https://graph.facebook.com/oauth/access_token?client_id=' + clientId + '&client_secret=' + clientSecret + '&grant_type=client_credentials'

	appToken = requests.get(appLink).json()['access_token']

	link = 'https://graph.facebook.com/debug_token?input_token=' + userToken + '&access_token=' + appToken

	try:
		user_id = requests.get(link).json()['data']['user_id']
		userlink = 'https://graph.facebook.com/v11.0/'+ user_id + '?fields=name&access_token='+ appToken
		user_name = requests.get(userlink).json()

	except (ValueError, KeyError, TypeError) as error:
		raise GraphQLError ("somthing went wrong!")	

	return {
	    "name":user_name["name"]
	}  
