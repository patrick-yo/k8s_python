from flask_restplus import Resource, Namespace
from kubernetes import client, config
# import pandas as pd

ns = Namespace('namespace', description='namespace api')

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()


@ns.route('/list_namespace')
class ListNamespace(Resource):
    def get(self):
        v1 = client.CoreV1Api()
        ret = v1.list_namespace()
        data = []
        for i in ret.items:
            data.append(i.metadata.name)
        return data

