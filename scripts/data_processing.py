import dask
from dask import delayed
import re
import pandas as pd
import glob
import gzip

dask.config.set(scheduler='processes', num_workers=8)

# Regular expression to match pages related to "Barack_Obama"
pattern = re.compile(r'^\S+\s+\S+\s+\S+\s+\S*Barack_Obama\S*')

@delayed
def read_and_filter_with_regex(filename):
    """
    Reads a compressed Wikipedia traffic data file and filters lines containing "Barack_Obama".
    """
    matched_rows = []
    with gzip.open(filename, 'rt', encoding='utf-8') as f: 
        for line in f:
            if pattern.match(line):  
                matched_rows.append(line.strip().split())
    return pd.DataFrame(matched_rows)

def process_wikipedia_data(data_path):
    """
    Reads all Wikipedia data files, filters relevant data, and returns a DataFrame.
    """
    file_list = glob.glob(f'{data_path}/*.gz')
    tasks = [read_and_filter_with_regex(f) for f in file_list]
    results = dask.compute(*tasks, scheduler='threads')
    
    df_column_names = ['date', 'time', 'language', 'webpage', 'number of hits', 'page size']
    df = pd.concat(results, ignore_index=True)
    df.columns = df_column_names
    
    return df

if __name__ == "__main__":
    data_path = "./data"  # Path to the data files
    df = process_wikipedia_data(data_path)
    print(df.head())
    print(f"Total records: {df.shape[0]}")