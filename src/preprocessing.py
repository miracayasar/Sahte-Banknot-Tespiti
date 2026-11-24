# -*- coding: utf-8 -*-
"""Sahte Banknot Tespiti | Ortak veri hazırlama modülü.

Kaynak çalışma: Veri_On_Isleme.ipynb (İbrahim Alo, 24 Kasım 2026).
Veri: UCI Banknote Authentication, DOI: 10.24432/C55P57, CC BY 4.0.
Model eğitimi içermez. Orijinal ZIP arşivini yerel olarak kullanır.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


OZELLIKLER = ["variance", "skewness", "curtosis", "entropy"]
SUTUNLAR = OZELLIKLER + ["class"]


def veri_hazirla(dosya_adi):
    """UCI ZIP dosyasını okuyup iki model için ortak verileri döndürür.

    Lojistik Regresyon: X_train_scaled, X_test_scaled.
    Karar Ağacı: X_train, X_test.
    Ortak etiketler: y_train, y_test.
    scaler: yeni girdilere eğitimden öğrenilen dönüşümü uygulamak için.
    """
    # 1. Veri okuma ve temizleme
    veri = pd.read_csv(dosya_adi, compression="zip", header=None)
    if veri.shape[1] != len(SUTUNLAR):
        raise ValueError("Veri seti tam olarak beş sütun içermelidir.")
    veri.columns = SUTUNLAR
    if veri.isna().any().any():
        raise ValueError("Veri setinde eksik değer bulundu.")
    if not all(pd.api.types.is_numeric_dtype(veri[s]) for s in SUTUNLAR):
        raise ValueError("Tüm sütunlar sayısal olmalıdır.")
    temiz_veri = veri.drop_duplicates()

    # 2. Özellikler ve hedef değişken
    X = temiz_veri[OZELLIKLER]
    y = temiz_veri["class"]
    if set(y.unique()) != {0, 1}:
        raise ValueError("Sınıf etiketleri 0 ve 1 olmalıdır.")
    if not np.isfinite(X.to_numpy()).all():
        raise ValueError("Sonlu olmayan özellik değeri bulundu.")

    # 3. Ortak eğitim-test ayrımı (notebook ile aynı parametreler)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # 4. Standardizasyon: yalnızca eğitim verisinden öğrenilir.
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 5. Notebook'taki bütünlük kontrolleri
    if not (X_train.index.equals(y_train.index)
            and X_test.index.equals(y_test.index)
            and X_train.index.intersection(X_test.index).empty
            and len(X_train) + len(X_test) == len(temiz_veri)):
        raise ValueError("Eğitim-test ayrımı veya etiket eşleşmesi hatalı.")

    ortak_ozellikler = X_train.drop_duplicates().merge(
        X_test.drop_duplicates(), on=OZELLIKLER, how="inner"
    )
    if not ortak_ozellikler.empty:
        raise ValueError("Aynı özellik vektörü eğitim ve testte bulunuyor.")

    if not (X_train_scaled.shape == X_train.shape
            and X_test_scaled.shape == X_test.shape
            and np.isfinite(X_train_scaled).all()
            and np.isfinite(X_test_scaled).all()
            and np.allclose(X_train_scaled.mean(axis=0), 0)
            and np.allclose(X_train_scaled.std(axis=0), 1)
            and np.allclose(X_test_scaled, scaler.transform(X_test))):
        raise ValueError("Standardizasyon kontrolleri başarısız.")

    # Her iki model için verileri tek bir sözlükte döndür.
    return {
        "X_train": X_train,
        "X_test": X_test,
        "X_train_scaled": X_train_scaled,
        "X_test_scaled": X_test_scaled,
        "y_train": y_train,
        "y_test": y_test,
        "scaler": scaler,
        "temiz_veri": temiz_veri,
    }
