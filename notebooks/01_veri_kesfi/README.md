# 📊 6. Hafta — Banknot Veri Analizi

**Marmara Üniversitesi | Yazılım Mühendisliği Temelleri**

| Bilgi | Açıklama |
|---|---|
| Proje | Sahte Banknot Tespiti |
| Dönem | 2026–2027 Güz |
| Çalışma ortamı | Google Colab / Jupyter Notebook |
| Analiz tarihi | 4 Kasım 2026 |

## 🎯 1. Çalışmanın Amacı

Bu çalışma, **UCI Banknote Authentication** veri setini Python ile incelemek ve temel betimsel istatistikleri hesaplamak amacıyla hazırlanmıştır.

Çalışma kapsamında:

- Veri setindeki **1.372 kayıt** incelenmiştir.
- Sayısal özelliklerin toplam, ortalama, minimum ve maksimum değerleri hesaplanmıştır.
- Sınıf dağılımı analiz edilmiştir.
- **İki sütun grafiği ve bir çizgi grafiği** oluşturulmuştur.
- Elde edilen sonuçlar yorumlanmıştır.

> **Kapsam:** Bu çalışma, dönem projesinin veri analizi aşamasıdır. Henüz makine öğrenmesi modellerinin eğitimi veya başarı değerlendirmesi yapılmamıştır.

## 📂 2. Kullanılan Veri Seti

| Bilgi | Açıklama |
|---|---|
| Veri seti | Banknote Authentication |
| Kaynak | UCI Machine Learning Repository |
| Kayıt sayısı | 1.372 |
| Sütun sayısı | 5 |
| Sayısal özellik sayısı | 4 |
| Hedef değişken | `class` |
| Eksik değer sayısı | 0 |
| Veri seti lisansı | CC BY 4.0 |

- **Resmî kaynak:** [UCI Banknote Authentication](https://archive.ics.uci.edu/dataset/267/banknote)
- **DOI:** [10.24432/C55P57](https://doi.org/10.24432/C55P57)

### Veri Setindeki Değişkenler

| Değişken | Açıklama |
|---|---|
| `variance` | Dalgacık dönüşümlü görüntünün varyansı |
| `skewness` | Dalgacık dönüşümlü görüntünün çarpıklığı |
| `curtosis` | Dalgacık dönüşümlü görüntünün basıklığı |
| `entropy` | Görüntünün entropisi |
| `class` | Sınıf etiketi (0 veya 1) |

Veri seti, banknotların fiziksel uzunluk veya ağırlık ölçümlerini değil, görüntülerden elde edilmiş sayısal özellikleri içermektedir.

## 📈 3. İstatistiksel Analiz Sonuçları

Veri setindeki **1.372 kaydın tamamı** üzerinden hesaplanan değerler aşağıda sunulmuştur.

| Özellik | Toplam | Ortalama | Minimum | Maksimum |
|---|---:|---:|---:|---:|
| `variance` | 595,0848 | 0,4337 | -7,0421 | 6,8248 |
| `skewness` | 2.637,4685 | 1,9224 | -13,7731 | 12,9516 |
| `curtosis` | 1.917,5444 | 1,3976 | -5,2861 | 17,9274 |
| `entropy` | -1.634,9527 | -1,1917 | -8,5482 | 2,4495 |

### Sınıf Dağılımı

| Sınıf | Kayıt sayısı | Oran |
|---|---:|---:|
| Sınıf 0 | 762 | %55,54 |
| Sınıf 1 | 610 | %44,46 |
| **Toplam** | **1.372** | **%100** |

## 📉 4. Oluşturulan Grafikler

### Grafik 1 — Banknot Sınıf Dağılımı

`class` sütunundaki 0 ve 1 etiketlerinin kayıt sayıları sütun grafiğiyle karşılaştırılmıştır.

### Grafik 2 — Sayısal Özelliklerin Ortalamaları

`variance`, `skewness`, `curtosis` ve `entropy` değişkenlerinin ortalama değerleri sütun grafiğiyle gösterilmiştir.

### Grafik 3 — Variance Değerleri

1.372 kaydın tamamına ait `variance` değerleri çizgi grafiğiyle görselleştirilmiştir.

> **Yorumlama notu:** Çizgi grafiğindeki yatay eksen kayıt sırasını göstermektedir. Grafik, zaman serisi veya zamana bağlı bir değişim olarak yorumlanmamalıdır.

Grafikler, çalıştırılmış Jupyter Notebook dosyasında görüntülenebilir.

## 💻 5. Kullanılan Teknolojiler

| Teknoloji | Kullanım amacı |
|---|---|
| Python | Veri işleme ve hesaplama |
| Google Colab | Bulut tabanlı çalışma ortamı |
| Jupyter Notebook | Kod, açıklama ve çıktıları belgeleme |
| Pandas | Veri analizi ve istatistiksel hesaplamalar |
| Matplotlib | Grafik oluşturma |
| GitHub | Dosya yönetimi ve ekip çalışması |

## 👥 6. Ekip Üyeleri ve Görev Dağılımı

| Ekip üyesi | Görev ve sorumluluk |
|---|---|
| **İbrahim Alo** | Google Colab uygulaması, istatistiksel hesaplamalar ve grafiklerin hazırlanması |
| **Miraç Yaşar** | GitHub depo yönetimi, dosya organizasyonu ve proje tesliminin koordinasyonu |
| **Buğra Ahat** | Veri kaynağı ve lisans doğrulaması, analiz sonuçlarının kontrolü ve akademik yorumun gözden geçirilmesi |

Görev dağılımı, ekip çalışmasının izlenebilirliği amacıyla belirtilmiştir. Atanan kontrol görevleri tamamlandığında sonuçlar ekip tarafından doğrulanmalıdır.

## 📝 7. Genel Değerlendirme

UCI Banknote Authentication veri setinin tamamı incelenerek temel betimsel istatistikler hesaplanmış ve grafiklerle görselleştirilmiştir.

Veri setinde eksik değer bulunmadığı belirlenmiştir. Dört sayısal özelliğin istatistiksel değerleri ve iki sınıfın dağılımı raporlanmıştır.

Bu analiz, ilerleyen aşamalarda uygulanması planlanan **Lojistik Regresyon** ve **Karar Ağacı** yöntemleri öncesinde veri setinin tanınmasını sağlamaktadır.

## 📚 8. Kaynakça ve Lisans

Lohweg, V. (2012). *Banknote Authentication* [Dataset]. UCI Machine Learning Repository.  
[https://doi.org/10.24432/C55P57](https://doi.org/10.24432/C55P57)

Veri seti, **Creative Commons Attribution 4.0 International (CC BY 4.0)** lisansıyla sunulmaktadır.

[Lisans metni](https://creativecommons.org/licenses/by/4.0/)

---

**Marmara Üniversitesi — Yazılım Mühendisliği Temelleri | 6. Hafta Çalışması**

