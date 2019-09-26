# Python Kafka Example

Kafka Example in Python for Consuming and Producing to Kafka topic.
This project consists of a consumer and a producer. The producer sends four messages of type `{'message': {"dataObjectID": "test1"}}` in JSON format to kafka. 
The consumer continuously polls and reads any new messages on kafka. For simplicity the consumer is run first and producer later. 

### Pre-requisites

The example code relies on a running Kafka service and the consumer and the producer would be running in a docker.

* docker - [Instructions to install](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

_Note:_ The instructions are focused on Ubuntu however other environments will be supported with a bit of googling.

## Project Setup

Follow the instructions below to configure your local machine to run and develop this example Python application. 

##### Start the Kafka [Instructions to start](https://www.sohamkamani.com/blog/2017/11/22/how-to-install-and-run-kafka/)

##### Run the consumer 
* Go to consumer directory 
* Build the docker image 
> sudo docker build -t python-kafka-consumer
* Run the docker image 
> sudo docker run --network="host" -it --rm --name kafka-consumer --env TOPIC="topic-kafka" --env KAFKA_BROKERS="localhost:9092" <<consumer_docker_image>>

##### Run the Producer 
* Go to producer directory 
* Build the docker image 
> sudo docker build -t python-kafka-producer
* Run the docker image 
> sudo docker run --network="host" -it --rm --name kafka-producer --env TOPIC="topic-kafka" --env KAFKA_BROKERS="localhost:9092" <<producer_docker_image>>



_Note:_ Since the kafka is running on the same host --network="host" is used. Refer docker networks for more configurations



### Alternative approach

The project is developed using pyCharm. Therfore it can be imported and directly run from the pyCharm. The environment 
variables `TOPIC` and `KAFKA_BROKERS` must be set before running consumer and producer separately.
