import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='numero_impar', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='numero_impar', queue=queue_name)

print(' [*] Waiting for alerts. To exit press CTRL+C')

def acionar_aviso(ch, method, properties, body):
    body = 0
    print(" [x] Zerando o valor: %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=acionar_aviso, auto_ack=True)

channel.start_consuming()
