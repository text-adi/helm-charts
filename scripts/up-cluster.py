import sys
import time

from cluster import K0SCluster


def main(*args, **kwargs):
    params = dict()

    for arg in args:
        arg: str
        if '=' in arg and arg.startswith('--'):
            key, value = arg.lstrip('-').split('=')
            params[key] = value
    cluster = K0SCluster(params['tag'])
    cluster.delete_cluster()
    cluster.create_master()
    cluster.create_workers(int(params['workers']))
    while params['ready-wait']:
        if cluster.is_ready_nodes():
            break
        time.sleep(1)
    print(cluster.admin_config)


if __name__ == '__main__':
    main(*sys.argv)
