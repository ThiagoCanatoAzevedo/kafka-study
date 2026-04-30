from pynput.mouse import Controller
from kafka import KafkaProducer
from dotenv import load_dotenv
import time, json, os

load_dotenv()

producer = KafkaProducer(
    bootstrap_servers=os.getenv("SERVER"),
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    linger_ms=0,      
    batch_size=16384  
)

mouse = Controller()

prev = None

while True:
    x, y = mouse.position

    if (x, y) != prev:
        producer.send(os.getenv("TOPIC"), value={"x": x, "y": y})
        prev = (x, y)

    time.sleep(0.01) 