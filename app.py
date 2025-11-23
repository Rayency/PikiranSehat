from flask import Flask, render_template, request
import pickle
import os
import numpy as np

app = Flask(__name__)

# Load model safely
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'mental_health_model.pkl')
    try:
        with open(model_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("❌ Model file not found!")
        return None

def load_model_info():
    info_path = os.path.join(os.path.dirname(__file__), 'models', 'model_info.pkl')
    try:
        with open(info_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("❌ Model info file not found!")
        return None

model = load_model()
model_info = load_model_info()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')

    try:
        nama = request.form.get('nama', '').strip()
        usia = int(request.form.get('usia', 0))
        durasi_tidur = float(request.form.get('durasi_tidur', 7))
        jam_belajar = float(request.form.get('jam_belajar', 5))

        if not nama:
            return "Nama tidak boleh kosong", 400

        features = np.array([
            int(request.form.get('jenis_kelamin', 0)),
            usia,
            int(request.form.get('tekanan_akademik', 3)),
            int(request.form.get('kepuasan_belajar', 3)),
            durasi_tidur,
            int(request.form.get('kualitas_pola_makan', 3)),
            int(request.form.get('pikiran_bunuh_diri', 0)),
            jam_belajar,
            int(request.form.get('stres_finansial', 0)),
            int(request.form.get('riwayat_gangguan_mental', 0))
        ]).reshape(1, -1)

        prediction = model.predict(features)[0]
        prediction_proba = model.predict_proba(features)[0]
        confidence = int(max(prediction_proba) * 100)

        return render_template('result.html',
                               nama=nama,
                               prediction=prediction,
                               confidence=confidence)

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

        return {
            "prediction": int(prediction),
            "status": "Sehat" if prediction == 0 else "Depresi"
        }, 200

    except Exception as e:
        return {"error": str(e)}, 400

