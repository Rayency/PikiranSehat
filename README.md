# 🧠 Mental Health Prediction System
## Sistem Prediksi Kesehatan Mental Mahasiswa

Aplikasi web interaktif untuk memprediksi status kesehatan mental mahasiswa menggunakan machine learning (Random Forest). Dibangun dengan Python Flask dan desain responsif menggunakan Tailwind CSS.

---

## 📋 Fitur Utama

✅ **Home Page** - Pengenalan aplikasi dan penjelasan tujuan
✅ **Form Prediksi** - Formulir lengkap dengan 10 pertanyaan penting
✅ **Skala Likert** - Rating 1-5 untuk pertanyaan subjektif  
✅ **Validasi Input** - Client-side dan server-side validation
✅ **Hasil Prediksi** - Status kesehatan mental + penjelasan detail
✅ **Rekomendasi** - Saran praktis berdasarkan hasil prediksi
✅ **Responsif** - Desain mobile-friendly dengan Tailwind CSS
✅ **API Endpoint** - JSON API untuk integrasi dengan aplikasi lain

---

## 🚀 Instalasi & Setup

### 1. Clone atau Download Project
```bash
cd c:\Users\LENOVO\OneDrive\Documents\projekan
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train Model (Optional - sudah disediakan)
```bash
python train_model.py
```

### 4. Jalankan Aplikasi
```bash
python app.py
```

### 5. Akses Aplikasi
Buka browser dan kunjungi: **http://127.0.0.1:5000**

---

## 📁 Struktur Folder

```
projekan/
├── app.py                    # Main Flask application
├── train_model.py            # Script untuk training model
├── requirements.txt          # Python dependencies
├── README.md                # Dokumentasi ini
│
├── models/                   # Folder model machine learning
│   ├── mental_health_model.pkl
│   └── model_info.pkl
│
├── templates/               # HTML templates
│   ├── home.html           # Halaman utama
│   ├── predict.html        # Form prediksi
│   └── result.html         # Halaman hasil
│
└── static/                  # Static files (CSS, JS, images)
    └── (folder kosong untuk assets tambahan)
```

---

## 🔍 Pertanyaan & Input Form

### Bagian 1: Informasi Pribadi
- **Nama Mahasiswa** (text input)
- **Jenis Kelamin** (dropdown: Laki-laki / Perempuan)
- **Usia** (number input, range 15-50)

### Bagian 2: Kehidupan Akademik
- **Tekanan Akademik** (skala 1-5: sangat rendah → sangat tinggi)
- **Kepuasan Belajar** (skala 1-5: sangat tidak puas → sangat puas)
- **Jam Belajar Per Hari** (number input, 0-24 jam)

### Bagian 3: Gaya Hidup
- **Durasi Tidur** (number input, 0-24 jam)
- **Kualitas Pola Makan** (skala 1-5: sangat buruk → sangat baik)

### Bagian 4: Kesehatan Mental
- **Pikiran Bunuh Diri** (ya/tidak)
- **Stres Finansial** (ya/tidak)
- **Riwayat Gangguan Mental di Keluarga** (ya/tidak)

---

## 🤖 Model Machine Learning

### Tipe Model
- **Algorithm**: Random Forest Classifier
- **Training Samples**: 200 data sintetis
- **Test Accuracy**: 82.5%
- **Features**: 10 fitur input

### Feature Importance (Urutan Pengaruh)
1. **Durasi Tidur** (20.91%) - Faktor paling penting
2. **Tekanan Akademik** (17.45%)
3. **Jam Belajar Harian** (17.44%)
4. **Kepuasan Belajar** (11.39%)
5. **Usia** (13.01%)
6. **Kualitas Pola Makan** (6.54%)
7. **Jenis Kelamin** (3.54%)
8. **Riwayat Gangguan Mental** (3.79%)
9. **Pikiran Bunuh Diri** (3.31%)
10. **Stres Finansial** (2.62%)

---

## 📊 Output Prediksi

Aplikasi memberikan hasil dalam format:

```
Status: Sehat/Normal atau Depresi
Tingkat Kepercayaan: 0-100%
Penjelasan Detail: Interpretasi hasil prediksi
Rekomendasi: Saran spesifik berdasarkan hasil
```

---

## 🔗 API Endpoints

### 1. Home Page
```
GET /
```
Menampilkan halaman utama

### 2. Prediction Form
```
GET /predict
```
Menampilkan formulir prediksi

### 3. Process Prediction (Form)
```
POST /predict
Content-Type: application/x-www-form-urlencoded

nama=John
jenis_kelamin=0
usia=20
tekanan_akademik=4
...
```

### 4. API Prediction (JSON)
```
POST /api/predict
Content-Type: application/json

{
  "jenis_kelamin": 0,
  "usia": 20,
  "tekanan_akademik": 4,
  "kepuasan_belajar": 3,
  "durasi_tidur": 7,
  "kualitas_pola_makan": 3,
  "pikiran_bunuh_diri": 0,
  "jam_belajar": 5,
  "stres_finansial": 0,
  "riwayat_gangguan_mental": 0
}
```

**Response:**
```json
{
  "prediction": 0,
  "prediction_label": "Sehat/Normal",
  "confidence": 0.92,
  "message": "Prediksi berhasil"
}
```

---

## 🎨 Desain & UX

- **Framework CSS**: Tailwind CSS (CDN)
- **Color Scheme**: 
  - Indigo (#4F46E5) - Primary
  - Green (#10B981) - Success/Healthy
  - Red (#EF4444) - Danger/Depression
  - Gray - Neutral
- **Responsif**: Mobile, Tablet, Desktop
- **Validasi**: HTML5 + JavaScript

---

## ⚠️ Disclaimer & Catatan Penting

1. **Bukan Diagnosis Medis**: Aplikasi ini adalah untuk self-assessment dan edukasi saja
2. **Konsultasi Profesional**: Selalu konsultasikan dengan psikolog/profesional kesehatan mental untuk diagnosis resmi
3. **Data Akurat**: Jawab pertanyaan dengan jujur untuk hasil yang akurat
4. **Privasi**: Data tidak disimpan, hanya diproses untuk prediksi

---

## 🚨 Jika Anda Dalam Krisis

Jika Anda atau seseorang yang Anda kenal mengalami pemikiran bunuh diri:

- 🆘 **Hubungi Layanan Darurat**: 112
- 📞 **Hotline Kesehatan Mental**: Hubungi dinas kesehatan setempat
- 🏥 **Kunjungi Rumah Sakit**: Pergi ke IGD rumah sakit terdekat

---

## 📝 Teknologi yang Digunakan

| Teknologi | Versi | Fungsi |
|-----------|-------|--------|
| Python | 3.8+ | Backend |
| Flask | 2.3.3 | Web Framework |
| scikit-learn | 1.3.0 | Machine Learning |
| pandas | 2.0.3 | Data Processing |
| numpy | 1.24.3 | Numerical Computing |
| Tailwind CSS | Latest | Frontend Styling |
| HTML5 | - | Markup |
| JavaScript | ES6 | Client-side Logic |

---

## 🔧 Development & Debugging

### Debug Mode
Aplikasi berjalan dalam debug mode (development). Untuk production:

```python
# Di app.py, ubah:
app.run(debug=False)
```

### Log & Error
- Check terminal untuk log Flask
- Check browser console (F12) untuk JavaScript errors

### Testing Prediksi Cepat
```python
python -c "
import pickle
import numpy as np

with open('models/mental_health_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Test data
test_input = np.array([[0, 20, 4, 3, 7, 3, 0, 5, 0, 0]])
prediction = model.predict(test_input)
print(f'Prediction: {prediction}')
"
```

---

## 📈 Roadmap Pengembangan

- [ ] Database untuk menyimpan riwayat prediksi (dengan persetujuan user)
- [ ] Export hasil sebagai PDF
- [ ] Dashboard admin untuk statistik
- [ ] Multi-bahasa support
- [ ] Mobile app (React Native/Flutter)
- [ ] Integrasi dengan chatbot AI
- [ ] Video edukasi kesehatan mental

---

## 👨‍💻 Author & Kontribusi

Dibuat untuk kesadaran kesehatan mental mahasiswa Indonesia.

Untuk laporan bug atau saran, silakan hubungi atau buat issue.

---

## 📄 Lisensi

Proyek ini tersedia untuk keperluan edukasi. Silakan gunakan sesuai dengan tujuan yang baik.

---

## 📞 Kontak & Support

Untuk pertanyaan atau dukungan lebih lanjut, silakan hubungi.

**Stay healthy, stay positive! 💚**

---

*Terakhir diupdate: November 2024*
