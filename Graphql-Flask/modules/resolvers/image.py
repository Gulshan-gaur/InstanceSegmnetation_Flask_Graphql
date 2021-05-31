import os
from graphql import GraphQLError
from models.user import User

def resolve_upload_image(root,info,image):
    filename= info.context
    print(filename)
    photo = filename
    fill = os.path.join(photo,'../image')
    payload = {
      "filename":fill,
    }
    return payload
    
