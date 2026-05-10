import time
import random
import math
import pandas as pd
from datetime import datetime
import os

sensor_val = random.uniform(500, 800)
drift = 0

def gerar_valor(t):
    global sensor_val, drift

    drift += random.uniform(-1.0, 1.0)

    regime = math.sin(t / 300)
    amplitude = 200 + 300 * abs(regime)

    ruido = random.gauss(0, 80)
    choque = random.uniform(-250, 250) if random.random() < 0.05 else 0
    onda = amplitude * math.sin(t / 15)

    novo = sensor_val + onda * 0.15 + ruido + choque + drift

    novo = max(200, min(1200, novo))
    sensor_val = novo

    return novo


while True:
    t = time.time()
    valor = gerar_valor(t)
    timestamp = datetime.now()

    linha = pd.DataFrame([{
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "co2": round(valor, 2)
    }])

    arquivo = "dados_tempo_real.csv"
    linha.to_csv(arquivo, mode="a", header=not os.path.exists(arquivo), index=False)

    print("CO2:", round(valor, 2))
    time.sleep(1)