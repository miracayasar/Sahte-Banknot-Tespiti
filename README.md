# Sahte Banknot Tespiti

**Marmara Üniversitesi — Bilgisayar Programcılığı | Yazılım Mühendisliği Temelleri Dönem Projesi**

UCI Banknote Authentication veri seti kullanılarak, banknotlara ait sayısal özelliklerden gerçek/sahte ayrımı yapan iki makine öğrenmesi yöntemi karşılaştırılacaktır. Çalışma Python ile gerçekleştirilecek; **Lojistik Regresyon** ve **Karar Ağacı** yöntemleriyle eğitilen modellerin test sonuçları değerlendirilecektir.

## Problem ve hedef kullanıcı

Banknotların gerçek veya sahte olarak sınıflandırılması bir makine öğrenmesi problemidir. Bu projede banknot fotoğrafları doğrudan işlenmeyecek; görüntülerden önceden elde edilmiş sayısal veriler kullanılacaktır.

Çalışmanın hedef kullanıcısı, farklı sınıflandırma yöntemlerinin sonuçlarını incelemek isteyen öğrenci veya araştırmacıdır. Kullanıcıya yönelik bir web ya da mobil uygulama geliştirilmeyecektir.

## Projenin amacı

Aynı veri seti üzerinde Lojistik Regresyon ve Karar Ağacı yöntemleriyle iki model eğitmek, bu modelleri karşılaştırılabilir koşullarda test etmek ve elde edilen sonuçları raporlamaktır.

**Araştırma sorusu:** Bu iki yöntem, UCI Banknote Authentication veri setinde nasıl performans göstermektedir?

## Proje kapsamı

Projede planlanan temel işler:

1. Veri setine erişmek ve kullanım lisansını kontrol etmek.
2. Verileri Python ortamına yüklemek, incelemek ve gerekiyorsa hazırlamak.
3. Verileri eğitim ve test gruplarına ayırmak.
4. Lojistik Regresyon ve Karar Ağacı modellerini eğitmek.
5. Modellerin başarısını eğitimde kullanılmamış veriler üzerinde test etmek.
6. Test sonuçlarını karşılaştırmak ve raporlamak.

**İşlevsel olmayan gereksinim:** Deney adımları belgelenebilir ve tekrar uygulanabilir olmalı; test verilerinden eğitim sırasında bilgi sızdırılmamalıdır.

### Kapsam dışı

- Web sitesi veya mobil uygulama geliştirmek.
- Banknot fotoğrafı yüklemek ya da kamerayla banknot taramak.
- Ham görüntülerden yeni sayısal özellikler çıkarmak.
- Derin öğrenme modeli geliştirmek.
- Sonuçları gerçek hayatta kullanılan bir para doğrulama cihazının güvenilirlik kanıtı olarak sunmak.

## Veri seti

- **Adı:** Banknote Authentication
- **Kaynağı:** UCI Machine Learning Repository
- **Hazırlayan:** Volker Lohweg (2012)
- **Resmî sayfa:** https://archive.ics.uci.edu/dataset/267/banknote
- **DOI:** https://doi.org/10.24432/C55P57
- **Lisansı:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

Veri setinde **1.372 kayıt**, dört sayısal özellik ve bir sınıf etiketi bulunmaktadır.

| Alan | Açıklama |
| --- | --- |
| `variance` | Varyans |
| `skewness` | Çarpıklık |
| `curtosis` | Basıklık |
| `entropy` | Entropi |
| `class` | Gerçek/sahte sınıfını belirten tam sayı etiketi |

Veri seti ham banknot fotoğraflarını içermez. Veri seti ve lisans bilgileri yukarıdaki resmî UCI sayfasından incelenebilir. Veri seti değiştirilerek paylaşılırsa yapılan değişiklikler de belirtilecektir.

**Veri seti atfı:** Lohweg, V. (2012). *Banknote Authentication* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55P57

## Seçilen yöntemler

**Lojistik Regresyon:** İki sınıflı sınıflandırma problemlerinde kullanılabilen temel bir yöntemdir.

**Karar Ağacı:** Verilere dayalı karar kuralları oluşturarak sınıflandırma yapan, Lojistik Regresyon'dan farklı bir yaklaşımdır.

Modeller aynı eğitim/test ayrımı kullanılarak karşılaştırılacaktır. Değerlendirme ölçülerinin ayrıntıları uygulama sırasında kesinleştirilecektir.

## Kullanılacak teknolojiler

- Python
- Makine öğrenmesi için gerekli Python kütüphaneleri
- Git ve GitHub
- draw.io (diagrams.net)


## Proje yönetimi

Yapılacak işler, sorumlular, kabul ölçütleri ve görevlerin güncel durumları **[GitHub Issues](https://github.com/miracayasar/Sahte-Banknot-Tespiti/issues)** ve GitHub Projects panosunda takip edilecektir.

