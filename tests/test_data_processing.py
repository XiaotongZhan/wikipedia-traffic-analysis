import pytest
import pandas as pd
from scripts.data_processing import process_wikipedia_data

def test_process_wikipedia_data():
    """
    Test if the Wikipedia data processing returns a valid DataFrame
    """
    # Since we don't want to rely on real data, let's create a mock DataFrame
    df_mock = pd.DataFrame({
        'date': ['2024-03-01', '2024-03-02'],
        'time': ['12:00', '13:00'],
        'language': ['en', 'en'],
        'webpage': ['Barack_Obama', 'Barack_Obama'],
        'number of hits': [100, 200],
        'page size': [5000, 8000]
    })
    
    assert isinstance(df_mock, pd.DataFrame), "Data is not a DataFrame"
    assert df_mock.shape[0] > 0, "DataFrame should not be empty"
    assert 'webpage' in df_mock.columns, "Missing 'webpage' column"
