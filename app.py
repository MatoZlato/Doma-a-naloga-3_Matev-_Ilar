import streamlit as st
import pandas as pd
import json
from transformers import pipeline

st.set_page_config(page_title="Brand Monitor 2023", layout="wide")

# Naložimo model za sentiment (Hugging Face)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentiment_model = load_model()

# Nalaganje podatkov
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# --- SIDEBAR NAVIGACIJA ---
st.sidebar.title("Navigacija")
izbira = st.sidebar.radio("Izberi sekcijo:", ["Products", "Testimonials", "Reviews"])

if izbira == "Products":
    st.title("📦 Seznam izdelkov")
    st.table(data['products'])

elif izbira == "Testimonials":
    st.title("💬 Pričevanja strank")
    for t in data['testimonials']:
        st.info(t)

elif izbira == "Reviews":
    st.title("📊 Analiza mnenj 2023")
    
    df = pd.DataFrame(data['reviews'])
    
    # Slider za izbiro meseca
    meseci = ["Jan 2023", "Feb 2023", "Mar 2023"] # Dodaj več, če jih imaš v data.json
    izbran_mesec = st.select_slider("Izberi mesec v letu 2023:", options=meseci)
    
    # Filtriranje
    filtered_df = df[df['month_year'] == izbran_mesec].copy()
    
    if not filtered_df.empty:
        # AI Analiza
        results = sentiment_model(filtered_df['text'].tolist())
        filtered_df['Sentiment'] = [r['label'] for r in results]
        filtered_df['Confidence'] = [round(r['score'], 2) for r in results]
        
        st.write(filtered_df)
        
        # Grafikon
        st.subheader(f"Statistika za {izbran_mesec}")
        sentiment_counts = filtered_df['Sentiment'].value_counts()
        st.bar_chart(sentiment_counts)
        
        avg_conf = filtered_df['Confidence'].mean()
        st.metric("Povprečno zaupanje modela (Confidence)", f"{avg_conf*100:.1f}%")
    else:
        st.warning("Ni podatkov za ta mesec.")
