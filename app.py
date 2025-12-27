import streamlit as st
import pandas as pd
import json

st.title("🚀 Brand Monitor 2023")

# Nalaganje podatkov
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    st.success("Podatki so naloženi!")
    
    # Prikaz izdelkov
    st.header("Seznam izdelkov")
    st.table(data['products'])
    
    # Prikaz mnenj
    st.header("Mnenja strank")
    df = pd.DataFrame(data['reviews'])
    st.dataframe(df)

except Exception as e:
    st.error(f"Napaka pri branju data.json: {e}")