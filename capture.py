from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['35.202.231.149:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number': e, 'mensaje': 'test3'}
    print(e)
    producer.send('testTopic', value=data)
    sleep(1)
