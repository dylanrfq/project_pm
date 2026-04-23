# 📊 ANALISIS DAN PREDIKSI PERFORMA KONTEN VLOG YOUTUBE MENGGUNAKAN MACHINE LEARNING

## 1. RINGKASAN EKSEKUTIF

Proyek ini menganalisis performa konten video YouTube untuk memprediksi apakah sebuah video akan menjadi **viral** atau **tidak viral** menggunakan teknik Machine Learning. Model yang dibangun mencapai akurasi **95.58%** dalam memprediksi status viral videos.

---

## 2. LATAR BELAKANG MASALAH

### Konteks:
- YouTube adalah platform streaming video terbesar dengan miliaran video
- Performa konten (viral vs non-viral) dipengaruhi oleh berbagai faktor
- Content creators perlu memahami metrik apa yang paling berpengaruh terhadap keberhasilan konten

### Pertanyaan Riset:
- **Apa saja faktor utama yang menentukan apakah sebuah video viral di YouTube?**
- **Bisakah kita memprediksi status viral video berdasarkan metrik engagement-nya?**
- **Seberapa akurat prediksi model yang dibangun?**

---

## 3. DATASET

### Sumber Data:
- **Dataset**: `clean_youtube_data.csv`
- **Total Records**: 48,697 videos
- **Data Valid**: 40,848 videos (setelah cleaning)

### Karakteristik Data:
| Aspek | Detail |
|-------|--------|
| **Jumlah Baris** | 40,848 videos |
| **Jumlah Kolom** | 17 features (setelah cleaning) |
| **Range Tanggal** | November 2017 - Januari 2019 |
| **Missing Values** | Ditangani dengan dropna() |
| **Data Terduplikasi** | Tidak ada |

### Features yang Digunakan:

#### Input Features (X):
1. **Likes** - Jumlah likes yang diterima video
2. **Comment Count** - Jumlah komentar pada video
3. **Category ID** - Kategori konten video

#### Target Variable (y):
- **Viral Status** - Binary: 1 (Viral), 0 (Non-Viral)

### Distribusi Target:
```
Video Viral:       35,536 (86.99%)
Video Non-Viral:    5,312 (13.01%)
```
⚠️ **Catatan**: Dataset sangat imbalanced (87% viral), namun model tetap performa baik.

---

## 4. METODOLOGI

### 4.1 Data Preprocessing
```python
1. Load Dataset
   ↓
2. Remove Unnamed Columns (hasil parsing error CSV)
   ↓
3. Check Missing Values & Drop NaN
   ↓
4. Convert Data Types (pandas to numeric)
   ↓
5. Handle Outliers (implicit dalam StandardScaler)
   ↓
6. Feature Scaling (StandardScaler) untuk RF optimality
```

### 4.2 Train-Test Split
- **Training Set**: 80% (32,678 videos)
- **Testing Set**: 20% (8,170 videos)
- **Strategy**: Stratified split (mempertahankan distribusi target)
- **Random State**: 42 (reproducibility)

### 4.3 Model Selection: Random Forest Classifier

#### Mengapa Random Forest?
✔️ Robust terhadap outliers  
✔️ Tidak memerlukan feature scaling (tapi kami tetap scale untuk normalisasi)  
✔️ Interpretable feature importance  
✔️ Excellent untuk binary classification  

#### Hyperparameters:
- `n_estimators`: 100 trees
- `random_state`: 42 (reproducibility)
- `n_jobs`: -1 (parallel processing)

### 4.4 Evaluation Metrics

1. **Accuracy** = (TP + TN) / (TP + TN + FP + FN)
   - Proporsi prediksi yang benar

2. **Precision** = TP / (TP + FP)
   - Dari video yang diprediksi viral, berapa % benar-benar viral?

3. **Recall** = TP / (TP + FN)
   - Dari semua video viral yang sebenarnya, berapa % yang terdeteksi?

4. **F1-Score** = 2 × (Precision × Recall) / (Precision + Recall)
   - Harmonic mean dari precision dan recall

---

## 5. HASIL & ANALISIS

### 5.1 Data Statistics

| Metrik | Likes | Comment Count | Category ID |
|--------|-------|---------------|-------------|
| Mean | 74,386 | 8,459 | 19.97 |
| Std Dev | 229,150 | 37,475 | 7.57 |
| Min | 0 | 0 | 1 |
| Max | 5,613,827 | 1,361,580 | 43 |
| 50th Percentile (Median) | 18,098 | 1,855 | 24 |

📊 **Insight**:
- Banyak outliers pada likes dan comments (std > mean)
- Category ID range: 1-43 (YouTube official categories)
- Median comments: ~2000, menunjukkan engagement yang cukup tinggi

### 5.2 Model Performance

#### Training Set
```
Accuracy:  99.96%
Precision: 99.96%
Recall:    100.00%
F1-Score:  99.98%
```

#### Testing Set ⭐
```
Accuracy:  95.58% ✓ EXCELLENT
Precision: 97.10% ✓
Recall:    97.85% ✓
F1-Score:  97.47% ✓
```

#### Confusion Matrix (Test Set):
```
                Predicted
              Non-Viral  Viral
Actual Non-V    854       208
       Viral     153      6955
```

| Metrik | Value | Interpretasi |
|--------|-------|--------------|
| **True Negatives (TN)** | 854 | Video non-viral yang tepat diprediksi non-viral |
| **False Positives (FP)** | 208 | Video non-viral tapi diprediksi viral (minor issue) |
| **False Negatives (FN)** | 153 | Video viral tapi diprediksi non-viral (major issue) |
| **True Positives (TP)** | 6,955 | Video viral yang tepat diprediksi viral ✓ |

### 5.3 Feature Importance

| Feature | Importance | Persentase |
|---------|-----------|-----------|
| **Likes** | 0.5247 | **52.47%** 🥇 |
| **Comment Count** | 0.4152 | **41.53%** 🥈 |
| **Category ID** | 0.0600 | **6.00%** 🥉 |

📌 **Insight**:
- **Likes adalah faktor DOMINAN** (>50%) dalam menentukan viral
- Engagement metrics (likes + comments) > 93% importance
- Category ID memiliki pengaruh minimal (6%)

---

## 6. KESIMPULAN

### 6.1 Temuan Utama

1. ✅ **Model sangat akurat** - 95.58% accuracy pada test set
2. ✅ **Prediksi reliable** - 97.85% recall (menangkap video viral dengan baik)
3. ✅ **Indikator kuat** - Likes & comments adalah predictor terbaik
4. ✅ **Scalable** - Model dapat diaplikasikan untuk prediksi real-time

### 6.2 Implikasi Praktis

**Untuk Content Creators:**
- Fokus pada **meningkatkan likes & engagement** ↑
- Dorong viewers untuk like & comment
- Category ID kurang penting, fokus pada kualitas konten

**Untuk Platform (YouTube):**
- Gunakan model untuk early detection viral videos
- Personalisasi rekomendasi konten
- Identifikasi content strategy yang efektif

---

## 7. KETERBATASAN & FUTURE WORK

### Keterbatasan:
1. ⚠️ Dataset imbalanced (87% viral vs 13% non-viral)
2. ⚠️ Tidak mempertimbangkan faktor temporal (trend waktu)
3. ⚠️ Missing features: engagement rate, viewer demographic, content type
4. ⚠️ Periode data terbatas (Nov 2017 - Jan 2019)

### Rekomendasi Future Work:
- 🔄 Tambah features: view count, publishing time, content duration
- 🔄 Implementasi SMOTE untuk handle class imbalance
- 🔄 Try advanced models: XGBoost, Neural Networks
- 🔄 Time-series analysis untuk prediksi viral trend
- 🔄 Natural Language Processing (NLP) pada video title & description

---

## 8. REFERENSI TEKNIS

### Libraries & Tools:
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-Learn** - Machine Learning
- **Matplotlib & Seaborn** - Data visualization
- **Python 3.14.4** - Programming language

### Reproducibility:
```bash
# Install dependencies
pip install -r requirements.txt

# Run analysis
python main.py

# Generate visualizations
python visualization.py
```

---

## 📎 ATTACHED OUTPUTS

1. ✅ `main.py` - Main analysis script
2. ✅ `visualization.py` - Visualization generator
3. ✅ `requirements.txt` - Dependencies list
4. ✅ `01_target_distribution.png` - Target variable breakdown
5. ✅ `02_feature_distribution.png` - Feature distributions
6. ✅ `03_feature_importance.png` - Feature importance plot
7. ✅ `04_confusion_matrix_metrics.png` - Model evaluation
8. ✅ `05_train_test_comparison.png` - Train vs test performance

---

**Tanggal Report**: April 23, 2026  
**Dataset**: clean_youtube_data.csv (40,848 records)  
**Model Accuracy**: 95.58% ✅

