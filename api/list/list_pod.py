from flask_restplus import Resource, Namespace
from kubernetes import client, config
import pandas as pd

ns = Namespace('pod', description='pod api')

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()


@ns.route('/list_all_pods')
class ListPods(Resource):
    def get(self):
        v1 = client.CoreV1Api()
        ret = v1.list_pod_for_all_namespaces(watch=False)
        data_dict = {'ip': [], 'namespace': [], 'name': []}
        for i in ret.items:
            data_dict['ip'].append(i.status.pod_ip)
            data_dict['namespace'].append(i.metadata.namespace)
            data_dict['name'].append(i.metadata.name)
        df = pd.DataFrame(data_dict, columns=['ip', 'namespace', 'name'])
        data = df.to_dict(orient='records')
        return data

