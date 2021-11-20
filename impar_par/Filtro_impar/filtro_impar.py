import pika, sys, os

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='impar')

    def checar_valor(ch, method, properties, body):
        val = int(body)
        print(" [x] Valor recebido %r" % body)
        if(val % 2 == 1):
            print("O valor é impar")
            channel.exchange_declare(exchange='numero_impar', exchange_type='fanout')
            channel.basic_publish(exchange='numero_impar', routing_key='', body=str(val))
            print(" [x] Numero ímpar %d" % val)

    channel.basic_consume(queue='impar', on_message_callback=checar_valor, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)