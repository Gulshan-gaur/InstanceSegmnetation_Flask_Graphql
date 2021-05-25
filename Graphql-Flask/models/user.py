import datetime
import sys
sys.path.insert(0,'..')
from database.connection import Database
db_con= Database()
db = db_con.db
class User():
    def create(user_context):
        newUser = db.users.insert_one(user_context)
        user_context['id'] = newUser.inserted_id
        return user_context

    def  find_by_email(userEmail):
        old_user = db.users.find_one(userEmail)
        if old_user:
             return True
        else:
             return False
