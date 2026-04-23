import pandas as pd

print("Attempting to read CSV with different parameters...")

# Try 1: Default
try:
    df = pd.read_csv("clean_youtube_data.csv")
    print(f"✓ Success with default: {df.shape}")
except Exception as e:
    print(f"✗ Default failed: {type(e).__name__}")

# Try 2: With sep=','
try:
    df = pd.read_csv("clean_youtube_data.csv", sep=',', on_bad_lines='skip')
    print(f"✓ Success with sep=',': {df.shape}")
except Exception as e:
    print(f"✗ sep=',' failed: {type(e).__name__}")

# Try 3: With sep=';'
try:
    df = pd.read_csv("clean_youtube_data.csv", sep=';', on_bad_lines='skip')
    print(f"✓ Success with sep=';': {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nFirst row:\n{df.iloc[0]}")
except Exception as e:
    print(f"✗ sep=';' failed: {type(e).__name__}: {e}")

# Try 4: Check first line
try:
    with open("clean_youtube_data.csv", 'r', encoding='utf-8') as f:
        for i in range(5):
            print(f"Line {i+1}: {f.readline()[:100]}")
except Exception as e:
    print(f"Error reading first lines: {e}")
