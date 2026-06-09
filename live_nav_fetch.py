import os
import requests
import pandas as pd

RAW_DIR = 'data/raw'
os.makedirs(RAW_DIR, exist_ok=True)

print("=== STARTING LIVE NAV FETCH (Tasks 4 & 5) ===")

# Scheme mapping as specified in the tasks
schemes = {
    'HDFC_Top_100_Direct': '125497',
    'SBI_Bluechip': '119551',
    'ICICI_Bluechip': '120503',
    'Nippon_Large_Cap': '118632',
    'Axis_Bluechip': '119092',
    'Kotak_Bluechip': '120841'
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            if 'data' in json_data and len(json_data['data']) > 0:
                # Flatten the JSON list into a tabular dataframe
                df_live = pd.DataFrame(json_data['data'])
                df_live['amfi_code'] = code
                
                # Save to raw files
                output_path = os.path.join(RAW_DIR, f'{name}_nav.csv')
                df_live.to_csv(output_path, index=False)
                print(f"  ✓ Successfully fetched and saved: {name}_nav.csv")
            else:
                print(f"  ⚠ API returned empty array for {name}")
        else:
            print(f"  ❌ API failure for {name} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"  ❌ Error fetching {name}: {e}")

print("=== LIVE NAV FETCH COMPLETE ===\n")