from flask_restful import Api
from api.domains.signin.view import SignInView
from api.domains.token.view import TokenView
from api.domains.users.view import UserView

def routes(api: Api):
  api.add_resource(UserView, '/users')
  api.add_resource(SignInView, '/signin')
  api.add_resource(TokenView, '/token/validate')