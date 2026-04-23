import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

print("="*70)
print("YOUTUBE DATA ANALYSIS & VIRAL VIDEO PREDICTION")
print("="*70)

# ======================
# 1. LOAD DATA
# ======================
print("\n[1] Loading data dari clean_youtube_data.csv...")
df = pd.read_csv(
    "clean_youtube_data.csv",
    sep=';',
    encoding='latin1',
    on_bad_lines='skip',
    low_memory=False
)

print(f"Dataset shape: {df.shape}")
print(f"Jumlah baris: {len(df)}")
print(f"Jumlah kolom: {len(df.columns)}")

# Drop kolom Unnamed yang tidak berguna
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(f"Setelah drop Unnamed columns: {df.shape}")
print(f"Kolom yang valid: {df.columns.tolist()}")

# ======================
# 2. DATA CLEANING & PREPROCESSING
# ======================
print("\n[2] Cleaning & Preprocessing data...")

# Filter hanya kolom yang diperlukan
required_cols = ['likes', 'comment_count', 'category_id', 'viral']
available_cols = [col for col in required_cols if col in df.columns]
print(f"\nKolom yang tersedia: {available_cols}")

# Pilih kolom features yang tersedia (DEFINE SEBELUM DIGUNAKAN)
feature_cols = [col for col in ['likes', 'comment_count', 'category_id'] if col in df.columns]
print(f"Feature columns: {feature_cols}")

# Check missing values
print("\nMissing values pada kolom yang digunakan:")
missing_info = df[available_cols].isnull().sum()
print(missing_info)

# Drop missing values
df_clean = df[available_cols].dropna()
print(f"\nDataset setelah drop missing values: {df_clean.shape}")

# Convert ke numeric type dan drop baris yang error
print("\nConverting features to numeric...")
for col in feature_cols:
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

# Drop baris dengan NaN setelah conversion
df_clean = df_clean.dropna()
print(f"Dataset setelah convert & drop NaN: {df_clean.shape}")

# Convert viral target to int
df_clean['viral'] = df_clean['viral'].astype(int)
# Display statistics
print("\n--- STATISTIK DATA ---")
print(df_clean.describe())

# ======================
# 3. PILIH FITUR & TARGET
# ======================
print("\n[3] Memilih features dan target...")

# Pilih kolom features yang tersedia
feature_cols = [col for col in ['likes', 'comment_count', 'category_id'] if col in df_clean.columns]
X = df_clean[feature_cols]
y = df_clean['viral']

print(f"Features: {X.shape}")
print(f"Target: {y.shape}")
print(f"Feature columns: {feature_cols}")
print(f"\nDistribusi target (viral):")
print(y.value_counts())
print(f"\nPersentase:")
print(y.value_counts(normalize=True) * 100)

# ======================
# 4. SPLIT DATA (TRAINING & TESTING)
# ======================
print("\n[4] Membagi data menjadi training dan testing (80-20)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set: {X_train.shape}")
print(f"Testing set: {X_test.shape}")

# ======================
# 5. FEATURE SCALING
# ======================
print("\n[5] Scaling features menggunakan StandardScaler...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ======================
# 6. TRAIN MODEL (Random Forest Classifier)
# ======================
print("\n[6] Training Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1, verbose=0)
model.fit(X_train_scaled, y_train)
print("✓ Model training selesai!")

# ======================
# 7. PREDIKSI & EVALUASI
# ======================
print("\n[7] Evaluasi Model...")
y_pred_train = model.predict(X_train_scaled)
y_pred_test = model.predict(X_test_scaled)

# Training Performance
print("\n" + "-"*70)
print("TRAINING SET PERFORMANCE")
print("-"*70)
print(f"Accuracy:  {accuracy_score(y_train, y_pred_train):.4f}")
print(f"Precision: {precision_score(y_train, y_pred_train):.4f}")
print(f"Recall:    {recall_score(y_train, y_pred_train):.4f}")
print(f"F1-Score:  {f1_score(y_train, y_pred_train):.4f}")

# Testing Performance
print("\n" + "-"*70)
print("TESTING SET PERFORMANCE")
print("-"*70)
test_accuracy = accuracy_score(y_test, y_pred_test)
print(f"Accuracy:  {test_accuracy:.4f}")
print(f"Precision: {precision_score(y_test, y_pred_test):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred_test):.4f}")
print(f"F1-Score:  {f1_score(y_test, y_pred_test):.4f}")

# Classification Report
print("\n" + "-"*70)
print("CLASSIFICATION REPORT (TEST SET)")
print("-"*70)
print(classification_report(y_test, y_pred_test, target_names=['Not Viral', 'Viral']))

# Confusion Matrix
print("\n" + "-"*70)
print("CONFUSION MATRIX")
print("-"*70)
cm = confusion_matrix(y_test, y_pred_test)
print(cm)
print(f"\nTrue Negatives (TN):  {cm[0,0]}")
print(f"False Positives (FP): {cm[0,1]}")
print(f"False Negatives (FN): {cm[1,0]}")
print(f"True Positives (TP):  {cm[1,1]}")

# Feature Importance
print("\n" + "-"*70)
print("FEATURE IMPORTANCE")
print("-"*70)
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)
print(feature_importance.to_string(index=False))

print("\n" + "="*70)
print("✓ ANALISIS SELESAI!")
print("="*70)