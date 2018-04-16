
"""Basic package information."""
from __future__ import absolute_import
from setuptools import setup, find_packages

install_requires = [
    'lemur',

    # InfluxDB version should be frosen to this version until requests>=2.17
    # is used by Lemur.
    'influxdb==4.1.0'
]

setup(
    name='lemur-influxdb',
    version='1.0.0',
    author='Titouan Christophe',
    author_email='titouan.christophe@railnova.eu',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    license='MIT',
    entry_points={
        'lemur.plugins': [
            'influxdb = lemur_influxdb.plugin:InfluxDBMetricPlugin',
        ]
    }
)
