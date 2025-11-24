from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

# Load model paths
model_path = os.path.join(os.path.dirname(__file__), 'models', 'mental_health_model.pkl')
model_info_path = os.path.join(os.path.dirname(__file__), 'models', 'model_info.pkl')

# Load trained model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load model info (feature columns)
with open(model_info_path, 'rb') as f:
    model_info = pickle.load(f)

feature_columns = model_info['feature_columns']


# ================= ROUTES =================

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')

    try:
        # Get form data
        nama = request.form.get('nama', '').strip()
        jenis_kelamin = int(request.form.get('jenis_kelamin', 0))
        usia = int(request.form.get('usia', 0))
        tekanan_akademik = int(request.form.get('tekanan_akademik', 3))
        kepuasan_belajar = int(request.form.get('kepuasan_belajar', 3))
        durasi_tidur = float(request.form.get('durasi_tidur', 7))
        kualitas_pola_makan = int(request.form.get('kualitas_pola_makan', 3))
        pikiran_bunuh_diri = int(request.form.get('pikiran_bunuh_diri', 0))
        jam_belajar = float(request.form.get('jam_belajar', 5))
        stres_finansial = int(request.form.get('stres_finansial', 0))
        riwayat_gangguan_mental = int(request.form.get('riwayat_gangguan_mental', 0))

        # Validate inputs
        if not nama:
            return "Error: Nama mahasiswa tidak boleh kosong", 400
        
        if usia < 15 or usia > 50:
            return "Error: Usia harus antara 15-50 tahun", 400
        
        if durasi_tidur < 0 or durasi_tidur > 24:
            return "Error: Durasi tidur tidak valid", 400
        
        if jam_belajar < 0 or jam_belajar > 24:
            return "Error: Jam belajar tidak valid", 400

        # Prepare features
        features = np.array([
            jenis_kelamin,
            usia,
            tekanan_akademik,
            kepuasan_belajar,
            durasi_tidur,
            kualitas_pola_makan,
            pikiran_bunuh_diri,
            jam_belajar,
            stres_finansial,
            riwayat_gangguan_mental
        ]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0]
        confidence = int(max(prediction_proba) * 100)

        return render_template(
            'result.html',
            nama=nama,
            jenis_kelamin=str(jenis_kelamin),
            usia=usia,
            tekanan_akademik=tekanan_akademik,
            kepuasan_belajar=kepuasan_belajar,
            durasi_tidur=durasi_tidur,
            kualitas_pola_makan=kualitas_pola_makan,
            pikiran_bunuh_diri=str(pikiran_bunuh_diri),
            jam_belajar=jam_belajar,
            stres_finansial=str(stres_finansial),
            riwayat_gangguan_mental=str(riwayat_gangguan_mental),
            prediction=prediction,
            confidence=confidence
        )

    except Exception as e:
        return f"Error: {str(e)}", 500


@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()

        features = np.array([
            int(data.get('jenis_kelamin', 0)),
            int(data.get('usia', 0)),
            int(data.get('tekanan_akademik', 3)),
            int(data.get('kepuasan_belajar', 3)),
            float(data.get('durasi_tidur', 7)),
            int(data.get('kualitas_pola_makan', 3)),
            int(data.get('pikiran_bunuh_diri', 0)),
            float(data.get('jam_belajar', 5)),
            int(data.get('stres_finansial', 0)),
            int(data.get('riwayat_gangguan_mental', 0))
        ]).reshape(1, -1)

        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0]
        confidence = float(max(prediction_proba))

        return {
            'prediction': int(prediction),
            'prediction_label': 'Sehat/Normal' if prediction == 0 else 'Depresi',
            'confidence': confidence,
            'message': 'Prediksi berhasil'
        }, 200

    except Exception as e:
        return {'error': str(e)}, 400


# =============== RUN SERVER (REPLIT VERSION) ===============
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

