import json
import time
import random
import os
from kafka import KafkaProducer

BROKER = os.getenv("KAFKA_BROKER", "localhost:19092")
TOPIC = "retail-operations"

# Keep trying to connect to Kafka if it's booting up
for _ in range(10):
    try:
        producer = KafkaProducer(
            bootstrap_servers=[BROKER],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        break
    except Exception:
        time.sleep(3)

stores = ["STORE_BLR_01", "STORE_DWR_02", "STORE_MUM_03", "STORE_DEL_04"]
materials = ["MAT_1001_DENIM", "MAT_2002_SHIRT", "MAT_3003_JACKET"]

while True:
    # 90% Normal Operations, 10% Anomalies/Errors
    is_weird_event = random.random() < 0.10
    
    event = {
        "store_id": random.choice(stores),
        "material_id": random.choice(materials),
        "quantity": random.randint(1, 5) if not is_weird_event else random.randint(40, 100),
        "amount": round(random.uniform(500, 3000), 2) if not is_weird_event else round(random.uniform(25000, 50000), 2),
        "idoc_status": "30" if not is_weird_event else "51" # 51 is SAP standard for Error/IDoc Fail
    }
    
    producer.send(TOPIC, event)
    print(f"Dispatched Retail Event: {event}")
    time.sleep(random.uniform(0.5, 2.0)) # Continuous streaming