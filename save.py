import pandas as pd

print("fetching data to save...")

import requests
all_hourly = []
all_daily = []

for year in range(1950, 2025):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 9.03,
        "longitude": 38.74,
        "start_date": f"{year}-01-01",
        "end_date": f"{year}-12-31",
        "hourly": ["temperature_2m", "rain"],
        "daily": ["temperature_2m_max", "temperature_2m_min", "rain_sum"],
        "timezone": "Africa/Addis_Ababa"
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'hourly' in data:
            hourly_df = pd.DataFrame(data['hourly'])
            daily_df = pd.DataFrame(data['daily'])
            hourly_df['time'] = pd.to_datetime(hourly_df['time'])
            daily_df['time'] = pd.to_datetime(daily_df['time'])
            hourly_df.set_index('time', inplace=True)
            daily_df.set_index('time', inplace=True)
            all_hourly.append(hourly_df)
            all_daily.append(daily_df)
            print(f"✓ {year}")

hourly_df = pd.concat(all_hourly)
daily_df = pd.concat(all_daily)

# Save to CSV (always works)
hourly_df.to_csv('addis_weather_1950_2024_hourly.csv')
daily_df.to_csv('addis_weather_1950_2024_daily.csv')

print(f"\n Saved {len(hourly_df):,} records!")