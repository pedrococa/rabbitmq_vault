# rabbitmq_vault 

Notes and scripts to demo Rabbitmq and Hashicorp Vault 

RabbitMQ is an open source message broker software implementing several message queuing protocols: AMQP, STOMP, MQTT, etc.
Hashicorp Vault is a tool for managing secrets.

This repo contains some notes and scripts to demo Vault with a RabbitMQ setup:

- Publisher.py
- Consumer.py
-
Carry out this demo on an Ubuntu 18.04 box with the Pika library (Python3) and with the RabbitMQ server running:

- sudo apt-get install rabbitmq-server
- sudo apt-get install python3-amqp 
- sudo apt-get install python3-pika python3-pika-pool

