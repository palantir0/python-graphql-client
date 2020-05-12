from requests import post
import json

class GraphQLClient:
    """ A Simple GraphQL Client
    """
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def execute(self, query, variables=None, operationName=None):
        """ Run query on graphql endpoint
        """
        req = dict(query=query, variables=variables)
        if operationName is not None:
            req['operationName'] = operationName
        return post(self.endpoint, json=req, headers=self.headers).json()

    def addHeader(self, name, value):
        """ Addition headers that are needed for calls
        """
        self.headers[name] = value

    def addToken(self, value):
        """ Addition headers that are needed for alls - such as bearer token
        """
        self.headers['Authorization'] = value
