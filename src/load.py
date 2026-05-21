import pandas as pd

def load_data():
    print("Loading data...")
    df = pd.read_csv('data/transformed_weather.csv')
    # Example load: save to a database or final location
    df.to_csv('data/final_weather.csv', index=False)
    print("Data loaded successfully.")
