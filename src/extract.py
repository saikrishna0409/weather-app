import pandas as pd

def extract_data():
    # Example: Read raw weather data from CSV
    print("Extracting data...")
    df = pd.read_csv('data/raw_weather.csv')
    # Save extracted data for next step
    df.to_csv('data/extracted_weather.csv', index=False)
    print("Data extracted and saved.")
