from kubernetes import client, config
from kubernetes.client.rest import ApiException


class BaseJob(object):
    def __init__(self, config_path=None, token=None):
        if config_path:
            config.load_kube_config(config_path)
            self.batch_client = client.BatchV1Api()
        # FIXME
        # elif token:
        #     configuration = client.Configuration()
        #     configuration.api_key['authorization'] = token
        #     # configuration.api_key_prefix['authorization'] = 'Bearer'
        #     print(dir(configuration))
        #     # configuration.ssl_ca_cert = '<path_to_cluster_ca_certificate>'
        #     self.batch_client = client.BatchV1Api(client.ApiClient(configuration))
        else:
            raise Exception

    def create(self):
        raise NotImplementedError

    def run(self, namespace='default'):
        resp = self.batch_client.create_namespaced_job(
            namespace=namespace,
            body=self.job
        )
        return resp

    def list(self, namespace):
        pretty = 'pretty_example'
        limit = 56
        timeout_seconds = 56

        try: 
            return self.batch_client.list_namespaced_job(namespace, pretty=pretty, limit=limit, timeout_seconds=timeout_seconds)
        except ApiException as e:
            print("Exception when calling BatchV1Api->list_namespaced_job: %s\n" % e)

    def fetch(self, name, namespace):
        pretty = 'pretty_example'
        
        try: 
            api_response = self.batch_client.read_namespaced_job(name, namespace, pretty=pretty)
            return api_response
        except client.rest.ApiException as e:
            print("Exception when calling BatchV1Api->read_namespaced_job: %s\n" % e)

    def delete(self, name, namespace):
        pretty = 'pretty_example'
        body = client.V1DeleteOptions()
        
        try:
            return self.batch_client.delete_namespaced_job(name=name, body=body, namespace=namespace)
        except client.rest.ApiException as e:
            print("Exception when calling BatchV1Api->delete_namespaced_job: %s\n" % e)
