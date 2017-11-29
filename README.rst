===========
Dockerwatch
===========

Monitoring script for Docker.

Supported Metrics:

* Number of containers

Supported Backends:

* CloudWatch

Installation
============

::

    $ pip install dockerwatch

Usage
=====

::

   $ dockerwatch --settings=/path/to/dockerwatch.json


dockerwatch.json
-----------------

.. code-block:: json

    {
      "DOCKER_API_VERSION": "1.30",
      "AWS_REGION_NAME": "...",
      "AWS_ACCESS_KEY_ID": "...",
      "AWS_SECRET_ACCESS_KEY": "...",
      "AWS_ASG_NAME": "..."
    }
