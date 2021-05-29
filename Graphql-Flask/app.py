from flask import Flask, request, jsonify
from datetime import timedelta
#from config import Devconfig
from flask_jwt_extended import JWTManager
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from database import connection
from resolver import schema

# initialise flask object
app = Flask(__name__)

# database connection
connect_db = connection.Database()
db = connect_db.db
context_app = {
    'mongoClient': db,
}
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=2)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
jwt =JWTManager(app)
'''app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)'''
#app.config = Devconfig.JWT_SECRET_KEY
schema = schema
# Create home route

@app.route("/")
def home():
   # todos = db.user.find()
    return "Hello world " 

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=context_app,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code




if __name__ == '__main__':
  app.run(debug=True)
