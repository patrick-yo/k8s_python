from flask import Blueprint
from flask_restplus import Api
from api.list.list_pod import ns as list_pod_api
from api.list.list_namespace import ns as list_ns_api

blueprint = Blueprint('list', __name__, url_prefix='/list')

api = Api(blueprint, title='list', version='1.0', description='1.0')

api.add_namespace(list_pod_api)
api.add_namespace(list_ns_api)


