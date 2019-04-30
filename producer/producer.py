import json
from kafka import KafkaProducer
import threading
import logging

class Producer(threading.Thread):
    daemon = True

    def __init__(self, server, topic):
        self.logger = logging.getLogger()

        self.logger.info("Initializing Kafka Producer")

        self.producer = KafkaProducer(bootstrap_servers=server,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        self.topic = topic

    def send_data(self, data):
        self.logger.info('Sending the data {} to topic {}'.format(data, self.topic))
        self.producer.send(self.topic, data)

