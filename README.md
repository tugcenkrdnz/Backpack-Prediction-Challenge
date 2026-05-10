# Kaggle S5E2 - 🎒 Sırt Çantası Fiyat Tahmin Sistemi 

Bu proje, Kaggle "Backpack Prediction Challenge" yarışması kapsamında geliştirilmiş, sırt çantası özelliklerine göre fiyat tahmini yapan bir makine öğrenmesi uygulamasıdır.

## 🎯 Proje Amacı
300.000 satırlık veri seti kullanılarak; malzeme, kapasite, marka ve bölme sayısı gibi özelliklerin fiyat üzerindeki etkisini analiz etmek ve en düşük RMSE (Hata Kareler Ortalamasının Karekökü) değerine ulaşmak hedeflenmiştir.

## 🛠️ Kullanılan Teknolojiler
- **Dil:** Python 3.11/3.13
- **Model:** CatBoost Regressor
- **Kütüphaneler:** Pandas, Numpy, Scikit-learn
- **Arayüz:** Streamlit
- **Teknikler:** Target Encoding, Feature Engineering (Interaction Features), Residual Analysis

## 📈 Model Performansı
- **En İyi Test Skoru (RMSE):** 38.89
- **Öne Çıkan Özellikler:** - Weight Capacity (kg) (~%23.7 önem)
    - Material-Size Etkileşimi
    - Marka ve Renk Bazlı Fiyat Ortalamaları (Target Encoding)

## 🚀 Uygulamayı Çalıştırma

1. **Gerekli Kütüphaneleri Yükleyin:**
   ```bash
   pip install -r requirements.txt

```

2. **Uygulamayı Başlatın:**
```bash
streamlit run app.py

```



## 📁 Dosya Yapısı

* `app.py`: Streamlit arayüz kodu.
* `catboost_backpack_model.cbm`: Eğitilmiş CatBoost model dosyası.
* `requirements.txt`: Gerekli bağımlılıklar listesi.
* `README.md`: Proje dökümantasyonu.