import os
import sys
sys.path.insert(0,'../..')
from graphql import GraphQLError
from models.user import User
from flask_jwt_extended import  jwt_required


def resolve_upload_image(root,info,image):
    print(info)
    fileitem= info.variable_values['image']
    #print(filename.filename)
    image = fileitem.filename
    filepath = os.path.join('image',image)
    fileitem.save(filepath)
    payload = {
      "filename":filepath,
      "message":"file uploaded"
    }
    return payload
    
