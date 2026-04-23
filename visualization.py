import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

print("Loading and processing data...")

# Load data
df = pd.read_csv("clean_youtube_data.csv", sep=';', encoding='latin1', on_bad_lines='skip', low_memory=False)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Prepare data
feature_cols = ['likes', 'comment_count', 'category_id']
required_cols = feature_cols + ['viral']
df_clean = df[required_cols].dropna()

for col in feature_cols:
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
df_clean = df_clean.dropna()
df_clean['viral'] = df_clean['viral'].astype(int)

X = df_clean[feature_cols]
y = df_clean['viral']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)
y_pred_test = model.predict(X_test_scaled)

print("Creating visualizations...")

# ===== FIGURE 1: Distribution Target Variable =====
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Pie chart
viral_counts = y.value_counts()
colors = ['#FF6B6B', '#4ECDC4']
axes[0].pie(viral_counts.values, labels=['Viral (1)', 'Non-Viral (0)'], autopct='%1.1f%%', 
            colors=colors, startangle=90, textprops={'fontsize': 12, 'weight': 'bold'})
axes[0].set_title('Distribusi Target Variable (Viral vs Non-Viral)', fontsize=14, weight='bold', pad=20)

# Bar chart
viral_counts.plot(kind='bar', ax=axes[1], color=colors, edgecolor='black', linewidth=1.5)
axes[1].set_title('Jumlah Video Viral vs Non-Viral', fontsize=14, weight='bold', pad=20)
axes[1].set_xlabel('Status Viral', fontsize=11)
axes[1].set_ylabel('Jumlah Video', fontsize=11)
axes[1].set_xticklabels(['Non-Viral (0)', 'Viral (1)'], rotation=0)
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('01_target_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 01_target_distribution.png")
plt.close()

# ===== FIGURE 2: Feature Distribution =====
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Likes distribution
axes[0, 0].hist(df_clean['likes'], bins=50, color='#3498db', edgecolor='black', alpha=0.7)
axes[0, 0].set_xlabel('Likes', fontsize=11)
axes[0, 0].set_ylabel('Frequency', fontsize=11)
axes[0, 0].set_title('Distribusi Likes', fontsize=12, weight='bold')
axes[0, 0].set_xlim(0, df_clean['likes'].quantile(0.99))
axes[0, 0].grid(alpha=0.3)

# Comments distribution
axes[0, 1].hist(df_clean['comment_count'], bins=50, color='#2ecc71', edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('Comment Count', fontsize=11)
axes[0, 1].set_ylabel('Frequency', fontsize=11)
axes[0, 1].set_title('Distribusi Comment Count', fontsize=12, weight='bold')
axes[0, 1].set_xlim(0, df_clean['comment_count'].quantile(0.99))
axes[0, 1].grid(alpha=0.3)

# Category distribution
category_counts = df_clean['category_id'].value_counts().head(10)
axes[1, 0].barh(range(len(category_counts)), category_counts.values, color='#e74c3c', edgecolor='black')
axes[1, 0].set_yticks(range(len(category_counts)))
axes[1, 0].set_yticklabels([f'Category {cid}' for cid in category_counts.index])
axes[1, 0].set_xlabel('Jumlah Video', fontsize=11)
axes[1, 0].set_title('Top 10 Kategori Video', fontsize=12, weight='bold')
axes[1, 0].grid(axis='x', alpha=0.3)

# Box plot by viral status
df_clean.boxplot(column='likes', by='viral', ax=axes[1, 1])
axes[1, 1].set_xlabel('Status Viral', fontsize=11)
axes[1, 1].set_ylabel('Likes', fontsize=11)
axes[1, 1].set_title('Likes Distribution by Viral Status', fontsize=12, weight='bold')
axes[1, 1].set_xticklabels(['Non-Viral', 'Viral'])
plt.suptitle('')

plt.tight_layout()
plt.savefig('02_feature_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 02_feature_distribution.png")
plt.close()

# ===== FIGURE 3: Feature Importance =====
fig, ax = plt.subplots(figsize=(10, 6))

feature_importance = pd.DataFrame({
    'Feature': feature_cols,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

colors_importance = ['#f39c12', '#3498db', '#2ecc71']
bars = ax.barh(feature_importance['Feature'], feature_importance['Importance'], color=colors_importance, edgecolor='black', linewidth=1.5)

# Add percentage labels
for i, (idx, row) in enumerate(feature_importance.iterrows()):
    ax.text(row['Importance'] + 0.01, i, f"{row['Importance']*100:.2f}%", va='center', fontsize=11, weight='bold')

ax.set_xlabel('Importance Score', fontsize=12, weight='bold')
ax.set_title('Feature Importance dalam Prediksi Video Viral', fontsize=14, weight='bold', pad=20)
ax.set_xlim(0, max(feature_importance['Importance']) * 1.15)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('03_feature_importance.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 03_feature_importance.png")
plt.close()

# ===== FIGURE 4: Confusion Matrix & Performance Metrics =====
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_test)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0], 
            xticklabels=['Non-Viral', 'Viral'], yticklabels=['Non-Viral', 'Viral'],
            cbar_kws={'label': 'Count'}, annot_kws={'size': 12, 'weight': 'bold'})
axes[0].set_title('Confusion Matrix (Test Set)', fontsize=14, weight='bold', pad=20)
axes[0].set_ylabel('Actual', fontsize=11, weight='bold')
axes[0].set_xlabel('Predicted', fontsize=11, weight='bold')

# Performance Metrics Bar Chart
metrics_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
metrics_values = [
    accuracy_score(y_test, y_pred_test),
    precision_score(y_test, y_pred_test),
    recall_score(y_test, y_pred_test),
    f1_score(y_test, y_pred_test)
]

colors_metrics = ['#e74c3c', '#f39c12', '#2ecc71', '#3498db']
bars = axes[1].bar(metrics_names, metrics_values, color=colors_metrics, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bar, val in zip(bars, metrics_values):
    height = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.4f}', ha='center', va='bottom', fontsize=12, weight='bold')

axes[1].set_ylabel('Score', fontsize=11, weight='bold')
axes[1].set_title('Model Performance Metrics', fontsize=14, weight='bold', pad=20)
axes[1].set_ylim(0, 1.1)
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('04_confusion_matrix_metrics.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 04_confusion_matrix_metrics.png")
plt.close()

# ===== FIGURE 5: Model Comparison (Train vs Test) =====
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_pred_train = model.predict(X_train_scaled)

metrics = {
    'Accuracy': [
        accuracy_score(y_train, y_pred_train),
        accuracy_score(y_test, y_pred_test)
    ],
    'Precision': [
        precision_score(y_train, y_pred_train),
        precision_score(y_test, y_pred_test)
    ],
    'Recall': [
        recall_score(y_train, y_pred_train),
        recall_score(y_test, y_pred_test)
    ],
    'F1-Score': [
        f1_score(y_train, y_pred_train),
        f1_score(y_test, y_pred_test)
    ]
}

fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(metrics))
width = 0.35

train_values = [metrics[m][0] for m in metrics]
test_values = [metrics[m][1] for m in metrics]

bars1 = ax.bar(x - width/2, train_values, width, label='Training Set', color='#3498db', edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, test_values, width, label='Testing Set', color='#2ecc71', edgecolor='black', linewidth=1.5)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.4f}', ha='center', va='bottom', fontsize=10, weight='bold')

ax.set_ylabel('Score', fontsize=12, weight='bold')
ax.set_title('Perbandingan Performa Model: Training vs Testing Set', fontsize=14, weight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(metrics.keys())
ax.set_ylim(0, 1.1)
ax.legend(fontsize=11, loc='lower right')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('05_train_test_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Saved: 05_train_test_comparison.png")
plt.close()

print("\n✓ Semua visualisasi berhasil dibuat!")
print("\nFile yang dihasilkan:")
print("  1. 01_target_distribution.png")
print("  2. 02_feature_distribution.png")
print("  3. 03_feature_importance.png")
print("  4. 04_confusion_matrix_metrics.png")
print("  5. 05_train_test_comparison.png")
