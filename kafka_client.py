from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='104.197.55.247:9092')
producer.send('FirstTopic', b'Hello, World RaspberryZero!')
producer.send('FirstTopic', key=b'message-two', value=b'This is Kafka-Python from RaspberryZero')