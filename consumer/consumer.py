import logging
import json
from kafka import KafkaConsumer
import threading
from time import sleep

class Consumer(threading.Thread):
    daemon = True

    def json_deserializer(self, data):
        if data is None:
            return
        try:
            return json.loads(data.decode('utf-8'))
        except json.decoder.JSONDecodeError:
            self.logging.exception('Unable to decode: %s', data)
            return None

    def __init__(self, server, topic):
        self.logger = logging.getLogger()

        self.logger.info("Initializing Kafka Consumer")

        # Initialize consumer Instance
        self.consumer = KafkaConsumer(topic, bootstrap_servers=server,
                                 value_deserializer=self.json_deserializer)
        self.topic = topic

    def register_kafka_listener(self):

        self.logger.info("About to register listener to topic: {}".format(self.topic))
        # Poll kafka
        t1 = threading.Thread(target=self.poll)
        t1.start()
        self.logger.info("started a background thread")

    def poll(self):
        self.logger.info("About to start polling for topic: {}".format(self.topic))
        self.consumer.poll(timeout_ms=6000)
        for msg in self.consumer:
            self.kafka_listener(msg)


    def kafka_listener(self, message):
        self.logger.info('Consumer Received {}'.format(message))

