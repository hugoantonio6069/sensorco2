import time
import random
import math
import sqlite3
from datetime import datetime

conn = sqlite3.connect("sensor.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS dados (
    timestamp TEXT,
    co2 REAL
)
""")

conn.commit()

sensor_val = random.uniform(500, 800)
drift = 0

def gerar_valor(t):
    global sensor_val, drift

    drift += random.uniform(-1, 1)

    regime = math.sin(t / 300)
    amplitude = 200 + 300 * abs(regime)

    ruido = random.gauss(0, 80)
    choque = random.uniform(-250, 250) if random.random() < 0.05 else 0
    onda = amplitude * math.sin(t / 15)

    novo = sensor_val + onda * 0.15 + ruido + choque + drift

    novo = max(200, min(1200, novo))

    sensor_val = novo
    return novo

t = 0

while True:
    valor = gerar_valor(t)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    c.execute("INSERT INTO dados VALUES (?, ?)", (timestamp, valor))
    conn.commit()

    print(timestamp, valor)

    t += 1
    time.sleep(1)