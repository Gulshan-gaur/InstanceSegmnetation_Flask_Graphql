from ariadne import QueryType, MutationType
from modules.resolvers.registerEmail import resolve_create_user
from modules.resolvers.loginEmail import resolve_login_user
from modules.resolvers.queries import resolve_hello
from modules.resolvers.image import resolve_upload_image
from modules.resolvers.refresh_access_token import resolve_access_token,resolve_refresh_token

#Query 
query = QueryType()
query.set_field("hello", resolve_hello)
query.set_field("access_token", resolve_access_token)
query.set_field("refresh_token",resolve_refresh_token)
#Mutation
mutation = MutationType()
mutation.set_field("create_user",resolve_create_user)
mutation.set_field("login_user",resolve_login_user)
mutation.set_field("upload_image",resolve_upload_image)
