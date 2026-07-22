import json
import time
import requests
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Starting Producer Stream...")

while True:
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url).json()
        data = {
            "symbol": "bitcoin",
            "price_usd": response["bitcoin"]["usd"],
            "timestamp": int(time.time())
        }
        producer.send('crypto_topic', value=data)
        print(f"Sent to Kafka: {data}")
        time.sleep(5)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
