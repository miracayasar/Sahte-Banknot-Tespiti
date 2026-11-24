
# ⚙️ Veri Hazırlama ve Ön İşleme

**Marmara Üniversitesi | Yazılım Mühendisliği Temelleri**

| Bilgi | Açıklama |
|---|---|
| Proje | Sahte Banknot Tespiti |
| Hazırlayan | İbrahim Alo |
| Tarih | 24 Kasım 2026 |
| Çalışma ortamı | Google Colab |
| Proje görevi | [Issue #4 — Veri Hazırlama ve Ön İşleme](https://github.com/miracayasar/Sahte-Banknot-Tespiti/issues/4) |

---

## 🎯 1. Çalışmanın Amacı

Bu çalışmanın amacı, UCI Banknote Authentication veri setini Lojistik Regresyon (Logistic Regression) ve Karar Ağacı (Decision Tree) modellerinin eğitimine uygun hale getirmektir.

Her iki model için ortak eğitim ve test kümeleri oluşturularak adil, tutarlı ve tekrar üretilebilir bir performans karşılaştırması yapılması hedeflenmiştir.

## 📂 2. Kullanılan Veri Seti

| Özellik | Açıklama |
|---|---|
| Veri seti | UCI Banknote Authentication |
| Başlangıç kayıt sayısı | 1.372 |
| Sütun sayısı | 5 |
| Sayısal özellik sayısı | 4 |
| Hedef değişken | class |
| Lisans | CC BY 4.0 |

**Veri kaynağı:** [UCI Banknote Authentication](https://archive.ics.uci.edu/dataset/267/banknote)

**Ayrıntılı veri seti açıklaması:** [Veri Seti Dokümantasyonu](../../data/README.md)

## 🔧 3. Gerçekleştirilen İşlemler

- Veri setinin Google Colab ortamına yüklenmesi ve okunması.
- Eksik ve tekrarlanan kayıtların kontrol edilmesi.
- Tam satır tekrarlarının kaldırılması.
- Veri türlerinin doğrulanması.
- Özelliklerin (X) ve hedef değişkenin (y) ayrılması.
- Eğitim ve test kümelerinin oluşturulması.
- Lojistik Regresyon için standardizasyon uygulanması.
- Veri bütünlüğü ve ölçeklendirme kontrollerinin hazırlanması.

## 📊 4. Elde Edilen Sonuçlar

| Kontrol | Sonuç |
|---|---:|
| Başlangıç kayıt sayısı | 1.372 |
| Kaldırılan tekrarlı kayıt sayısı | 24 |
| Temizlenmiş kayıt sayısı | 1.348 |
| Eksik değer sayısı | 0 |
| Kalan tam satır tekrarı | 0 |
| Eğitim kayıtları | 1.078 |
| Test kayıtları | 270 |
| Ortak eğitim ve test indeksleri | 0 |

### Eğitim ve Test Ayrımı

| Parametre | Değer |
|---|---|
| Eğitim oranı | Yaklaşık %80 |
| Test oranı | Yaklaşık %20 |
| random_state | 42 |
| stratify | y |

random_state parametresi tekrar üretilebilirliği, stratify parametresi ise sınıf oranlarının eğitim ve test kümelerinde yaklaşık olarak korunmasını sağlamaktadır.

## 🛡️ 5. Veri Sızıntısının Önlenmesi

Tam satır tekrarları eğitim ve test ayrımından önce kaldırılmıştır.

StandardScaler yalnızca eğitim verisi üzerinde öğrenilmiş ve test verisine aynı dönüşüm uygulanmıştır.

Ölçeklendirilmiş eğitim verisinde dört özelliğin ortalaması yaklaşık 0, standart sapması ise 1 olarak doğrulanmıştır.

Notebook içerisinde sınıf etiketlerini, veri bütünlüğünü, ortak özellik vektörlerini ve veri kümelerinin uyumluluğunu denetleyen ek kontroller de bulunmaktadır.

## 🧠 6. Model Eğitiminde Kullanılacak Veriler

| Veri | Lojistik Regresyon | Karar Ağacı |
|---|---|---|
| Eğitim girdileri | `X_train_scaled` | `X_train` |
| Test girdileri | `X_test_scaled` | `X_test` |
| Eğitim etiketleri | `y_train` | `y_train` |
| Test etiketleri | `y_test` | `y_test` |

Lojistik Regresyon için ölçeklendirilmiş, Karar Ağacı için ise ölçeklendirilmemiş veriler hazırlanmıştır.

Her iki model aynı eğitim ve test kayıtlarını kullanacaktır.

## 🛠️ 7. Kullanılan Teknolojiler

| Teknoloji | Kullanım amacı |
|---|---|
| Python | Programlama |
| Pandas | Veri okuma ve temizleme |
| NumPy | Sayısal işlemler ve doğrulama |
| Scikit-learn | Eğitim-test ayrımı ve standardizasyon |
| Google Colab | Geliştirme ortamı |
| Jupyter Notebook | Teknik dokümantasyon |

## 💻 8. Çalıştırma Talimatları

1. UCI Banknote Authentication veri setini ZIP biçiminde indirin.
2. Veri ön işleme notebook'unu Google Colab üzerinde açın.
3. İlk kod hücresini çalıştırarak ZIP dosyasını yükleyin.
4. Tüm kod hücrelerini sırasıyla çalıştırın.
5. Son teknik kontrollerin başarılı olduğunu doğrulayın.


**Notebook dosyası:** [Veri Ön İşleme Çalışması](On_Isleme.ipynb)

**Ortak Python modülü:** [Preprocessing.py](../../src/Preprocessing.py)

**Modül kullanım talimatları:** [Kaynak Kodlar README](../../src/README.md)


Ayrı bir çalışma ortamında model eğitimi yapılacaksa ön işleme işlemleri aynı veri seti ve aynı parametrelerle yeniden gerçekleştirilmelidir.

## 📝 9. Genel Değerlendirme

Veri setindeki eksik değerler ve tekrarlanan kayıtlar kontrol edilmiş, 24 tam satır tekrarı kaldırılmış ve 1.348 kayıt üzerinden ortak eğitim-test kümeleri oluşturulmuştur.

Lojistik Regresyon modeli için gerekli standardizasyon işlemi gerçekleştirilirken Karar Ağacı için ölçeklendirilmemiş veriler korunmuştur.

Bu çalışma yalnızca veri hazırlama ve ön işleme aşamasını kapsamaktadır. Model eğitimi, tahmin işlemleri ve performans karşılaştırması sonraki proje aşamalarında gerçekleştirilecektir.

## 📚 10. Kaynakça ve Lisans

Lohweg, V. (2012). *Banknote Authentication* [Dataset]. UCI Machine Learning Repository.

- **DOI:** https://doi.org/10.24432/C55P57
- **Lisans:** [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Proje:** [Ana Proje Sayfası](../../README.md)

---

**Marmara Üniversitesi — Yazılım Mühendisliği Temelleri**

**Sahte Banknot Tespiti | 2026–2027 Güz Dönemi**

