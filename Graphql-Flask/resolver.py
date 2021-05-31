from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers,upload_scalar
from modules.resolvers import query,mutation


type_defs = load_schema_from_path("./modules/typeDefs")
schema = make_executable_schema(
     type_defs, query, mutation, [upload_scalar], snake_case_fallback_resolvers
)
    





