import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CO₂ IoT Dashboard")

st.title("📊 Sistema IoT de Emissões CO₂")

arquivo = "dados_tempo_real.csv"

# -------------------------
# CARREGAR DADOS
# -------------------------
if os.path.exists(arquivo):

    df = pd.read_csv(arquivo)

    # converter timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # -------------------------
    # MÉTRICAS
    # -------------------------
    st.metric("🌫️ CO₂ atual (ppm)", df["co2"].iloc[-1])

    # -------------------------
    # TEMPO REAL
    # -------------------------
    st.subheader("📈 Sensor em Tempo Real")
    st.line_chart(df.set_index("timestamp")["co2"])

    # -------------------------
    # MINUTOS
    # -------------------------
    df_min = df.set_index("timestamp").resample("1min").mean(numeric_only=True).dropna()

    st.subheader("📊 Média por Minuto")
    st.line_chart(df_min)

    # -------------------------
    # HORAS
    # -------------------------
    df_hora = df.set_index("timestamp").resample("1H").mean(numeric_only=True).dropna()

    st.subheader("⏳ Média por Hora")
    st.line_chart(df_hora)

    # -------------------------
    # DIAS
    # -------------------------
    df_dia = df.set_index("timestamp").resample("1D").mean(numeric_only=True).dropna()

    st.subheader("📅 Média por Dia")
    st.line_chart(df_dia)

    # -------------------------
    # DOWNLOAD
    # -------------------------
    st.subheader("⬇️ Download dos Dados")

    st.download_button(
        "📥 Baixar CSV completo",
        df.to_csv(index=False),
        file_name="dados_tempo_real.csv"
    )

else:
    st.warning("Aguardando dados do backend...")