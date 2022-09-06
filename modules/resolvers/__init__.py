from ariadne import QueryType, MutationType
from modules.resolvers.registerEmail import resolve_create_user
from modules.resolvers.loginEmail import resolve_login_user
from modules.resolvers.queries import resolve_hello, resolve_user_data,resolve_own_data
from modules.resolvers.fileUpload import resolve_upload_image
from modules.resolvers.refresh_access_token import resolve_access_token,resolve_refresh_token
from modules.resolvers.wine_test import resolve_imagePrediction
from modules.resolvers.fileDownload import resolve_file_download
from modules.resolvers.registerFacebook import resolve_facebook


#Query 
query = QueryType()
query.set_field("hello", resolve_hello)
query.set_field("access_token", resolve_access_token)
query.set_field("refresh_token",resolve_refresh_token)
query.set_field("user_data",resolve_user_data)
query.set_field("own_data",resolve_own_data)
query.set_field("own_data",resolve_own_data)
query.set_field("download",resolve_file_download)

#Mutation
mutation = MutationType()
mutation.set_field("create_user",resolve_create_user)
mutation.set_field("login_user",resolve_login_user)
mutation.set_field("upload_image",resolve_upload_image)
mutation.set_field("predict_quality",resolve_wine_quality)
mutation.set_field("facebook_login",resolve_facebook)
