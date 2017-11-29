import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='dockerwatch',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/hirokiky/dockerwatch',
    license='MIT',
    author='Hiroki KIYOHARA',
    author_email='hirokiky@gmail.com',
    description='Monitoring script for Docker',
    long_description=README,
    install_requires=[
        'docker==2.6.1',
        'boto3==1.4.8',
    ],
    entry_points={
        'console_scripts': [
            'dockerwatch = dockerwatch.main:main',
        ],
    },
)
