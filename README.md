# 🎬 YouTube Video Viral Prediction using Machine Learning

Proyek machine learning untuk **memprediksi apakah sebuah video YouTube akan viral atau tidak** menggunakan dataset trending videos dan algoritma Random Forest.

---

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Requirements](#requirements)
- [Installation](#installation)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Model Performance](#model-performance)
- [Feature Importance](#feature-importance)
- [Insights & Recommendations](#insights--recommendations)
- [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start

```bash
# 1. Navigate to project directory
cd c:\Users\User\Documents\pythonku

# 2. Activate virtual environment
venv\Scripts\activate.bat

# 3. Run analysis
python main.py

# 4. Generate visualizations
python visualization.py
```

---

## 📦 Requirements

- **Python**: 3.14.4 or higher
- **OS**: Windows 10/11 (PowerShell/CMD)
- **Disk Space**: ~2 GB (including venv)
- **RAM**: Minimum 2GB recommended
- **Dataset**: `clean_youtube_data.csv` (48,697 records)

---

## 🔧 Installation

### Step 1: Clone/Download Project

```bash
# Download to your local machine
cd c:\Users\User\Documents
# Extract or clone project files
```

### Step 2: Verify Project Structure

```
pythonku/
├── main.py                          # Main analysis script
├── visualization.py                 # Visualization generator
├── clean_youtube_data.csv           # Dataset (48,697 records)
├── requirements.txt                 # Dependencies list
├── LAPORAN.md                       # Full report
├── PANDUAN_PRESENTASI.md            # Presentation guide
├── README.md                        # This file
├── venv/                            # Virtual environment
└── output/                          # Generated visualizations
    ├── 01_target_distribution.png
    ├── 02_feature_distribution.png
    ├── 03_feature_importance.png
    ├── 04_confusion_matrix_metrics.png
    └── 05_train_test_comparison.png
```

---

## 🌐 Virtual Environment Setup

### Option 1: Windows CMD

```batch
# Navigate to project directory
cd c:\Users\User\Documents\pythonku

# Create virtual environment (if not exists)
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# You should see (venv) in your prompt
# (venv) C:\Users\User\Documents\pythonku>
```

### Option 2: Windows PowerShell

```powershell
# Navigate to project directory
cd c:\Users\User\Documents\pythonku

# Create virtual environment (if not exists)
python -m venv venv

# Activate virtual environment (with bypass for execution policy)
& .\venv\Scripts\Activate.ps1

# If you get execution policy error, use:
powershell -ExecutionPolicy Bypass -Command "& {.\venv\Scripts\Activate.ps1}"
```

### Option 3: Using Batch File (Easiest)

Create file `activate.bat`:
```batch
@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
cmd /k
```

Then double-click `activate.bat` to open terminal with venv activated.

### Verify Activation

```bash
# Should show virtual environment path
python --version
# Output: Python 3.14.4

# Should show venv path (not system python)
where python
# Output: c:\Users\User\Documents\pythonku\venv\Scripts\python.exe
```

### Deactivate Virtual Environment

```bash
deactivate

# Prompt returns to normal (no venv prefix)
```

---

## 📚 Dependencies

### Core Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| **pandas** | 2.2.0 | Data manipulation & analysis |
| **numpy** | 2.4.4 | Numerical computing |
| **scikit-learn** | 1.8.0 | Machine learning algorithms |
| **scipy** | 1.17.1 | Scientific computing |
| **matplotlib** | 3.8.0 | Data visualization |
| **seaborn** | 0.13.0 | Statistical visualization |
| **joblib** | 1.5.3 | Parallel processing |

### Installation

#### Option 1: Install from requirements.txt (Recommended)

```bash
# Activate venv first
venv\Scripts\activate.bat

# Install all dependencies at once
pip install -r requirements.txt
```

#### Option 2: Install Individual Packages

```bash
# Activate venv
venv\Scripts\activate.bat

# Install dependencies one by one
pip install pandas==2.2.0
pip install numpy==2.4.4
pip install scikit-learn==1.8.0
pip install matplotlib==3.8.0
pip install seaborn==0.13.0
pip install scipy==1.17.1
```

#### Option 3: Install Latest Versions

```bash
# Activate venv
venv\Scripts\activate.bat

# Install latest compatible versions
pip install pandas numpy scikit-learn matplotlib seaborn scipy
```

### Verify Installation

```bash
# Check if all packages installed
python -c "import pandas, numpy, sklearn, matplotlib, seaborn; print('✓ All packages installed!')"

# Check specific versions
python -c "import pandas as pd; print(f'pandas: {pd.__version__}')"
python -c "import numpy as np; print(f'numpy: {np.__version__}')"
python -c "import sklearn; print(f'scikit-learn: {sklearn.__version__}')"
```

---

## 💻 Usage

### Running Main Analysis

```bash
# Make sure venv is activated
venv\Scripts\activate.bat

# Run analysis script
python main.py
```

**Expected Output:**
```
======================================================================
YOUTUBE DATA ANALYSIS & VIRAL VIDEO PREDICTION
======================================================================

[1] Loading data dari clean_youtube_data.csv...
Dataset shape: (48697, 128)
Jumlah baris: 48697
Jumlah kolom: 128
...
[7] Evaluasi Model...
Accuracy:  0.9558
Precision: 0.9710
Recall:    0.9785
F1-Score:  0.9747
✓ ANALISIS SELESAI!
```

**Time to Complete**: ~2-3 minutes

### Generating Visualizations

```bash
# Make sure venv is activated
venv\Scripts\activate.bat

# Generate visualization plots
python visualization.py
```

**Expected Output:**
```
Loading and processing data...
Creating visualizations...
✓ Saved: 01_target_distribution.png
✓ Saved: 02_feature_distribution.png
✓ Saved: 03_feature_importance.png
✓ Saved: 04_confusion_matrix_metrics.png
✓ Saved: 05_train_test_comparison.png

✓ Semua visualisasi berhasil dibuat!
```

**Time to Complete**: ~30-60 seconds

### Running Both Scripts

```bash
# Sequential execution
python main.py && python visualization.py

# With output to file
python main.py > output_main.txt 2>&1
python visualization.py > output_viz.txt 2>&1
```

---

## 📊 Analyzing Results

### Step 1: Understand Data

```python
# See what main.py prints:
# - Dataset shape: 48,697 videos with 128 features
# - Valid data: 40,848 after cleaning
# - Target distribution: 86.99% viral, 13.01% non-viral
```

**Key Metrics**:
- Total videos analyzed: **40,848**
- Training set: **32,678 (80%)**
- Testing set: **8,170 (20%)**

### Step 2: Review Model Performance

From `main.py` output:
```
TEST SET PERFORMANCE:
- Accuracy:  95.58%  ✓ (95.58% predictions correct)
- Precision: 97.10%  ✓ (97.10% of viral predictions correct)
- Recall:    97.85%  ✓ (97.85% of actual viral videos detected)
- F1-Score:  97.47%  ✓ (balanced metric)
```

### Step 3: Analyze Feature Importance

From `main.py` output:
```
FEATURE IMPORTANCE:
Feature          Importance    Percentage
────────────────────────────────────────
likes            0.524740      52.47%  🥇
comment_count    0.415248      41.53%  🥈
category_id      0.060013      6.00%   🥉
```

**Interpretation**:
- **Likes** is the DOMINANT predictor (52%)
- **Comments** is also very important (41%)
- **Category** has minimal effect (6%)
- **Engagement metrics** = 94% total importance

### Step 4: Review Confusion Matrix

From `main.py` output:
```
CONFUSION MATRIX:
              Predicted
            Non-V  Viral
Actual Non-V  854    208
       Viral  153  6,955

Metrics:
- True Negatives (TN):    854  (correctly identified non-viral)
- False Positives (FP):   208  (non-viral but predicted viral)
- False Negatives (FN):   153  (viral but predicted non-viral)
- True Positives (TP):  6,955  (correctly identified viral)
```

---

## 📈 Results

### Visualization Outputs

Run `python visualization.py` to generate 5 key visualizations:

#### 1️⃣ Target Distribution (01_target_distribution.png)

Shows breakdown of viral vs non-viral videos:
- **Pie Chart**: 86.99% viral (green), 13.01% non-viral (red)
- **Bar Chart**: Absolute counts

📊 **Insight**: Dataset heavily skewed toward viral videos, but model handles this well.

```
[PIE CHART VISUALIZATION]
Viral (1):      35,536 videos (86.99%)
Non-Viral (0):   5,312 videos (13.01%)
```

#### 2️⃣ Feature Distributions (02_feature_distribution.png)

Four subplots showing feature statistics:

**A. Likes Histogram**
- Distribution: Right-skewed
- Mean: 74,386 | Median: 18,098
- Range: 0 to 5,613,827

**B. Comments Histogram**
- Distribution: Right-skewed
- Mean: 8,459 | Median: 1,855
- Range: 0 to 1,361,580

**C. Top 10 Categories (Bar Chart)**
- Category 25 (Entertainment): Most popular
- Categories 1-43 total
- Fairly balanced distribution

**D. Likes by Viral Status (Box Plot)**
- Viral videos: Significantly higher likes
- Clear separation indicates good predictor

📊 **Insight**: Viral videos have substantially more engagement (likes/comments).

#### 3️⃣ Feature Importance (03_feature_importance.png)

Horizontal bar chart showing:
```
Likes:           52.47% ████████████████████████
Comments:        41.53% ████████████████████
Category:         6.00% ███
```

📊 **Insight**: Engagement metrics (likes+comments) = 94% importance.

#### 4️⃣ Model Performance (04_confusion_matrix_metrics.png)

Two subplots:

**A. Confusion Matrix Heatmap**
```
                Predicted
              Non-V   Viral
Actual Non-V  854     208
       Viral  153    6955
```

**B. Performance Metrics Bar Chart**
```
Accuracy:   95.58% ████████████████████
Precision:  97.10% ████████████████████
Recall:     97.85% ████████████████████
F1-Score:   97.47% ████████████████████
```

📊 **Insight**: Model EXCELLENT across all metrics.

#### 5️⃣ Train vs Test Comparison (05_train_test_comparison.png)

Comparison of model performance on training vs testing data:

```
              Training  Testing   Gap
─────────────────────────────────────
Accuracy      99.96%    95.58%   -4.38%
Precision     99.96%    97.10%   -2.86%
Recall        100.00%   97.85%   -2.15%
F1-Score      99.98%    97.47%   -2.51%
```

📊 **Insight**: Small gap indicates good generalization (minimal overfitting).

---

## 🏆 Model Performance Summary

### Overall Scores

| Metric | Score | Interpretation |
|--------|-------|-----------------|
| **Accuracy** | 95.58% | 95 out of 100 predictions correct |
| **Precision** | 97.10% | 97 out of 100 viral predictions correct |
| **Recall** | 97.85% | Catches 98% of actual viral videos |
| **F1-Score** | 97.47% | Balanced performance metric |

### Classification Report

```
              Precision    Recall  F1-Score   Support
─────────────────────────────────────────────────
Not Viral        0.85      0.80      0.83      1,062
    Viral        0.97      0.98      0.97      7,108
─────────────────────────────────────────────
 Accuracy                           0.96      8,170
 Macro Avg       0.91      0.89      0.90      8,170
Weighted Avg     0.95      0.96      0.96      8,170
```

### Model Conclusion

✅ **Model is PRODUCTION READY**
- Exceeds 90% accuracy target ✓
- Exceeds 95% precision target ✓
- No severe overfitting ✓
- Generalizes well to unseen data ✓

---

## 🔍 Feature Importance Analysis

### Ranking

| Rank | Feature | Importance | Category |
|------|---------|------------|----------|
| 🥇 1st | Likes | 52.47% | Engagement |
| 🥈 2nd | Comment Count | 41.53% | Engagement |
| 🥉 3rd | Category ID | 6.00% | Metadata |

### Interpretation

**Likes (52.47% importance)**
- Most critical factor for predicting viral status
- Reflects viewer satisfaction & interest
- Strong correlation with viral potential

**Comments (41.53% importance)**
- Second most important predictor
- Indicates audience engagement & discussion
- Complementary to likes metric

**Category (6.00% importance)**
- Minimal influence on viral prediction
- Video quality/content matters more than genre
- All categories can potentially go viral

### Key Takeaway

🎯 **ENGAGEMENT IS EVERYTHING**
- Engagement metrics = 94% total importance
- Content quality > Genre/Category selection
- Focus on maximizing likes & comments

---

## 💡 Insights & Recommendations

### For Content Creators

1. **Maximize Engagement**
   - Encourage viewers to LIKE videos
   - Ask for comments in video
   - Respond to comments (boost engagement)
   - Use engaging thumbnails & titles

2. **Quality Over Category**
   - Don't choose category based on trends
   - Focus on HIGH-QUALITY content
   - Better: Excellent video in any genre
   - vs.: Mediocre video in trending genre

3. **Create Engagement Loop**
   - Quality content → More views
   - More views → More recommendations
   - More recommendations → More viral
   - Positive feedback loop ✓

### For Platform (YouTube)

- Model confirms engagement-based ranking
- Can identify viral videos early
- Optimize recommendation algorithm
- Support new creators with insights

### Future Improvements

- Add more features (duration, publish time)
- Implement class balancing (SMOTE)
- Try advanced models (XGBoost, Neural Networks)
- NLP analysis of titles & descriptions
- Time-series viral trend prediction

---

## 🔧 Troubleshooting

### Issue 1: Virtual Environment Not Found

```
Error: Cannot find file venv\Scripts\activate.bat
```

**Solution**:
```bash
# Create virtual environment
python -m venv venv

# Then activate
venv\Scripts\activate.bat
```

### Issue 2: Module Not Found (pandas, sklearn, etc.)

```
ModuleNotFoundError: No module named 'sklearn'
```

**Solution**:
```bash
# Make sure venv is activated
venv\Scripts\activate.bat

# Install requirements
pip install -r requirements.txt

# Or install individual package
pip install scikit-learn
```

### Issue 3: Python Version Mismatch

```
Error: Python 3.14.4 required, but 3.9.0 installed
```

**Solution**:
```bash
# Check current Python version
python --version

# If using different version, update venv
python -m venv venv --upgrade

# Or install newer Python globally
# Then create new venv
```

### Issue 4: CSV File Not Found

```
FileNotFoundError: clean_youtube_data.csv not found
```

**Solution**:
- Ensure `clean_youtube_data.csv` in project root
- Check file path in `main.py` line 16
- Use absolute path if needed:
  ```python
  df = pd.read_csv(r"c:\Users\User\Documents\pythonku\clean_youtube_data.csv")
  ```

### Issue 5: Execution Policy Error (PowerShell)

```
File cannot be loaded because running scripts is disabled on this system
```

**Solution**:
```powershell
# Use bypass flag
powershell -ExecutionPolicy Bypass -Command "& {.\venv\Scripts\Activate.ps1}"

# Or use CMD instead
cmd
venv\Scripts\activate.bat
```

### Issue 6: Out of Memory Error

```
MemoryError: Unable to allocate X.XX GiB
```

**Solution**:
- Use sample of data instead
- Reduce `n_estimators` in Random Forest
- Close other applications
- Upgrade RAM

### Issue 7: Slow Performance

**Optimize**:
```bash
# Reduce n_estimators in visualization.py (line ~100)
# Change: n_estimators=100
# To: n_estimators=50

# Or run without parallel processing
# Change: n_jobs=-1
# To: n_jobs=1
```

---

## 📚 Additional Resources

### Project Files

- **[LAPORAN.md](LAPORAN.md)** - Full technical report
- **[PANDUAN_PRESENTASI.md](PANDUAN_PRESENTASI.md)** - Complete presentation guide
- **[main.py](main.py)** - Main analysis source code
- **[visualization.py](visualization.py)** - Visualization source code

### External References

- [Scikit-Learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [YouTube API Docs](https://developers.google.com/youtube/v3)

### Dataset Info

- **Source**: YouTube Trending Videos Dataset (2017-2019)
- **Records**: 48,697 videos
- **Valid Records**: 40,848 after cleaning
- **Features**: 128 original features → 3 engineered features

---

## 📝 Quick Reference

### Common Commands

```bash
# Activate environment
venv\Scripts\activate.bat

# Deactivate environment
deactivate

# Install dependencies
pip install -r requirements.txt

# Run analysis
python main.py

# Generate visualizations
python visualization.py

# Check installed packages
pip list

# Update package
pip install --upgrade package_name

# Remove old venv and create new
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### File Locations

```
Project Root: c:\Users\User\Documents\pythonku\

Key Files:
├── Python Scripts:
│  ├── main.py
│  ├── visualization.py
│  
├── Data:
│  └── clean_youtube_data.csv
│
├── Documentation:
│  ├── README.md (this file)
│  ├── LAPORAN.md
│  ├── PANDUAN_PRESENTASI.md
│  └── requirements.txt
│
├── Virtual Environment:
│  └── venv/
│     └── Scripts/
│        ├── activate.bat
│        ├── python.exe
│        └── pip.exe
│
└── Outputs:
   ├── 01_target_distribution.png
   ├── 02_feature_distribution.png
   ├── 03_feature_importance.png
   ├── 04_confusion_matrix_metrics.png
   └── 05_train_test_comparison.png
```

---

## ✅ Verification Checklist

Before running project, verify:

- [ ] Python 3.14.4+ installed
- [ ] Virtual environment created (`venv/` folder exists)
- [ ] Dependencies installed (`pip list` shows all packages)
- [ ] Dataset present (`clean_youtube_data.csv` exists)
- [ ] Can activate venv (no errors)
- [ ] Can run `python main.py` (completes in 2-3 min)
- [ ] Can run `python visualization.py` (generates 5 PNG files)

---

## 🎓 Learning Outcomes

After running this project, you will understand:

✅ How to set up Python virtual environments
✅ Data preprocessing & feature engineering
✅ Train-test split & feature scaling
✅ Random Forest classifier implementation
✅ Model evaluation metrics (accuracy, precision, recall, F1)
✅ Feature importance analysis
✅ How to create data visualizations with Matplotlib & Seaborn
✅ Real-world machine learning workflow

---

## 📞 Support

For issues or questions:

1. Check **[Troubleshooting](#troubleshooting)** section
2. Review **[LAPORAN.md](LAPORAN.md)** for detailed analysis
3. Check script comments in **[main.py](main.py)**
4. Review **[PANDUAN_PRESENTASI.md](PANDUAN_PRESENTASI.md)** for context

---

## 📄 License & Attribution

**Dataset**: YouTube Trending Videos Dataset (2017-2019)  
**Analysis**: Machine Learning Project  
**Date**: April 23, 2026

---

**Last Updated**: April 23, 2026  
**Status**: ✅ Complete & Production Ready

