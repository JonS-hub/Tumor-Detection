🧠 Tumor Detection AI (YOLOv11 & Flask)

✨ Özellikler
Hızlı Tespit: YOLOv11 modeli ile tıbbi görüntüler üzerinde yüksek doğruluklu nesne tespiti.

Web Arayüzü: Flask tabanlı, modern ve kullanıcı dostu kontrol paneli.

Çoklu Dosya Analizi: Aynı anda birden fazla MR görselini işleme yeteneği.

Analiz Geçmişi: Session (oturum) bazlı geçmiş takibi ve görselleştirme.

Detaylı Raporlama: Her bir tespit için % bazında güven (confidence) skoru.

✨ Features
Fast Detection: High-accuracy object detection on medical images using the YOLOv11 model.

Web Interface: Modern and user-friendly control panel based on Flask.

Multi-File Analysis: Ability to process multiple MRI images simultaneously.

Analysis History: Session-based history tracking and visualization.

Detailed Reporting: Confidence scores in % for each detection.


<img width="1919" height="874" alt="1" src="https://github.com/user-attachments/assets/1a02e0c4-fe8d-409e-af20-0333cd56e5ba" />



🛠️ Kullanılan Teknolojiler
Dil: Python

Model: YOLOv11 (Ultralytics)

Web Framework: Flask

Görüntü İşleme: OpenCV, Supervision

Arayüz: HTML5, CSS3 (FontAwesome entegrasyonu ile)

🛠️ Tech Stack
Language: Python

Model: YOLOv11 (Ultralytics)

Web Framework: Flask

Image Processing: OpenCV, Supervision

Frontend: HTML5, CSS3 (with FontAwesome integration)

![1](https://github.com/user-attachments/assets/87bf8f99-3cad-4ae7-be3b-116b6c1a4615)


📊 Eğitim Süreci (Dataset & Training)
Model, titizlikle etiketlenmiş MR veri setleri kullanılarak eğitilmiştir. Eğitim sürecinde modelin genelleme yeteneğini artırmak için veri artırma (augmentation) teknikleri uygulanmış ve last.pt ağırlık dosyası en iyi sonuç veren epoch verileriyle oluşturulmuştur.

📊 Training Process
The model was trained using meticulously labeled MRI datasets. Data augmentation techniques were applied during training to improve generalization, and the last.pt weight file was generated from the best-performing epochs.

<img width="1919" height="867" alt="Screenshot_3" src="https://github.com/user-attachments/assets/b32b7b9b-fde8-4677-859f-55cb4f2acd12" />


# Install requirements / Gereksinimleri yükleyin
pip install flask opencv-python ultralytics supervision

# Run the application / Uygulamayı çalıştırın
python app.py
