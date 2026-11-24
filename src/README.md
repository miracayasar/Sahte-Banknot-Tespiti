
# Kaynak Kodlar (Source Code)

Bu klasör, Sahte Banknot Tespiti projesinde kullanılan yeniden kullanılabilir Python modüllerini içermektedir.

## Mevcut Modüller

| Dosya | Açıklama |
|---|---|
| [preprocessing.py](preprocessing.py) | Veri temizleme, eğitim-test ayrımı, standardizasyon ve veri bütünlüğü kontrolleri |

## Veri Ön İşleme Modülünün Kullanımı

Google Colab çalışma ortamına `preprocessing.py` dosyasını ve orijinal UCI veri setinin ZIP arşivini yükleyin.

```python
from preprocessing import veri_hazirla

veriler = veri_hazirla("banknote+authentication.zip")
```

### Model Eğitiminde Kullanılacak Değişkenler

| Veri | Lojistik Regresyon | Karar Ağacı |
|---|---|---|
| Eğitim girdileri | `veriler["X_train_scaled"]` | `veriler["X_train"]` |
| Test girdileri | `veriler["X_test_scaled"]` | `veriler["X_test"]` |
| Eğitim etiketleri | `veriler["y_train"]` | `veriler["y_train"]` |
| Test etiketleri | `veriler["y_test"]` | `veriler["y_test"]` |

Modül, orijinal veri setiyle Google Colab ortamında başarıyla test edilmiştir.

## İlgili Dokümantasyon

- [Veri Ön İşleme Çalışması](../notebooks/02_veri_on_isleme/)
- [Veri Seti Açıklaması](../data/README.md)
- [Ana Proje Sayfası](../README.md)

