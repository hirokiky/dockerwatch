"""
Module to correct stats data from Docker.
"""
import docker

from dockerwatch.settings import settings


def get_client():
    return docker.from_env(
        version=settings()['DOCKER_API_VERSION'],
    )


class Stats(object):
    """ Data Class for stats from Docker.

    This class is just to store data and properties.
    """
    def __init__(self, num_containers=None):
        self.num_containers = num_containers

    def __repr__(self):
        return '''Docker Stats:
    num_containers: {self.num_containers}'''.format(self=self)


def retrieve_stats():
    """ Correct stasts/inspected data from Docker.
    """
    client = get_client()
    containers = client.containers.list()
    num_containers = len(containers)
    return Stats(
        num_containers=num_containers,
    )
