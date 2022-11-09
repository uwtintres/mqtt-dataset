# MQTT-Dataset v1.2

## Evaluating the Reliability of MQTT with Comparative Analysis<br/>
With the growing interest in Internet of Things (IoT) devices, a number of communication protocols have been developed to support a variety of IoT use cases. One promising communication paradigm that has been widely adopted in the IoT is the publish-subscribe pattern, which is supported by a number of messaging protocols such as MQTT, AMQP, and XMPP. Due to the diversity of IoT device types, an IoT application may communicate with IoT devices using a variety of messaging protocols, software frameworks, and strategies. To this extent, it becomes critical to determine the robustness of components responsible for message delivery (i.e., message brokers). We conduct a comparative study of the MQTT protocol's performance in this paper, comparing performance variables across a range of payload sizes and security levels. Preliminary results indicate that when the payload size remains small, using higher security levels does not result in significant latency overheads. Additionally, we discovered that implementing mutual authentication via Transport Layer Security (TLS) has no effect on MQTT response times in persistent connections when compared to using the default security level, which authenticates only the server.<br/>

For more details on this research study or if using the dataset, please cite the following papers:

Liu, Y., Al-Masri, E. Evaluating the Reliability of MQTT with Comparative Analysis. IEEE 4th International Conference on Knowledge Innovation and Invention (ICKII), (2021), pp. 24-29. https://doi.org/10.1109/ICKII51822.2021.9574783

Liu, Y., Al-Masri, E. Slow Subscribers: a novel IoT-MQTT based denial of service attack. Cluster Comput (2022). https://doi.org/10.1007/s10586-022-03788-9


How to use the dataset:
 - `data/` raw data
 - `agg/` data cleaning, aggregation, plotting
