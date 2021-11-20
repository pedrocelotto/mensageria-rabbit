import pika
import random
import time

def main():
    # Conectando com o Rabbit
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    valor = str(random.randint(0,50))
    print('O valor é ', valor)

    # Criando fila
    channel.queue_declare(queue='impar')

    # Enviando msg para fila
    channel.basic_publish(exchange='',
                        routing_key='impar', #nome da fila
                        body=valor)
    connection.close()

if __name__ == '__main__':
    while(True):
        try:
            main()
            time.sleep(10)
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)