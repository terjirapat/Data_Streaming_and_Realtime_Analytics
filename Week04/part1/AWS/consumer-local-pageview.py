from confluent_kafka import Consumer
import time

c = Consumer({
    'bootstrap.servers': 'ec2-13-229-46-113.ap-southeast-1.compute.amazonaws.com:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['streams-pageviewstats-untyped-output'])
              

print("Start consumer...")
while True:
    msg = c.poll(0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    value = msg.value().decode()
        
    kvalue = msg.key().decode("utf-8", "ignore")
    print('Received message: {0} , {1}'.format(kvalue, value))
    
    
c.close()

