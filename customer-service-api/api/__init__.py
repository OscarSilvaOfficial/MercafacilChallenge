from flask import Flask
from api.urls import routes
from flask_restful import Api

def flask_instance(flask=Flask):
  app = flask(__name__)
  return app

def flask_restful(app):
  api = Api(app)
  api.prefix = '/api'
  return api

def application():
  app = flask_instance()
  api = flask_restful(app)
  routes(api)
  return app