import os
import glob
import pandas as pd

RAW_DIR = 'data/raw'

print("=== STARTING DATA INGESTION ANALYSIS (Task 3) ===")

# Find all CSV files inside data/raw
csv_files = glob.glob(os.path.join(RAW_DIR, '*.csv'))

if not csv_files:
    print("⚠ No CSV files found! Make sure your downloaded datasets are inside data/raw/")
else:
    for file_path in csv_files:
        file_name = os.path.basename(file_path)
        try:
            df = pd.read_csv(file_path)
            print(f"\n📁 Dataset: {file_name}")
            print(f"   Shape (Rows, Columns): {df.shape}")
            print("   Data Types:")
            for col, dtype in df.dtypes.items():
                print(f"     - {col}: {dtype}")
            print("   Head Preview:")
            print(df.head(2).to_string(index=False, justify='left'))
            print("-" * 50)
        except Exception as e:
            print(f"❌ Failed to read {file_name}: {e}")

print("\n=== FUND MASTER & VALIDATION SUMMARY (Tasks 6 & 7) ===")
# Updated paths to accurately track files with numeric prefixes
nav_path = os.path.join(RAW_DIR, '02_nav_history.csv')
master_path = os.path.join(RAW_DIR, '01_fund_master.csv')

if os.path.exists(nav_path) and os.path.exists(master_path):
    df_nav = pd.read_csv(nav_path)
    df_master = pd.read_csv(master_path)
    
    # Task 6: Explore Master Data structures
    print(f"Unique Fund Houses: {df_master['fund_house'].nunique() if 'fund_house' in df_master.columns else 'N/A'}")
    print(f"Unique Categories: {df_master['category'].unique() if 'category' in df_master.columns else 'N/A'}")
    
    # Dynamic parsing for risk profiles
    risk_col = 'risk_category' if 'risk_category' in df_master.columns else ('risk_grade' if 'risk_grade' in df_master.columns else None)
    if risk_col:
        print(f"Risk Profile Classifications: {df_master[risk_col].unique()}")
    
    # Task 7: Referential Integrity Validation Check
    master_codes = set(df_master['amfi_code'].unique())
    history_codes = set(df_nav['amfi_code'].unique())
    missing_codes = master_codes - history_codes
    
    if not missing_codes:
        print("\n✅ DATA QUALITY SUMMARY: Verification Pass! Every code in fund_master maps perfectly to nav_history.")
    else:
        print(f"\n⚠ DATA QUALITY SUMMARY: Validation Alert! {len(missing_codes)} AMFI codes in fund_master are missing history rows.")
else:
    print("⚠ Quality checks skipped. Ensure '02_nav_history.csv' and '01_fund_master.csv' are present in data/raw/")