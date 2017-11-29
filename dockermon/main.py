import argparse

from dockermon.backends.cloudwatch import send_stats
from dockermon.stats import retrieve_stats
from dockermon.settings import initial_settings


def main():
    parser = argparse.ArgumentParser(
        description="Command to send stats of Docker")
    parser.add_argument('--settings')
    args = parser.parse_args()

    initial_settings(args.settings)

    docker_stats = retrieve_stats()
    send_stats(docker_stats)
