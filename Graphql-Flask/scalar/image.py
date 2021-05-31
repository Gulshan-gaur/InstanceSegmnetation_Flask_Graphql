import os
from graphql import GraphQLError
from models.user import User
path = 'modules/image'

def resolve_upload_image(root,info):
    filename , mimetype,encoding = info.context.get()
    fill = os.path.join(image,path)
    payload = {
      "filename":filename,
      "mimetype":mimetype,
      "encoding":encoding
    }
    return payload
    
