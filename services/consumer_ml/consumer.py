import os
import json
import pickle
import time
import psycopg2
from kafka import KafkaConsumer

BROKER = os.getenv("KAFKA_BROKER", "localhost:19092")
DB_URL = os.getenv("DATABASE_URL", "postgresql://retail_admin:retail_secure_pass@localhost:5432/omnistream_db")

with open("iso_forest.pkl", "rb") as f:
    model = pickle.load(f)

# Connect to Database
time.sleep(5) # Let DB stabilize
conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()

consumer = KafkaConsumer(
    "retail-operations",
    bootstrap_servers=[BROKER],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Streaming ETL Consumer Engine running...")
for message in consumer:
    data = message.value
    
    # Feature Engineering for Inference Engine
    is_51 = 1 if data["idoc_status"] == "51" else 0
    features = [[data["quantity"], data["amount"], is_51]]
    
    # Run Scikit-Learn Inference
    # Isolation forest outputs -1 for anomalies, 1 for normal data
    prediction = model.predict(features)[0]
    is_anomaly = 1 if prediction == -1 else 0
    
    # Business Logic rule engine for Stockout Risks
    stockout_risk = 1 if data["quantity"] > 50 else 0

    # Persist directly to DB for real-time Dashboard access
    cursor.execute(
        """INSERT INTO retail_events (store_id, material_id, quantity, amount, idoc_status, is_anomaly, stockout_risk) 
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (data["store_id"], data["material_id"], data["quantity"], data["amount"], data["idoc_status"], is_anomaly, stockout_risk)
    )
    conn.commit()
    print(f"Processed & Logged. Anomaly Flag: {is_anomaly} | Stockout Risk: {stockout_risk}")