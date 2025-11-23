"""
Test script untuk Mental Health Prediction Web App
"""

import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

def test_home_page():
    """Test home page"""
    print("=" * 60)
    print("TEST 1: Home Page")
    print("=" * 60)
    
    response = requests.get(f'{BASE_URL}/')
    print(f"Status Code: {response.status_code}")
    print(f"Content length: {len(response.content)} bytes")
    print(f"Page title found: {'Prediksi Kesehatan Mental' in response.text}")
    print()


def test_predict_form_page():
    """Test prediction form page"""
    print("=" * 60)
    print("TEST 2: Prediction Form Page")
    print("=" * 60)
    
    response = requests.get(f'{BASE_URL}/predict')
    print(f"Status Code: {response.status_code}")
    print(f"Content length: {len(response.content)} bytes")
    print(f"Form found: {'predictionForm' in response.text}")
    print()


def test_form_submission_valid():
    """Test form submission dengan data valid"""
    print("=" * 60)
    print("TEST 3: Form Submission - Valid Data")
    print("=" * 60)
    
    form_data = {
        'nama': 'John Doe',
        'jenis_kelamin': '0',  # Laki-laki
        'usia': '20',
        'tekanan_akademik': '4',
        'kepuasan_belajar': '3',
        'durasi_tidur': '7',
        'kualitas_pola_makan': '3',
        'pikiran_bunuh_diri': '0',
        'jam_belajar': '5',
        'stres_finansial': '0',
        'riwayat_gangguan_mental': '0'
    }
    
    response = requests.post(f'{BASE_URL}/predict', data=form_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response contains result: {'Hasil Prediksi' in response.text or 'result' in response.text}")
    print(f"Response length: {len(response.content)} bytes")
    print()


def test_form_submission_invalid_nama():
    """Test form submission dengan nama kosong"""
    print("=" * 60)
    print("TEST 4: Form Submission - Invalid (Empty Name)")
    print("=" * 60)
    
    form_data = {
        'nama': '',  # Empty
        'jenis_kelamin': '0',
        'usia': '20',
        'tekanan_akademik': '4',
        'kepuasan_belajar': '3',
        'durasi_tidur': '7',
        'kualitas_pola_makan': '3',
        'pikiran_bunuh_diri': '0',
        'jam_belajar': '5',
        'stres_finansial': '0',
        'riwayat_gangguan_mental': '0'
    }
    
    response = requests.post(f'{BASE_URL}/predict', data=form_data)
    print(f"Status Code: {response.status_code}")
    print(f"Error message found: {'Error' in response.text}")
    print()


def test_form_submission_invalid_usia():
    """Test form submission dengan usia tidak valid"""
    print("=" * 60)
    print("TEST 5: Form Submission - Invalid (Age out of range)")
    print("=" * 60)
    
    form_data = {
        'nama': 'John Doe',
        'jenis_kelamin': '0',
        'usia': '100',  # Invalid age
        'tekanan_akademik': '4',
        'kepuasan_belajar': '3',
        'durasi_tidur': '7',
        'kualitas_pola_makan': '3',
        'pikiran_bunuh_diri': '0',
        'jam_belajar': '5',
        'stres_finansial': '0',
        'riwayat_gangguan_mental': '0'
    }
    
    response = requests.post(f'{BASE_URL}/predict', data=form_data)
    print(f"Status Code: {response.status_code}")
    print(f"Error message found: {'Error' in response.text}")
    print()


def test_api_endpoint():
    """Test API endpoint JSON"""
    print("=" * 60)
    print("TEST 6: API Endpoint (JSON)")
    print("=" * 60)
    
    json_data = {
        'jenis_kelamin': 0,
        'usia': 20,
        'tekanan_akademik': 4,
        'kepuasan_belajar': 3,
        'durasi_tidur': 7,
        'kualitas_pola_makan': 3,
        'pikiran_bunuh_diri': 0,
        'jam_belajar': 5,
        'stres_finansial': 0,
        'riwayat_gangguan_mental': 0
    }
    
    response = requests.post(
        f'{BASE_URL}/api/predict',
        json=json_data,
        headers={'Content-Type': 'application/json'}
    )
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Prediction: {result.get('prediction_label')}")
        print(f"Confidence: {result.get('confidence'):.2%}")
        print(f"Message: {result.get('message')}")
    else:
        print(f"Error: {response.text}")
    print()


def test_api_endpoint_different_values():
    """Test API dengan nilai yang berbeda (untuk depresi)"""
    print("=" * 60)
    print("TEST 7: API Endpoint - Depression Case")
    print("=" * 60)
    
    json_data = {
        'jenis_kelamin': 1,
        'usia': 21,
        'tekanan_akademik': 5,  # Tinggi
        'kepuasan_belajar': 1,  # Rendah
        'durasi_tidur': 3,      # Kurang tidur
        'kualitas_pola_makan': 2,  # Buruk
        'pikiran_bunuh_diri': 1,    # Ada
        'jam_belajar': 12,          # Banyak
        'stres_finansial': 1,       # Ada
        'riwayat_gangguan_mental': 1  # Ada
    }
    
    response = requests.post(
        f'{BASE_URL}/api/predict',
        json=json_data,
        headers={'Content-Type': 'application/json'}
    )
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Prediction: {result.get('prediction_label')}")
        print(f"Confidence: {result.get('confidence'):.2%}")
        print(f"Message: {result.get('message')}")
    else:
        print(f"Error: {response.text}")
    print()


def run_all_tests():
    """Jalankan semua test"""
    print("\n")
    print("=" * 60)
    print("Mental Health Prediction System - Test Suite")
    print("=" * 60)
    print()
    
    try:
        test_home_page()
        test_predict_form_page()
        test_form_submission_valid()
        test_form_submission_invalid_nama()
        test_form_submission_invalid_usia()
        test_api_endpoint()
        test_api_endpoint_different_values()
        
        print("=" * 60)
        print("SEMUA TEST SELESAI - OK")
        print("=" * 60)
        
    except Exception as e:
        print(f"ERROR: {e}")
        print("Pastikan Flask app masih running di http://127.0.0.1:5000")


if __name__ == '__main__':
    run_all_tests()
