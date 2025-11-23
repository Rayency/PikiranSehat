import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Load dataset dari folder "projek matdis"
dataset_path = r'c:\Users\LENOVO\OneDrive\Documents\projek matdis\Depression Student Dataset.csv'

print("Loading dataset...")
df = pd.read_csv(dataset_path)

print(f"Dataset shape: {df.shape}")
print(f"\nColumn names:")
print(df.columns.tolist())
print(f"\nFirst few rows:")
print(df.head())
print(f"\nData types:")
print(df.dtypes)
print(f"\nDataset info:")
print(df.info())

# Map column names untuk sesuai dengan form kami
# Dataset columns: Gender, Age, Academic Pressure, Study Satisfaction, Sleep Duration, 
#                 Dietary Habits, Have you ever had suicidal thoughts ?, Study Hours, 
#                 Financial Stress, Family History of Mental Illness, Depression

feature_mapping = {
    'Gender': 'Jenis_Kelamin',
    'Age': 'Usia',
    'Academic Pressure': 'Tekanan_Akademik',
    'Study Satisfaction': 'Kepuasan_Belajar',
    'Sleep Duration': 'Durasi_Tidur',
    'Dietary Habits': 'Kualitas_Pola_Makan',
    'Have you ever had suicidal thoughts ?': 'Pikiran_Bunuh_Diri',
    'Study Hours': 'Jam_Belajar_Harian',
    'Financial Stress': 'Stres_Finansial',
    'Family History of Mental Illness': 'Riwayat_Gangguan_Mental',
    'Depression': 'Depression'
}

# Rename columns
df_renamed = df.rename(columns=feature_mapping)

# Feature engineering - convert to numeric
X = df_renamed.drop('Depression', axis=1).copy()
y = df_renamed['Depression'].copy()

# Initialize label encoders dictionary
label_encoders = {}

# Encode Gender
le_gender = LabelEncoder()
X['Jenis_Kelamin'] = le_gender.fit_transform(X['Jenis_Kelamin'])
label_encoders['Jenis_Kelamin'] = {'Male': 0, 'Female': 1}
print(f"\nGender mapping: {label_encoders['Jenis_Kelamin']}")

# Handle Sleep Duration - convert "5-6 hours" to numeric
def map_sleep_duration(sleep_str):
    if pd.isna(sleep_str):
        return 6  # default
    sleep_str = str(sleep_str).lower()
    if 'more than 8' in sleep_str:
        return 9
    elif '7-8' in sleep_str:
        return 7.5
    elif '5-6' in sleep_str:
        return 5.5
    elif 'less than 5' in sleep_str:
        return 4
    else:
        return 6  # default

X['Durasi_Tidur'] = X['Durasi_Tidur'].apply(map_sleep_duration)
print(f"Sleep Duration mapped")

# Encode Dietary Habits
le_dietary = LabelEncoder()
dietary_mapping = X['Kualitas_Pola_Makan'].unique()
print(f"Dietary Habits unique values: {dietary_mapping}")
dietary_numeric = []
for val in X['Kualitas_Pola_Makan']:
    if 'Unhealthy' in val or 'unhealthy' in val:
        dietary_numeric.append(1)
    elif 'Moderate' in val or 'moderate' in val:
        dietary_numeric.append(3)
    elif 'Healthy' in val or 'healthy' in val:
        dietary_numeric.append(5)
    else:
        dietary_numeric.append(3)  # default
X['Kualitas_Pola_Makan'] = dietary_numeric
label_encoders['Kualitas_Pola_Makan'] = {'Unhealthy': 1, 'Moderate': 3, 'Healthy': 5}

# Encode Suicidal Thoughts (Yes/No)
le_suicidal = LabelEncoder()
suicidal_mapping = {'No': 0, 'Yes': 1}
X['Pikiran_Bunuh_Diri'] = X['Pikiran_Bunuh_Diri'].map(suicidal_mapping).fillna(0).astype(int)
label_encoders['Pikiran_Bunuh_Diri'] = suicidal_mapping

# Encode Financial Stress (Yes/No)
# Need to convert text to Yes/No first
financial_mapping = {}
for val in X['Stres_Finansial'].unique():
    if pd.isna(val):
        financial_mapping[val] = 0
    else:
        financial_mapping[val] = 1 if str(val).lower() in ['yes', '1', 'true'] else 0

X['Stres_Finansial'] = X['Stres_Finansial'].map(financial_mapping).fillna(0).astype(int)
label_encoders['Stres_Finansial'] = financial_mapping

# Encode Family History (Yes/No)
family_history_mapping = {}
for val in X['Riwayat_Gangguan_Mental'].unique():
    if pd.isna(val):
        family_history_mapping[val] = 0
    else:
        family_history_mapping[val] = 1 if str(val).lower() in ['yes', '1', 'true'] else 0

X['Riwayat_Gangguan_Mental'] = X['Riwayat_Gangguan_Mental'].map(family_history_mapping).fillna(0).astype(int)
label_encoders['Riwayat_Gangguan_Mental'] = family_history_mapping

# Target encoding (Depression: Yes=1, No=0)
y_encoded = (y == 'Yes').astype(int)

# Display feature info
print(f"\n[OK] Features prepared")
print(f"Shape: {X.shape}")
print(f"Target distribution: {np.bincount(y_encoded)}")

# Reorder features sesuai dengan form kami
feature_columns = [
    'Jenis_Kelamin',
    'Usia', 
    'Tekanan_Akademik',
    'Kepuasan_Belajar',
    'Durasi_Tidur',
    'Kualitas_Pola_Makan',
    'Pikiran_Bunuh_Diri',
    'Jam_Belajar_Harian',
    'Stres_Finansial',
    'Riwayat_Gangguan_Mental'
]

X = X[feature_columns]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Train model
print("\nTraining Random Forest model...")
model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight={0: 1.0, 1: 1.3}  # Depresi lebih penting (weight 1.3x)
)
model.fit(X_train, y_train)

# Evaluate
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"Train accuracy: {train_score:.4f}")
print(f"Test accuracy: {test_score:.4f}")

# Feature importance
print(f"\nFeature importance:")
for name, importance in zip(feature_columns, model.feature_importances_):
    print(f"  {name}: {importance:.4f}")

# Save model
os.makedirs('models', exist_ok=True)
with open('models/mental_health_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save feature columns info
model_info = {
    'feature_columns': feature_columns,
    'label_encoders': label_encoders
}

with open('models/model_info.pkl', 'wb') as f:
    pickle.dump(model_info, f)

print("\n[OK] Model saved successfully!")
print("  - models/mental_health_model.pkl")
print("  - models/model_info.pkl")
print(f"\n[OK] Training completed with {len(df)} samples")

