import duckdb
import pandas as pd
import clickhouse_connect
from pathlib import Path

# -------------------------
# Connect DuckDB
# -------------------------

duck_conn = duckdb.connect("analytics.duckdb")

# -------------------------
# Connect ClickHouse
# -------------------------

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='admin',
    password='admin123'
)

# -------------------------
# Create Tables
# -------------------------

create_table_query = """
CREATE TABLE IF NOT EXISTS trips (
    VendorID UInt8,
    tpep_pickup_datetime TIMESTAMP,
    tpep_dropoff_datetime TIMESTAMP,
    passenger_count Float,
    trip_distance Float,
    fare_amount Float,
    total_amount Float,
    payment_type INTEGER
)
ENGINE = MergeTree()
ORDER BY tpep_pickup_datetime
"""

client.command(create_table_query)

duck_conn.execute("""
CREATE TABLE IF NOT EXISTS trips (
    VendorID INTEGER,
    tpep_pickup_datetime TIMESTAMP,
    tpep_dropoff_datetime TIMESTAMP,
    passenger_count FLOAT,
    trip_distance FLOAT,
    fare_amount FLOAT,
    total_amount FLOAT,
    payment_type INTEGER
)
""")
# -------------------------
# Load Data
# -------------------------

files = Path("data").glob("*.parquet")

for file in files:
    print(f"Loading {file}")

    df = pd.read_parquet(file)

    needed_cols = [
        'VendorID',
        'tpep_pickup_datetime',
        'tpep_dropoff_datetime',
        'passenger_count',
        'trip_distance',
        'fare_amount',
        'total_amount',
        'payment_type'
    ]

    df = df[needed_cols]

    # DuckDB
    duck_conn.register("temp_df", df)
    duck_conn.execute("INSERT INTO trips SELECT * FROM temp_df")

    # ClickHouse
    client.insert_df("trips", df)

print("Data Loaded Successfully")
