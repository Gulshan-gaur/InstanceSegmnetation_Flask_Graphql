from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers
from modules.resolvers.queries import query
from modules.resolvers.registerEmail import mutation


type_defs = load_schema_from_path("./modules/typeDefs")
schema = make_executable_schema(
     type_defs, query, mutation, snake_case_fallback_resolvers
)
    




