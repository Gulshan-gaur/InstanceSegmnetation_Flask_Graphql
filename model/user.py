import datetime
import sys
sys.path.insert(0,'..')
from database.connection import Database
db= Database().db
#db = db_con.db

class User:
    '''
    user operation with database 
    '''
    def create(user_context):
        newUser = db.users.insert_one(user_context)
        user_context['id'] = newUser.inserted_id
        return user_context

    def find_by_email(userEmail):
        old_user = db.users.find_one(userEmail)
        return old_user
    
    #User find in images collection
    def find_email_image(userEmail):
        old_user = db.images.find_one(userEmail)
        return old_user
    
    # Image Upload in images collection acc. to their email id as primary key
    def image_upload(image_context):
        old_user = User.find_email_image({'email':image_context['email']})
        # check user in images collcetion
        if not old_user:
            record = [image_context['image']]
            imageUpload = db.images.insert_one({"email":image_context['email'],'images':record})
        else:
            if old_user['email']== image_context['email']:
                imageUpload = db.images.update_one({'email':image_context['email']},{'$push':{'images':image_context['image']}})
        return imageUpload
    
