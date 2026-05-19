import time
import duckdb
import clickhouse_connect

# --------------------
# Connections
# --------------------

duck_conn = duckdb.connect("analytics.duckdb")

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='admin',
    password='admin123'
)

queries_duckdb = [

    """
    SELECT payment_type, AVG(total_amount)
    FROM trips
    GROUP BY payment_type
    """,

    """
    SELECT VendorID, SUM(total_amount)
    FROM trips
    GROUP BY VendorID
    """,

    """
    SELECT EXTRACT(HOUR FROM tpep_pickup_datetime) AS hour,
           COUNT(*)
    FROM trips
    GROUP BY hour
    """
]

queries_clickhouse = [

    """
    SELECT payment_type, AVG(total_amount)
    FROM trips
    GROUP BY payment_type
    """,

    """
    SELECT VendorID, SUM(total_amount)
    FROM trips
    GROUP BY VendorID
    """,

    """
    SELECT toHour(tpep_pickup_datetime) AS hour,
           COUNT(*)
    FROM trips
    GROUP BY hour
    """
]

print("\n===== DUCKDB =====")

for i, query in enumerate(queries_duckdb):

    start = time.time()

    duck_conn.execute(query).fetchall()

    end = time.time()

    print(f"Query {i+1}: {end-start:.4f} sec")

print("\n===== CLICKHOUSE =====")

for i, query in enumerate(queries_clickhouse):

    start = time.time()

    client.query(query)

    end = time.time()

    print(f"Query {i+1}: {end-start:.4f} sec")
