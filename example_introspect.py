#!/usr/bin/env python

from graphqlclient import GraphQLClient
from pprint import PrettyPrinter
import json

'''
How to run this example with a simplest adriadne server

A simple server is documented at https://ariadnegraphql.org/docs/intro

Change this line in the complete code at the bottom of the intro page: 
    from ariadne.asgi import GraphQL
into 
    from ariadne.wsgi import GraphQL

And add the following to the end of the code to run a built-in wsgi server: 

    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8000, app)
    httpd.handle_request()
    httpd.serve_forever(.1)

Note that the resolver there may not be able to run `info.context["request"]`. 
Just comment those lines out and return some dummy strings, if that happens. 
'''


def main():
    # assume a server is running at `localhost:8000`:
    url = 'http://localhost:8000/'
    # or use this:  url = 'http://swapi.graph.cool/'
    client = GraphQLClient(url)

    # the introspection query request below was copied from a playground in a browser
    # when running an adriadne server.
    query_introspect_raw = '''{"operationName":"IntrospectionQuery","variables":{},"query":"query IntrospectionQuery {\n  __schema {\n    queryType {\n      name\n    }\n    mutationType {\n      name\n    }\n    subscriptionType {\n      name\n    }\n    types {\n      ...FullType\n    }\n    directives {\n      name\n      description\n      locations\n      args {\n        ...InputValue\n      }\n    }\n  }\n}\n\nfragment FullType on __Type {\n  kind\n  name\n  description\n  fields(includeDeprecated: true) {\n    name\n    description\n    args {\n      ...InputValue\n    }\n    type {\n      ...TypeRef\n    }\n    isDeprecated\n    deprecationReason\n  }\n  inputFields {\n    ...InputValue\n  }\n  interfaces {\n    ...TypeRef\n  }\n  enumValues(includeDeprecated: true) {\n    name\n    description\n    isDeprecated\n    deprecationReason\n  }\n  possibleTypes {\n    ...TypeRef\n  }\n}\n\nfragment InputValue on __InputValue {\n  name\n  description\n  type {\n    ...TypeRef\n  }\n  defaultValue\n}\n\nfragment TypeRef on __Type {\n  kind\n  name\n  ofType {\n    kind\n    name\n    ofType {\n      kind\n      name\n      ofType {\n        kind\n        name\n        ofType {\n          kind\n          name\n          ofType {\n            kind\n            name\n            ofType {\n              kind\n              name\n              ofType {\n                kind\n                name\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}\n"}'''
    query_introspect = query_introspect_raw.replace('\n', '\\n')
    req = json.loads(query_introspect)

    query = req.get('query', None)
    vars = req.get('variables', None)
    oper = req.get('operationName', None)
    if query is None or vars is None:
        return

    result = client.execute(query, variables=vars, operationName=oper)

    pp = PrettyPrinter(indent=4)
    pp.pprint(result)

if __name__ == '__main__':
    main()
