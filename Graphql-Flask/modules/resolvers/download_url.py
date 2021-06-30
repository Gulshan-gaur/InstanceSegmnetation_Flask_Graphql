import os
import sys
sys.path.insert(0,'../..')
from flask import send_file
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def download_file():
	identity = get_jwt_identity()
	oldUser = User.find_email_image({'email':identity})
	#if not oldUser:
	#raise GraphQLError(message="Something Went Wrong")
	#else:
	image = oldUser['images'][0]
	filepath = os.path.join('image',image)
	#obj = open(filepath,'rb')
	#print(obj.read())
	return send_file(filepath, as_attachment=True, attachment_filename=image)