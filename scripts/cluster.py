import time

import docker
from docker.models.containers import ExecResult
from docker.models.resource import Model


class K0SCluster(object):
    image = 'docker.io/k0sproject/k0s'
    project: str
    tag: str

    master: Model | None = None

    def __init__(self, tag: str, project: str = 'k0s'):
        self.client = docker.from_env()
        self.tag = tag
        self.project = project

    def create_master(self):
        """Run master nodes"""

        container_name = '%s-master' % (self.project,)
        labels = dict(
            item='cluster',
            product='k0s',
            type='master',
        )
        volume = self.client.volumes.create(
            name=container_name,
            driver='local',
            labels=labels,
        )

        container = self.client.containers.run(
            image='%s:%s' % (self.image, self.tag),
            labels=labels,
            name=container_name,
            hostname=container_name,
            privileged=True,
            volumes={volume.name: {'bind':'/var/lib/k0s', 'mode': 'rw'}},
            ports={'6443/tcp': 6443},
            cgroupns='host',
            command='k0s controller',
            detach=True,
        )
        if container is None:
            return False
        self.master = container
        return True

    @property
    def master_token(self):
        """Get master token for create worker nodes"""
        while True:
            result: ExecResult = self.master.exec_run('k0s token create --role=worker')
            if result.exit_code != 0:
                time.sleep(1)
                continue
            return result.output.decode('utf-8')

    @property
    def admin_config(self):
        while True:
            result: ExecResult = self.master.exec_run('cat /var/lib/k0s/pki/admin.conf')
            if result.exit_code != 0:
                time.sleep(1)
                continue
            return result.output.decode('utf-8')

    def create_workers(self, count_nodes: int):
        """Run worker nodes"""
        token = self.master_token
        for i in range(count_nodes):
            container_name = '%s-worker-%s' % (self.project, i + 1,)
            labels = dict(
                item='cluster',
                product='k0s',
                type='worker',
            )
            volume = self.client.volumes.create(
                name=container_name,
                driver='local',
                labels=labels,
            )
            containers = self.client.containers.run(
                image='%s:%s' % (self.image, self.tag),
                labels=labels,
                name=container_name,
                hostname=container_name,
                volumes={volume.name: {'bind':'/var/lib/k0s', 'mode': 'rw'}},
                privileged=True,
                cgroupns='host',
                command='k0s worker %s' % (token,),
                detach=True,
            )

            while 1:
                if containers.status == 'created':
                    break
                time.sleep(0.1)

    def delete_cluster(self):
        containers = self.client.containers.list(
            all=True,
            filters=dict(
                label=['item=cluster', 'product=k0s']
            )
        )
        for container in containers:
            container.remove(force=True)

        volumes = self.client.volumes.list(
            filters=dict(
                label=['item=cluster', 'product=k0s']
            )
        )
        for volume in volumes:
            volume.remove(force=True)
