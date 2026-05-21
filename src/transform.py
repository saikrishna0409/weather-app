import pandas as pd

def transform_data():
    print("Transforming data...")
    df = pd.read_csv('data/extracted_weather.csv')
    # Example transformation: convert temperature from F to C
    df['temperature_c'] = (df['temperature_f'] - 32) * 5.0/9.0
    df.to_csv('data/transformed_weather.csv', index=False)
    print("Data transformed and saved.")
