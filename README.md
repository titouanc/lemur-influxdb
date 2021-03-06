# lemur-influxdb

[InfluxDB](https://www.influxdata.com/) metric plugin for [Lemur](https://github.com/netflix/lemur).

## Installation

```
pip install -e git+https://github.com/titouanc/lemur-influxdb#egg=lemur-influxdb
```

## Configuration

Add the following to your `lemur.conf.py`:

```python
# Add to active metric providers
METRIC_PROVIDERS = ['influxdb']

# Set the following variables
INFLUXDB_HOST = "localhost"  # Where's the InfluxDB server
INFLUXDB_PORT = 8086         # On which port is it listening
INFLUXDB_UDP = False         # Whether to use the UDP protocol or http
INFLUXDB_DATABASE = "lemur"  # Name of the database for lemur's metrics
```

If any of the `INFLUX_*` variable is not set, it will use default
values. The declarations above show the default values.
