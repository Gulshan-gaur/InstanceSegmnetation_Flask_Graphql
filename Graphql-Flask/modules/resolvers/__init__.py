from ariadne import QueryType, MutationType
from modules.resolvers.registerEmail import resolve_create_user
from modules.resolvers.queries import resolve_hello

#Query 
query = QueryType()
query.set_field("hello", resolve_hello)
#Mutation
mutation = MutationType()
mutation.set_field("create_user",resolve_create_user)
