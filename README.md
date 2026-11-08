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

Proje, temel sınıflandırma çalışmasının yanında, zaman ve teknik olanaklar elverdiğinde kullanıcıların banknot görüntüsü yükleyebileceği bir arayüz geliştirilmesini de isteğe bağlı hedef olarak içermektedir.



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

İsteğe bağlı arayüz geliştirilirse görsel banknot analiziyle ilgilenen kullanıcılar da hedef kitleye dâhil edilebilir.

---

## 🚀 3. Proje Kapsamı ve Öncelikler

Proje görevleri, önceliklerine göre **Must Have** ve **Should Have** olarak iki gruba ayrılmıştır.

### ✅ Must Have — Zorunlu Gereksinimler

Projenin tamamlanması için gerekli temel çalışmalar:

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

Temel proje tamamlandıktan sonra, yeterli zaman ve uygun veri bulunması durumunda aşağıdaki özelliklerin geliştirilmesi hedeflenmektedir:

- Kullanıcıların banknot fotoğrafı yükleyebileceği bir arayüz.
- Görüntüler üzerinden banknot analizi yapabilen ayrı bir makine öğrenmesi modeli.
- İlk aşamada **ABD doları** için görüntü analizi desteği.
- Analiz sonucunun kullanıcıya anlaşılır biçimde gösterilmesi.
- İlerleyen sürümlerde **Türk lirası** desteği.
- Uygun görülürse PDF veya belge üzerinden görüntü alma desteği.


Should Have kapsamındaki özellikler şu anda **planlama ve araştırma aşamasındadır**; uygulanmaları garanti edilmemektedir.

### 🚫 Mevcut Zorunlu Kapsamın Dışında

- Zorunlu olarak web veya mobil uygulama geliştirmek.
- Mevcut UCI veri setinden doğrudan fotoğraf tanıma sistemi oluşturmak.
- Ham görüntülerden özellik çıkaran bir sistem geliştirmek.
- Derin öğrenme modeli geliştirmeyi zorunlu tutmak.
- Eğitim amaçlı tahminleri gerçek hayatta kesin banknot doğrulaması olarak sunmak.

---

## 📂 4. Kullanılan Veri Seti

| Özellik | Bilgi |
|---|---|
| **Adı** | Banknote Authentication |
| **Kaynak** | UCI Machine Learning Repository |
| **Hazırlayan** | Volker Lohweg (2012) |
| **Kayıt sayısı** | 1.372 |
| **Sayısal özellik sayısı** | 4 |
| **Hedef değişken** | 1 |
| **Toplam sütun sayısı** | 5 |
| **Eksik değer** | 0 |
| **Lisans** | CC BY 4.0 |

**Resmî veri seti:** https://archive.ics.uci.edu/dataset/267/banknote

**DOI:** https://doi.org/10.24432/C55P57

### Veri Setindeki Değişkenler

| Değişken | Açıklama | Tür |
|---|---|---|
| `variance` | Dalgacık dönüşümlü görüntünün varyansı | Continuous |
| `skewness` | Dalgacık dönüşümlü görüntünün çarpıklığı | Continuous |
| `curtosis` | Dalgacık dönüşümlü görüntünün basıklığı | Continuous |
| `entropy` | Görüntünün entropisi | Continuous |
| `class` | Gerçek/sahte sınıf etiketi | Integer |

Veri seti **ham banknot fotoğraflarını değil**, görüntü işleme sonucunda önceden elde edilmiş sayısal özellikleri içermektedir.

Bu nedenle veri seti temel sınıflandırma çalışmasında kullanılacak, isteğe bağlı görüntü analizi çalışması ise ayrı değerlendirilecektir.

**Depodaki veri dosyası:** [data_banknote_authentication.txt](data/data_banknote_authentication.txt)

---

## 🧠 5. Seçilen Makine Öğrenmesi Yöntemleri

### Lojistik Regresyon

İki sınıflı sınıflandırma problemlerinde kullanılan temel bir makine öğrenmesi yöntemidir. Projede karşılaştırma için başlangıç modeli olarak kullanılacaktır.

### Karar Ağacı

Verilerden karar kuralları oluşturarak sınıflandırma yapan bir yöntemdir. Lojistik Regresyon ile farklı bir yaklaşımı temsil ettiği için karşılaştırmaya dâhil edilmiştir.

### Planlanan Model Değerlendirmesi

Modeller aynı eğitim/test ayrımı kullanılarak karşılaştırılacaktır.

Planlanan ölçütler:

| Ölçüt | Açıklama |
|---|---|
| Accuracy | Doğru tahmin oranı |
| Precision | Pozitif tahminlerin doğruluğu |
| Recall | Gerçek pozitif örnekleri yakalama oranı |
| F1-Score | Precision ve Recall'un dengeli özeti |
| Confusion Matrix | Doğru ve yanlış sınıflandırmaların dağılımı |

Test verilerinin model eğitimine bilgi sızdırmamasına dikkat edilecektir.

> **Not:** Model eğitimleri ve test sonuçları tamamlandığında bu bölüm gerçek deney sonuçlarıyla güncellenecektir.

---

## 📊 6. Haftalık Çalışmalar ve İlerleme


## 📂 Gerçekleştirilen Çalışmalar

Proje kapsamında tamamlanan çalışmalar, ilgili dosyalar ve belgelerle birlikte GitHub deposunda düzenli olarak saklanmaktadır.

| Çalışma | Kapsam | Dosyalar |
|---|---|---|
| **5. Hafta — UML ve Tasarım** | Use Case, Activity ve Class diyagramlarının hazırlanması; sistemin yapısının ve işleyişinin modellenmesi. | [UML Diyagramları](docs/uml/) |
| **6. Hafta — Veri Analizi** | UCI Banknote Authentication veri setinin Google Colab ortamında incelenmesi, temel istatistiklerin hesaplanması ve grafiklerle görselleştirilmesi. | Google Colab (notebooks/Hafta6_Ogrenci_Proje_Veri_Analizi_Sablonu.ipynb) |




---

## 🛠️ 7. Kullanılan Teknolojiler ve Araçlar

| Teknoloji / Araç | Kullanım Amacı |
|---|---|
| **Python** | Veri analizi ve model geliştirme |
| **Google Colab** | Bulut tabanlı Python çalışma ortamı |
| **Matplotlib** | Grafik ve görselleştirme |
| **Scikit-learn ** | Makine öğrenmesi modellerinin eğitimi ve değerlendirilmesi |
| **Git ve GitHub** | Sürüm kontrolü ve ekip çalışması |
| **draw.io / diagrams.net** | UML diyagramlarının hazırlanması |

İsteğe bağlı arayüzün kullanılacak teknolojisi, geliştirme aşamasında belirlenecektir.

---


## 👥 8. Proje Ekibi ve Görev Dağılımı

Proje, üç kişilik ekip tarafından yürütülmektedir. Görevler; model geliştirme, yazılım geliştirme, proje yönetimi ve dokümantasyon alanlarında paylaştırılmıştır.

### 📋 Genel Görev Dağılımı

| Ekip Üyesi | Görev ve Sorumluluklar |
|---|---|
| **Miraç Yaşar** | GitHub deposunun genel yönetimi, dosya ve sürüm organizasyonu, isteğe bağlı (Should Have) uygulamanın arayüz ve görüntü işleme sisteminin geliştirilmesi ve  sunumların hazırlanması ve gerçekleştirilmesi. |
| **İbrahim Alo** | Veri analizi, Lojistik Regresyon ve Karar Ağacı modellerinin geliştirilmesi ve test edilmesi, sunumların hazırlanması ve gerçekleştirilmesi. |
| **Buğra Ahat** | Projenin tüm raporlama ve dokümantasyon süreçlerinin yürütülmesi, teknik çalışmaların belgelenmesi, haftalık raporların hazırlanması ve proje sonuçlarının raporlanması. |


---


## 📚 9. Kaynakça ve Lisans

**Veri seti atfı:**

Lohweg, V. (2012). *Banknote Authentication* [Dataset]. UCI Machine Learning Repository.

https://doi.org/10.24432/C55P57

**Veri seti lisansı:**

Creative Commons Attribution 4.0 International (CC BY 4.0)

https://creativecommons.org/licenses/by/4.0/

Veri seti kullanılırken kaynak ve lisans bilgileri korunacaktır. Veri değiştirilerek paylaşılırsa yapılan değişiklikler de belirtilecektir.

İsteğe bağlı görüntü analizi geliştirmesinde kullanılabilecek yeni veri setleri için kaynak, lisans ve banknot görsellerinin kullanım koşulları ayrıca incelenecektir.

---

**Marmara Üniversitesi — Yazılım Mühendisliği Temelleri | 2026–2027 Güz Dönemi**

*Proje geliştirme süreci devam etmektedir.*
