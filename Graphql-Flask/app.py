from flask import Flask, request, jsonify
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

#query = ObjectType("Query")
#query.set_field("hello", resolve_hello)
#Graphql Schema 
#type_defs = load_schema_from_path("modules/schema.graphql")
schema = schema#make_executable_schema(
    #type_defs, query, snake_case_fallback_resolvers
#)
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
