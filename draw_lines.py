from kafka import KafkaConsumer
import tkinter as tk
import json, os, threading
from queue import Queue
from dotenv import load_dotenv

load_dotenv()

consumer = KafkaConsumer(
    os.getenv("TOPIC"),
    bootstrap_servers=os.getenv("SERVER"),
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="latest",
)

queue = Queue()

def consume():
    for message in consumer:
        queue.put(message.value)

threading.Thread(target=consume, daemon=True).start()

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

prev_x, prev_y = None, None

def draw():
    global prev_x, prev_y

    while not queue.empty():
        data = queue.get()
        x, y = data["x"], data["y"]

        if prev_x is not None:
            canvas.create_line(prev_x, prev_y, x, y, fill="black")

        prev_x, prev_y = x, y

    root.after(10, draw)

draw()
root.mainloop()