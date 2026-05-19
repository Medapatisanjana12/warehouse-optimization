CREATE TABLE trips_optimized
(
    VendorID UInt8,
    tpep_pickup_datetime DateTime,
    tpep_dropoff_datetime DateTime,
    passenger_count Float32,
    trip_distance Float32,
    fare_amount Float32,
    total_amount Float32,
    payment_type UInt8
)
ENGINE = MergeTree()

PARTITION BY toYYYYMM(tpep_pickup_datetime)

ORDER BY (
    tpep_pickup_datetime,
    VendorID,
    payment_type
);
