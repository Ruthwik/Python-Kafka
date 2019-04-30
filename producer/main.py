import logging
import time
import os

from producer import Producer

class Main(object):

    def __init__(self):
        if 'KAFKA_BROKERS' in os.environ:
            self.kafka_broker = os.environ['KAFKA_BROKERS']
        else:
            raise ValueError('KAFKA_BROKERS environment variable not set')

        if 'TOPIC' in os.environ:
            self.topic = os.environ['TOPIC']
        else:
            raise ValueError('TOPIC environment variable not set')

        self.logger = logging.getLogger()

        self.logger.info("KAFKA_BROKERS={}".format(self.kafka_broker))
        self.logger.info("TOPIC={}".format(self.topic))

    def run(self):

        producer = Producer(self.kafka_broker, self.topic)

        self.logger.info("Running Kafka Producer")

        for i in range(1, 5):
            data1 = {'message': {"dataObjectID": "test"+ str(i)}}
            producer.send_data(data1)
            time.sleep(4)


if __name__ == "__main__":

    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )

    logging.info("Initializing the server....")
    main = Main()
    main.run()