#!/usr/bin/env python
import sys
import os
from datetime import datetime
import subprocess
import yaml
from kubernetes import client, config
from jobs.pi import PIJob


if __name__ == '__main__':
    job_client = PIJob(config_path=os.path.join(os.environ["HOME"], '.kube/config'))
    name = 'pi-' + str(int(datetime.now().timestamp()))
    namespace = 'default'
    job_client.create(name)
    res = job_client.run(namespace)
    res = job_client.fetch(name, namespace)
    res = job_client.list(namespace)
    res = job_client.delete(name, namespace)
