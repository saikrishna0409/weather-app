import pandas as pd
from src.transform import transform_data
import os

def test_transform_data():
    # Prepare test data
    test_input = pd.DataFrame({
        'temperature_f': [32, 212],
    })
    test_input.to_csv('data/extracted_weather.csv', index=False)

    # Run transform
    transform_data()

    # Check output
    result = pd.read_csv('data/transformed_weather.csv')
    assert 'temperature_c' in result.columns
    assert abs(result.loc[0, 'temperature_c'] - 0) < 0.01
    assert abs(result.loc[1, 'temperature_c'] - 100) < 0.01

    # Clean up
    os.remove('data/extracted_weather.csv')
    os.remove('data/transformed_weather.csv')
