from ariadne import QueryType, MutationType

query = QueryType()

@query.field("hello")
def resolve_hello(root,info,name):
    return f'Hello {name}!'
