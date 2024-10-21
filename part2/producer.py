import pika
from faker import Faker

from models import Contact


EXCHANGE_NAME = "Email service"
QUEUE_NAME = "sending emails"
fake = Faker()

credentials = pika.PlainCredentials("admin", "adminpassword")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="direct")
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME)


def create_email_task(nums: int):
    for i in range(nums):
        contact = Contact(fullname=fake.name(), email=fake.email()).save()

        channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=QUEUE_NAME,
            body=str(contact.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )

    connection.close()


if __name__ == "__main__":
    create_email_task(5)
