import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series(df):
    """
    Plot time series of Wikipedia access traffic.
    """
    df['timestamp'] = pd.to_datetime(df['date'] + ' ' + df['time'], utc=True)
    df['number of hits'] = df['number of hits'].astype(int)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['number of hits'], marker='o', linestyle='-', label='Wikipedia Hits')
    plt.xlabel("Time")
    plt.ylabel("Number of Hits")
    plt.title("Wikipedia Traffic for 'Barack Obama'")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    
    plt.show()
    
if __name__ == "__main__":
    df = pd.read_csv("./data/processed_wikipedia.csv")
    plot_time_series(df)
