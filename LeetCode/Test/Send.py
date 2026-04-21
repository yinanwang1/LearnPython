#!/user/bin/env python3
# -*- coding: utf-8 -*-


import pika
import random

hostname = 'localhost'
parameters = pika.ConnectionParameters(hostname)
connection = pika.BlockingConnection(parameters)


channel = connection.channel()
channel.queue_declare(queue='hello')

number = random.randint(1, 1000)
body = 'hello world:%s' % number


channel.basic_publish(exchange='', routing_key='hello', body=body)
print("[x] Sent %s" % body)

connection.close()