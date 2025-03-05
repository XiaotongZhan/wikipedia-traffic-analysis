# Wikipedia Traffic Analysis with Dask & SQLite

## Overview
This project analyzes Wikipedia traffic data using **Dask** for parallel processing and **SQLite** for structured storage. The analysis focuses on web traffic to pages related to *Barack Obama*.

## Features
- Efficient **parallel data processing** with **Dask**
- **Filtering and cleaning** Wikipedia traffic logs
- **Time series visualization** of traffic trends
- **Storing & querying** processed data with **SQLite**

## Project Structure
```
📁 wikipedia-traffic-analysis
│── 📂 data/                 # Raw & processed datasets
│── 📂 scripts/              # Python scripts
│    ├── data_processing.py  # Dask-based data processing
│    ├── visualization.py    # Data visualization
│    ├── database_manager.py # SQLite database operations
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
│── setup.py                 # Optional package setup
```

## Installation
First, clone the repository:
```bash
git clone https://github.com/your-username/wikipedia-traffic-analysis.git
cd wikipedia-traffic-analysis
```
Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
### 1️⃣ **Process Wikipedia Traffic Data**
```python
from scripts.data_processing import process_wikipedia_data

df = process_wikipedia_data("./data")
print(df.head())
```

### 2️⃣ **Store Data in SQLite**
```python
from scripts.database_manager import create_database, insert_data

create_database()
insert_data(df)
```

### 3️⃣ **Query Data from SQLite**
```python
from scripts.database_manager import query_data

result_df = query_data()
print(result_df.head())
```

### 4️⃣ **Visualize Data**
```python
from scripts.visualization import plot_time_series

plot_time_series(df)
```

## Running Tests
To verify correctness:
```bash
pytest tests/
```

## License
This project is licensed under the MIT License.

---

Now your **GitHub repository** will be **clean, structured, and professional!** 🚀

