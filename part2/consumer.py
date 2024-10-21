import os
import sys

import pika
from producer import QUEUE_NAME

from models import Contact


def send_email(contact):
    print(f"Email was sent to {contact}")


def main():
    credentials = pika.PlainCredentials("admin", "adminpassword")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    def callback(ch, method, properties, body):
        pk = body.decode()
        contact = Contact.objects(id=pk, is_sent=False).first()
        if contact:
            send_email(contact.fullname)
            contact.update(set__is_sent=True)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    print("Waiting for messages")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
