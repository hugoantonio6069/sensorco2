import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Dashboard CO₂")

conn = sqlite3.connect("sensor.db")

df = pd.read_sql("SELECT * FROM dados", conn)

st.metric("Último valor CO₂", df["co2"].iloc[-1])

st.subheader("Histórico")
st.line_chart(df.set_index("timestamp")["co2"])