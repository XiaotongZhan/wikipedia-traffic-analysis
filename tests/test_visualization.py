import pytest
import pandas as pd
import matplotlib.pyplot as plt
from scripts.visualization import plot_time_series

@pytest.fixture
def sample_dataframe():
    """
    Create a test DataFrame for plotting
    """
    return pd.DataFrame({
        'date': ['2024-03-01'],
        'time': ['12:00'],
        'language': ['en'],
        'webpage': ['Barack_Obama'],
        'number of hits': [100],
        'page size': [5000]
    })

def test_plot_time_series(sample_dataframe):
    """
    Tests that the plotting function works
    """
    try:
        plot_time_series(sample_dataframe)
        plt.close()  # Close the image to prevent it from affecting the test
    except Exception as e:
        pytest.fail(f"Plotting function raised an error: {e}")
