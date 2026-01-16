from flask import Flask, render_template, request, url_for, session, redirect
import os
import cv2
from ultralytics import YOLO
import supervision as sv

app = Flask(__name__)
# Oturum (session) verilerini güvenli tutmak için bir anahtar
app.secret_key = 'tumor_detection_secret_key'

# YOLO modelini yükle
model = YOLO("last.pt")

# Klasör yolları
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'static/outputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Klasörleri otomatik oluştur
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_image(input_path, output_path):
    """Görseli işler, kutucukları çizer ve tespit verilerini döner."""
    image = cv2.imread(input_path)
    if image is None: 
        return 0, []

    # Görüntü boyutunu modelin beklediği boyuta getir
    resized = cv2.resize(image, (640, 640))
    
    # Model tahmini
    results = model(resized)[0]
    detections = sv.Detections.from_ultralytics(results)

    # Görseli etiketle
    annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()
    
    annotated = annotator.annotate(scene=resized, detections=detections)
    annotated = label_annotator.annotate(scene=annotated, detections=detections)

    # İşlenmiş görseli kaydet
    cv2.imwrite(output_path, annotated)
    
    # Doğruluk oranlarını % olarak listele
    confidences = [round(float(conf) * 100, 2) for conf in detections.confidence]
    return len(detections), confidences

@app.route('/', methods=['GET', 'POST'])
def index():
    # Geçmiş verisi yoksa boş bir liste oluştur
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        files = request.files.getlist('files')
        temp_history = session['history'] # Mevcut geçmişi al

        for file in files:
            if file and file.filename != '':
                # Dosya yollarını hazırla
                input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                output_filename = 'annotated_' + file.filename
                output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
                
                # Dosyayı kaydet ve işle
                file.save(input_path)
                count, confs = process_image(input_path, output_path)

                # Yeni sonucu listenin başına ekle (En yeni en üstte)
                result_entry = {
                    'filename': file.filename,
                    'url': url_for('static', filename=f'outputs/{output_filename}'),
                    'tumor_count': count,
                    'detections': [{'confidence': c} for c in confs]
                }
                temp_history.insert(0, result_entry)
        
        session['history'] = temp_history
        session.modified = True

    return render_template('index.html', results=session['history'])

@app.route('/clear')
def clear():
    """Tüm analiz geçmişini siler."""
    session.pop('history', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)