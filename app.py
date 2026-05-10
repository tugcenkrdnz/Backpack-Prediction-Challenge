import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor

# 1. Sayfa Ayarları
st.set_page_config(page_title="Çanta Fiyat Tahmini", page_icon="🎒", layout="centered")

@st.cache_resource
def load_model():
    model = CatBoostRegressor()
    model.load_model("catboost_backpack_model.cbm")
    return model

model = load_model()

# 2. Gerçek Target Encoding Verilerin (Senin paylaştığın sözlükler)
brand_means = {'Adidas': 80.63, 'Jansport': 81.79, 'Nike': 81.32, 'Puma': 81.45, 'Under Armour': 81.98, 'Unknown': 80.87}
style_means = {'Backpack': 81.40, 'Messenger': 81.41, 'Tote': 81.37, 'Unknown': 81.96}
color_means = {'Black': 80.51, 'Blue': 82.01, 'Gray': 80.85, 'Green': 82.38, 'Pink': 81.63, 'Red': 81.01, 'Unknown': 81.77}
material_size_means = {'Canvas_Large': 82.41, 'Canvas_Medium': 81.87, 'Canvas_Small': 82.28, 'Leather_Large': 80.88, 'Leather_Medium': 80.24, 'Leather_Small': 80.53, 'Nylon_Large': 81.09, 'Nylon_Medium': 81.02, 'Nylon_Small': 81.01, 'Polyester_Large': 82.14, 'Polyester_Medium': 82.23, 'Polyester_Small': 81.81}

# 3. Arayüz Tasarımı
st.title("🎒 Akıllı Sırt Çantası Fiyatlama")
st.info("Kaggle S5E2 Yarışması için geliştirilen CatBoost modelidir.")

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox("Marka", list(brand_means.keys()))
    material = st.selectbox("Malzeme", ["Canvas", "Leather", "Nylon", "Polyester"])
    size = st.selectbox("Boyut", ["Small", "Medium", "Large"])
    color = st.selectbox("Renk", list(color_means.keys()))
    compartments = st.number_input("Bölme Sayısı", 1, 15, 3)

with col2:
    style = st.selectbox("Stil", list(style_means.keys()))
    laptop = st.radio("Laptop Bölmesi", ["Yes", "No"])
    waterproof = st.radio("Su Geçirmezlik", ["Yes", "No"])
    weight_cap = st.slider("Taşıma Kapasitesi (kg)", 5, 50, 15)

# 4. Tahmin Motoru
if st.button("Fiyatı Hesapla"):
    # Girdi DataFrame'i
    input_df = pd.DataFrame({
        'Brand': [brand],
        'Material': [material],
        'Size': [size],
        'Compartments': [float(compartments)],
        'Laptop Compartment': [laptop],
        'Waterproof': [waterproof],
        'Style': [style],
        'Color': [color],
        'Weight Capacity (kg)': [float(weight_cap)]
    })

    # Özellik Mühendisliği (Interaction Features)
    ms_key = f"{material}_{size}"
    input_df['Material_Waterproof'] = material + "_" + waterproof
    input_df['Material_Size'] = ms_key
    
    # Target Encoding Atamaları (Dinamik)
    input_df['Brand_Target_Avg'] = brand_means.get(brand, 81.0)
    input_df['Color_Target_Avg'] = color_means.get(color, 81.0)
    input_df['Style_Target_Avg'] = style_means.get(style, 81.0)
    input_df['Material_Size_Target_Avg'] = material_size_means.get(ms_key, 81.0)

    # Tahmin
    prediction = model.predict(input_df)[0]
    
    # Görsel Sonuç
    st.markdown("---")
    st.success(f"### Tahmini Satış Fiyatı: {prediction:.2f} TL")