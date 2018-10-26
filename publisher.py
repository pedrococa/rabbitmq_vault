#!/usr/bin/env python3

import pika

# A pika is a small mammal, with short limbs, very round body, rounded ears, and no external tail. 
# Pikas resemble their close cousin the rabbit :)

# Set a connection, a channel and publish a hello message
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# Set a connection, a channel and publish a hello message
print(" [x] Sent 'Hello World!'")

# Close the connection
connection.close()
