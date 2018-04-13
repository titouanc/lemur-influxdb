"""
.. module: lemur.plugins.lemur_influxdb.plugin
    :platform: Unix
    :copyright: (c) 2018 by Titouan Christophe., see AUTHORS for more
    :license: MIT, see LICENSE for more details.

.. moduleauthor:: Titouan Christophe <titouan.christophe@railnova.eu>
"""
from datetime import datetime

from influxdb import InfluxDBClient
from flask import current_app
from lemur.plugins.bases.metric import MetricPlugin


class InfluxDBMetricPlugin(MetricPlugin):
    title = 'InfluxDB'
    slug = 'influxdb'
    description = 'Adds support for sending key metrics to InfluxDB via the UDP interface'
    version = '0.1.0'

    author = 'Titouan Christophe'
    author_url = 'https://github.com/titouanc/lemur-influxdb'

    def __init__(self, *args, **kwargs):
        cfg = current_app.config
        host = cfg.get('INFLUXDB_HOST', 'localhost')
        port = cfg.get('INFLUXDB_PORT', 8086)
        udp = cfg.get('INFLUXDB_UDP', False)
        database = cfg.get('INFLUXDB_DATABASE', 'lemur')

        if udp:
            self.client = InfluxDBClient(host=host, udp_port=port,
                                         use_udp=True, database=database)
        else:
            self.client = InfluxDBClient(host=host, port=port,
                                         database=database)
        super(InfluxDBMetricPlugin, self).__init__(*args, **kwargs)

    def submit(self, metric_name, metric_type, metric_value, metric_tags=None, options=None):
        if not options:
            options = self.options

        current_app.logger.info("InfluxDB ignores metric types (got '%s')",
                                metric_type)

        if not metric_tags:
            metric_tags = {}

        if not isinstance(metric_tags, dict):
            raise Exception(
                "Invalid Metric Tags for InfluxDB: Tags must be in dict format"
            )

        payload = [{
            'measurement': metric_name,
            'tags': metric_tags,
            'time': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            'fields': {'value': metric_value},
        }]
        print(payload)
        self.client.write_points(payload)

