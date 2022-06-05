This folder contains raw timing data collected from the MQTT broker setup.

Tentatively, each file has 5 fields of metadata associated with it:
qos, security_level, clients, topics, timeout

The `_CLEANED` files have large response time values removed. Unless you are writing your own code to load data, using the `_CLEANED` files is not necessary as the dataset processing methods in `agg/` already does filtering.
