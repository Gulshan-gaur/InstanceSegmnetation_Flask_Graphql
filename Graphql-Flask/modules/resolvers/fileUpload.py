import os
import sys
sys.path.insert(0,'../..')
from graphql import GraphQLError
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def resolve_upload_image(root,info,image):
    fileitem= info.variable_values['image']
    identity= get_jwt_identity() # This variable has email id that can verify with database value
    #print(filename.filename)
    image = fileitem.filename
    image_context = {"email":identity,"image":image}
    image_upload = User.image_upload(image_context)
    filepath = os.path.join('image',image)
    fileitem.save(filepath)
    payload = {
      "filename":filepath,
      "message":"file uploaded"
    }
    return payload
    
