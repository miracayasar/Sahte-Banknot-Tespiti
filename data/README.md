# 📂 Veri Seti — Banknote Authentication



## 📄 Veri Seti Bilgileri

| Özellik | Bilgi |
|---|---|
| Veri dosyası | `data_banknote_authentication.txt` |
| Kayıt sayısı | 1.372 |
| Toplam sütun sayısı | 5 |
| Sayısal özellik sayısı | 4 |
| Hedef değişken | `class` |
| Eksik değer sayısı | **0** |
| Tekrarlanan satır sayısı | 24 |
| Sınıflandırma türü | İkili sınıflandırma |

## 📊 Veri Setindeki Değişkenler

| Değişken | Açıklama | Veri türü |
|---|---|---|
| `variance` | Dalgacık dönüşümlü görüntünün varyansı | Continuous |
| `skewness` | Dalgacık dönüşümlü görüntünün çarpıklığı | Continuous |
| `curtosis` | Dalgacık dönüşümlü görüntünün basıklığı | Continuous |
| `entropy` | Görüntünün entropisi | Continuous |
| `class` | Sınıf etiketi (0 veya 1) | Integer |

## 🔍 Veri Yapısı ve Kalitesi

- Veri seti 1.372 satır ve 5 sütundan oluşmaktadır.
- **Hiçbir sütunda eksik değer bulunmamaktadır.**
- Dosyada sütun başlıkları yoktur ve değerler virgülle ayrılmıştır.
- Sınıf dağılımı: `0` sınıfında 762, `1` sınıfında 610 kayıt bulunmaktadır.
- İlk incelemede tespit edilen 24 tekrarlanan satır, veri ön işleme aşamasında kaldırılmıştır.
- Ham veri seti 1.372, temizlenmiş veri seti ise 1.348 kayıttan oluşmaktadır.
- [Veri Ön İşleme Çalışması](../notebooks/02_veri_on_isleme/README.md)


## 🎯 Projede Kullanım Amacı

Veri seti, **Lojistik Regresyon** ve **Karar Ağacı** modellerinin eğitilmesi, test edilmesi ve performanslarının karşılaştırılması amacıyla kullanılacaktır.

## 🔗 Kaynak ve Lisans

- **Kaynak:** UCI Machine Learning Repository
- **Hazırlayan:** Volker Lohweg (2012)
- **Resmî bağlantı:** https://archive.ics.uci.edu/dataset/267/banknote
- **DOI:** https://doi.org/10.24432/C55P57
- **Lisans:** Creative Commons Attribution 4.0 International (CC BY 4.0)


