import pytest
import pandas as pd
from scripts.database_manager import create_database, insert_data, query_data

@pytest.fixture
def sample_dataframe():
    """
    Create a test DataFrame for database testing
    """
    return pd.DataFrame({
        'date': ['2024-03-01'],
        'time': ['12:00'],
        'language': ['en'],
        'webpage': ['Barack_Obama'],
        'number_of_hits': [100],
        'page_size': [5000]
    })

def test_create_database():
    """
    Test that the SQLite database was created successfully
    """
    create_database()
    df = query_data()
    assert isinstance(df, pd.DataFrame), "Query did not return a DataFrame"

def test_insert_and_query_data(sample_dataframe):
    """
    Test data insertion and query functionality
    """
    insert_data(sample_dataframe)
    df = query_data()
    assert df.shape[0] > 0, "Database query returned empty DataFrame"
    assert 'webpage' in df.columns, "Missing 'webpage' column in database"
