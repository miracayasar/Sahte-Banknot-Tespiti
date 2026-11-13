# 💵 Sahte Banknot Tespiti

### Marmara Üniversitesi | Yazılım Mühendisliği Temelleri

**Dönem:** 2026–2027 Güz  
**Proje türü:** Makine Öğrenmesi ve Yazılım Mühendisliği  
**Ekip:** Miraç Yaşar • Buğra Ahat • İbrahim Alo  
**Durum:** Geliştirme aşamasında

---

## 📌 1. Proje Hakkında

Bu proje, banknotlara ait sayısal özellikler kullanılarak **gerçek ve sahte banknotların makine öğrenmesi yöntemleriyle sınıflandırılmasını** amaçlamaktadır.

Çalışmada **UCI Banknote Authentication** veri seti kullanılacak; **Lojistik Regresyon (Logistic Regression)** ve **Karar Ağacı (Decision Tree)** yöntemleri aynı veri seti üzerinde eğitilerek başarıları karşılaştırılacaktır.

Temel kapsam, iki sınıflandırma modelinin eğitilmesi, test edilmesi ve sonuçlarının karşılaştırılmasıdır. İsteğe bağlı geliştirmeler bu temel çalışmadan ayrı değerlendirilecektir.

---

## 🎯 2. Problem Tanımı ve Amaç

### Problem Tanımı

Banknotların gerçek veya sahte olarak sınıflandırılması, çeşitli makine öğrenmesi yöntemleriyle incelenebilen bir sınıflandırma problemidir.

Banknot görüntülerinden önceden çıkarılmış sayısal özellikler kullanılarak farklı algoritmaların sınıflandırma performansı araştırılacaktır.

### Projenin Temel Amacı

Aynı veri seti üzerinde iki makine öğrenmesi modelini:

1. Eğitmek,
2. Eğitimde kullanılmamış verilerle test etmek,
3. Performans ölçütlerini hesaplamak,
4. Sonuçlarını karşılaştırmak,
5. Bulguları bilimsel biçimde raporlamak.

### Araştırma Sorusu

> **Lojistik Regresyon ve Karar Ağacı yöntemleri, UCI Banknote Authentication veri setinde nasıl performans göstermektedir?**

### Hedef Kullanıcı

Temel çalışmanın hedef kullanıcıları, sınıflandırma yöntemlerinin performansını incelemek isteyen öğrenciler, araştırmacılar ve yazılım geliştiricilerdir.

---

## 🚀 3. Proje Kapsamı ve Öncelikler

Proje görevleri, önceliklerine göre **Must Have** ve **Should Have** olarak iki gruba ayrılmıştır.

### ✅ Must Have — Zorunlu Gereksinimler

Projenin tamamlanması için gerekli temel çalışmalar:

- En az üç akademik çalışmayı literatür taraması kapsamında karşılaştırmak ve yöntem seçimini gerekçelendirmek.
- UCI Banknote Authentication veri setine erişim sağlamak.
- Veri setinin kaynağını ve lisansını doğrulamak.
- Verileri Python ortamına yüklemek ve incelemek.
- Eksik ve tekrarlı verileri kontrol etmek.
- Gerekli veri ön işleme adımlarını gerçekleştirmek.
- Eğitim ve test verilerini ayırmak.
- Lojistik Regresyon modelini eğitmek.
- Karar Ağacı modelini eğitmek.
- Modellerin sınıflandırma başarılarını değerlendirmek.
- İki yöntemin sonuçlarını karşılaştırmak.
- Bulguları raporlamak ve GitHub üzerinde belgelemek.

**Bu bölüm dönem projesinin ana hedefidir.**

### ⭐ Should Have — İsteğe Bağlı Geliştirmeler

Temel proje tamamlandıktan sonra, zaman ve teknik olanaklar elverirse şu ek çalışmalar yapılabilir:

- Model performans sonuçlarını ve karşılaştırma grafiklerini daha anlaşılır biçimde sunmak.
- Sonuçların gösterimi için kapsamı ve teknolojisi ekip tarafından ayrıca netleştirilecek basit bir demo/arayüz hazırlamak.

Bu çalışmalar zorunlu değildir; henüz tamamlanmış özellikler olarak sunulmamaktadır.

### 🚫 Mevcut Kapsamın Dışında

- Banknot fotoğrafı yükleyerek sahte/gerçek tahmini yapmak (önceden düşünülen, sonradan kapsamdan çıkarılan fikir).
- Ham banknot görüntülerinden özellik çıkaran ayrı bir görüntü işleme modeli geliştirmek.
- Farklı para birimlerine ait fotoğrafları tanıyacak bir sistem geliştirmek.
- Web veya mobil uygulama geliştirmeyi zorunlu tutmak.
- Eğitim amaçlı sınıflandırma sonuçlarını gerçek hayatta kesin banknot doğrulaması olarak sunmak.

---

## 📂 4. Kullanılan Veri Seti

Projede **UCI Banknote Authentication** veri seti kullanılmaktadır. Veri seti, 1.372 banknot kaydına ait dört sayısal özellik ve bir sınıf etiketinden oluşmaktadır.

Bu veriler, Lojistik Regresyon ve Karar Ağacı modellerinin eğitilmesi ve karşılaştırılması amacıyla kullanılacaktır. Veri seti ham banknot fotoğrafları değil, görüntülerden önceden çıkarılmış sayısal özellikler içermektedir.

Dersin teslim kuralları gereği ham veri dosyası GitHub deposuna yüklenmemektedir. Çalıştırmak için veri seti [resmî UCI kaynağından](https://archive.ics.uci.edu/dataset/267/banknote) temin edilip çalışma ortamına yüklenir.

**Veri setinin özellikleri, değişkenleri, kaynağı ve lisans bilgileri:** [Veri Seti Dokümantasyonu](data/README.md)

---

## 🧠 5. Seçilen Makine Öğrenmesi Yöntemleri

### 📚 Literatür Taraması ve Yöntem Seçimi

Sahte banknot tespitinde kullanılacak makine öğrenmesi yöntemlerini belirlemek amacıyla, UCI Banknote Authentication veri seti üzerinde gerçekleştirilen akademik çalışmalar incelenmiştir.

#### Literatür Karşılaştırması

| Araştırma | Problem ve Veri | Yöntem ve Doğruluk (Accuracy) | Sınırlılık |
|---|---|---|---|
| Rashid (2020) [1] | Banknotların gerçek/sahte olarak sınıflandırılması; Banknote Authentication veri seti | Lojistik Regresyon: **%98,79**, Karar Ağacı: **%98,05**, Random Forest: **%99,30** | Erişilebilir kongre özetinde deney ayarları ayrıntılı açıklanmamıştır. |
| Khairy ve arkadaşları (2021) [2] | Sahte banknot tespiti; UCI Banknote Authentication veri seti | Lojistik Regresyon: **%99,10**, k-NN: **%99,90**, Random Forest: **%99,30** | Sonuçlar 10 katlı çapraz doğrulama yöntemiyle elde edilmiştir. |
| Eşidir ve arkadaşları (2025) [3] | Banknot sahteciliğinin tespiti; UCI Banknote Authentication veri seti | Lojistik Regresyon: **%99,30**, Random Forest: **%99,60**, XGBoost: **%99,60** | Çalışma belirli bir veri seti ve üç algoritmayla sınırlandırılmıştır. |

*Tablodaki oranlar ilgili araştırmaların kendi deney sonuçlarıdır.*

#### Yöntem Seçiminin Gerekçesi

Literatür taramasında farklı makine öğrenmesi algoritmalarının banknot sınıflandırmasında yüksek başarı elde ettiği görülmüştür. Özellikle Lojistik Regresyon ve Karar Ağacı yöntemlerinin de yüksek doğruluk oranlarına ulaşabildiği belirlenmiştir.

Bu bulgular doğrultusunda, farklı sınıflandırma yaklaşımlarını temsil eden **Lojistik Regresyon (Logistic Regression)** ve **Karar Ağacı (Decision Tree)** algoritmaları tercih edilmiştir.

Proje kapsamında iki modelin aynı eğitim ve test verileriyle karşılaştırılması hedeflenmektedir. Literatürdeki bulgulara dayanarak her iki modelin de **%95'in üzerinde doğruluk** elde edebileceği hipotezi test edilecektir.

## 📊 6. Haftalık Çalışmalar ve İlerleme

### 📂 Gerçekleştirilen Çalışmalar

Proje kapsamında tamamlanan çalışmalar, ilgili dosyalar ve belgelerle birlikte GitHub deposunda düzenli olarak saklanmaktadır.

| Çalışma | Kapsam | Dosyalar |
|---|---|---|
| **5. Hafta — UML ve Tasarım** | Use Case, Activity ve Class diyagramlarının hazırlanması; sistemin yapısının ve işleyişinin modellenmesi. | [UML Diyagramları](docs/uml/) · [5. Hafta UML Raporu](docs/haftalik_raporlar/5.%20hafta%20UML%20proje%20raporu.pdf) |
| **6. Hafta — Veri Analizi** | UCI Banknote Authentication veri setinin Google Colab ortamında incelenmesi, temel istatistiklerin hesaplanması ve grafiklerle görselleştirilmesi. | [Google Colab Çalışması](notebooks/Hafta6_Ogrenci_Proje_Veri_Analizi_Sablonu.ipynb) · [6. Hafta Açıklamaları](notebooks/README.md) |

---

## 🛠️ 7. Kullanılan Teknolojiler ve Araçlar

| Teknoloji / Araç | Kullanım Amacı |
|---|---|
| **Python** | Veri analizi ve model geliştirme |
| **Google Colab** | Bulut tabanlı Python çalışma ortamı |
| **Matplotlib** | Grafik ve görselleştirme |
| **Scikit-learn** | Makine öğrenmesi modellerinin eğitimi ve değerlendirilmesi |
| **Git ve GitHub** | Sürüm kontrolü ve ekip çalışması |
| **draw.io / diagrams.net** | UML diyagramlarının hazırlanması |

İsteğe bağlı arayüzün kullanılacak teknolojisi, geliştirme aşamasında belirlenecektir.

---

## 👥 8. Proje Ekibi ve Görev Dağılımı

Proje, üç kişilik ekip tarafından yürütülmektedir. Görevler; model geliştirme, yazılım geliştirme, proje yönetimi ve dokümantasyon alanlarında paylaştırılmıştır.

### 📋 Genel Görev Dağılımı

| Ekip Üyesi | Görev ve Sorumluluklar |
|---|---|
| **Miraç Yaşar** | GitHub deposunun genel yönetimi, dosya ve sürüm organizasyonu, isteğe bağlı arayüz çalışmasının değerlendirilmesi ve sunumların hazırlanması ve gerçekleştirilmesi. |
| **İbrahim Alo** | Veri analizi, Lojistik Regresyon ve Karar Ağacı modellerinin geliştirilmesi ve test edilmesi, sunumların hazırlanması ve gerçekleştirilmesi. |
| **Buğra Ahat** | Projenin tüm raporlama ve dokümantasyon süreçlerinin yürütülmesi, teknik çalışmaların belgelenmesi, haftalık raporların hazırlanması ve proje sonuçlarının raporlanması. |

---

## 📚 9. Kaynakça ve Lisans

### Literatür Taramasında Kullanılan Akademik Kaynaklar

**[1]** Rashid, H.-U. (2020). *Performance Analysis of Different Machine Learning Techniques on Banknote Authentication.* 4. Çukurova Uluslararası Bilimsel Araştırmalar Kongresi, Kongre Özet Kitabı, s. 143.  
Bağlantı: https://apbseski.mersin.edu.tr/files/fahriozsungur/Scientific_Meetings_017.pdf

**[2]** Khairy, R. S., Hussein, A. S., & AlRikabi, H. T. S. (2021). *The Detection of Counterfeit Banknotes Using Ensemble Learning Techniques of AdaBoost and Voting.* International Journal of Intelligent Engineering and Systems, 14(1), 326–339.  
DOI: https://doi.org/10.22266/IJIES2021.0228.31

**[3]** Eşidir, O. V., Bak, G., & Karadağ, B. (2025). *Finansal ve Medyatik Sahteciliğe Karşı Yapay Zekâ Çözümleri: Banknot Sahteciliği Tespitinde Makine Öğrenmesi Uygulamaları.* Akademik Araştırmalar ve Çalışmalar Dergisi, 17(33), 1066–1076.  
Makale: https://dergipark.org.tr/tr/pub/kilisiibfakademik/article/1740385

### Veri Seti Atfı ve Lisans

**Veri seti atfı:**

Lohweg, V. (2012). *Banknote Authentication* [Dataset]. UCI Machine Learning Repository.

https://doi.org/10.24432/C55P57

**Veri seti lisansı:**

Creative Commons Attribution 4.0 International (CC BY 4.0)

https://creativecommons.org/licenses/by/4.0/

Veri seti kullanılırken kaynak ve lisans bilgileri korunacaktır. Veri değiştirilerek paylaşılırsa yapılan değişiklikler de belirtilecektir. Ham veri dosyası GitHub deposunda tutulmamaktadır.

---

**Marmara Üniversitesi — Yazılım Mühendisliği Temelleri | 2026–2027 Güz Dönemi**

*Proje geliştirme süreci devam etmektedir.*
