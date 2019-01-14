from kubernetes import client
from jobs import BaseJob


class PIJob(BaseJob):
    def __init__(self, config_path=None, token=None):
        super(PIJob, self).__init__(config_path, token)

    def create(self, name):
        self.job = client.models.V1Job(
            api_version='batch/v1', kind='Job',
            metadata=client.models.V1ObjectMeta(
                name=name,
            ),
            spec=client.models.V1JobSpec(
                active_deadline_seconds=600,
                completions=1,
                parallelism=1,
                # TODO: backoffLimit
                template=self.__get_pod()
            )
        )

    def __get_pod(self):
        pod_template_spec = client.models.V1PodTemplateSpec(
            spec=client.models.V1PodSpec(
                restart_policy='Never',
                containers=self.__get_containers()
                )
            )
        return pod_template_spec

    def __get_containers(self):
        command = ['perl']
        args = ['-Mbignum=bpi', '-wle', 'print bpi(2000)']
        memory_usage = {'memory': '128Mi'}
        containers = [
            client.models.V1Container(
                command=command,
                args=args,
                image='perl',
                image_pull_policy='IfNotPresent',
                name='pi',
                # env=[access_key_env, secret_key_env],
                resources=client.models.V1ResourceRequirements(limits=memory_usage, requests=memory_usage),
            )
        ]
        return containers
