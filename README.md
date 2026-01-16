🧠 Tumor Detection 

✨ Özellikler
Hızlı Tespit: YOLOv11 modeli ile tıbbi görüntüler üzerinde yüksek doğruluklu nesne tespiti.

Web Arayüzü: Flask tabanlı, modern ve kullanıcı dostu kontrol paneli.

Çoklu Dosya Analizi: Aynı anda birden fazla MR görselini işleme yeteneği.

Analiz Geçmişi: Session (oturum) bazlı geçmiş takibi ve görselleştirme.

Detaylı Raporlama: Her bir tespit için % bazında güven (confidence) skoru.

🛠️ Kullanılan Teknolojiler
Dil: Python

Model: YOLOv8 (Ultralytics)

Web Framework: Flask

Görüntü İşleme: OpenCV, Supervision

Arayüz: HTML5, CSS3 (FontAwesome entegrasyonu ile)


pip install flask opencv-python ultralytics supervision
python app.py

<img width="1919" height="874" alt="1" src="https://github.com/user-attachments/assets/ee718700-8275-4be8-b727-dbd7ee844e2a" />




![1](https://github.com/user-attachments/assets/48fbdd59-12af-4242-917c-e095fb156191)



<img width="1919" height="867" alt="Screenshot_3" src="https://github.com/user-attachments/assets/f1179b1a-4211-4495-9374-2ace34eba400" />


📊 Eğitim Süreci (Dataset & Training)
Model, titizlikle etiketlenmiş MR veri setleri kullanılarak eğitilmiştir. Eğitim sürecinde modelin genelleme yeteneğini artırmak için veri artırma (augmentation) teknikleri uygulanmış ve last.pt ağırlık dosyası en iyi sonuç veren epoch verileriyle oluşturulmuştur.

