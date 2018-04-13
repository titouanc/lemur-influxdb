
"""Basic package information."""
from __future__ import absolute_import
from setuptools import setup, find_packages

install_requires = [
    'lemur',
    'influxdb'
]

setup(
    name='lemur-influxdb',
    version='0.1',
    author='Titouan Christophe',
    author_email='titouan.christophe@arailnova.eu',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'lemur.plugins': [
            'influxdb = lemur_influxdb.plugin:InfluxDBMetricPlugin',
        ]
    }
)