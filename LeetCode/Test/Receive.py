#!/user/bin/env python3
# -*- coding: utf-8 -*-

import pika

hostname = 'localhost'
parameters = pika.ConnectionParameters(hostname)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %4" % (body, ))

channel.basic_consume(callback, queue='hello', no_ack=True)

print("[*] Waiting for message. To exit press CRTL+C")

channel.start_cosuming()
