import aio_pika

async def consume_queue():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue("product_updates", durable=True)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                print(f"Message received: {message.body.decode()}")
                # Here, you can handle the message, like updating the store inventory
