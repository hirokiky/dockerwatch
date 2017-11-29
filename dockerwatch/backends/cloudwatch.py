import time

import boto3

from dockerwatch.settings import settings


def get_client():
    return boto3.client(
        'cloudwatch',
        region_name=settings()['AWS_REGION_NAME'],
        aws_access_key_id=settings()['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=settings()['AWS_SECRET_ACCESS_KEY'],
    )


def get_asg_name():
    return settings()['AWS_ASG_NAME']


def send_stats(stats):
    client = get_client()
    n = stats.num_containers

    # Put NumberOfContainers
    client.put_metric_data(
        Namespace='Dockerwatch',
        MetricData=[{
            'MetricName': 'NumberOfContainers',
            'Dimensions': [
                {
                    'Name': 'AutoScalingGroupName',
                    'Value': get_asg_name()
                },
            ],
            'Timestamp': time.time(),
            'Value': n,
            'Unit': 'Count',
            'StorageResolution': 60,
        }]
    )
