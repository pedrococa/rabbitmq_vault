#!/usr/bin/env python3

import pika

# A pika is a small mammal, with short limbs, very round body, rounded ears, and no external tail. 
# Pikas resemble their close cousin the rabbit :)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()
