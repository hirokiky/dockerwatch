=========
Dockermon
=========

Monitoring script for Docker.

Supported Metrics:

* Number of containers

Supported Backends:

* CloudWatch

Installation
============

::

    $ pip install dockermon

Usage
=====

::

   $ dockermon --settings=/path/to/dockermon.json


dockermon.json
--------------

.. code-block:: json

    {
      "DOCKER_API_VERSION": "1.30",
      "AWS_REGION_NAME": "...",
      "AWS_ACCESS_KEY_ID": "...",
      "AWS_SECRET_ACCESS_KEY": "...",
      "AWS_ASG_NAME": "..."
    }
