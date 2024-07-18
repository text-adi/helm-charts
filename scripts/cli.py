import time

import click

from cluster import K0SCluster


@click.group()
def cli():
    pass


@click.command('up-cluster')
@click.option('--tag', help='Version docker images', type=str)
@click.option('--workers', help='Count workers', type=int)
@click.option('--ready-wait', is_flag=True, help='Count workers', type=bool, default=False)
@click.option('--force', is_flag=True, help='Count workers', type=bool, default=False)
def up_cluster(tag: str, workers: int, ready_wait: bool, force: bool):
    cluster = K0SCluster(tag)
    if force:
        cluster.delete_cluster()
    cluster.create_master()
    cluster.create_workers(workers)

    while ready_wait:
        if cluster.is_ready_nodes():
            break
        time.sleep(1)
    print(cluster.admin_config)


cli.add_command(up_cluster)

if __name__ == '__main__':
    cli()
