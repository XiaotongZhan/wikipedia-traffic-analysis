import sqlite3
import pandas as pd

def create_database(db_path="wikipedia_traffic.db"):
    """
    Create SQLite database and table structure.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wikipedia_traffic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            time TEXT,
            language TEXT,
            webpage TEXT,
            number_of_hits INTEGER,
            page_size INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(df, db_path="wikipedia_traffic.db"):
    """
    Insert Pandas DataFrame data into SQLite database.
    """
    conn = sqlite3.connect(db_path)
    df.to_sql("wikipedia_traffic", conn, if_exists="append", index=False)
    conn.close()

def query_data(db_path="wikipedia_traffic.db"):
    """
    Query the database and return a Pandas DataFrame.
    """
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM wikipedia_traffic", conn)
    conn.close()
    return df

if __name__ == "__main__":
    create_database()
    df = pd.read_csv("./data/processed_wikipedia.csv")
    insert_data(df)
    result_df = query_data()
    print(result_df.head())
