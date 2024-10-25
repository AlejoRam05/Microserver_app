# products/producer.py
import aio_pika
import asyncio

async def send_message_to_queue(product_info):
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue("product_updates", durable=True)

    await channel.default_exchange.publish(
        aio_pika.Message(body=product_info.encode('utf-8')),
        routing_key=queue.name,
    )
    await connection.close()

# Call send_message_to_queue in product_router.py after adding a product



