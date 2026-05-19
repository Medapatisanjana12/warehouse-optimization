-- Query 1
SELECT
    payment_type,
    AVG(total_amount) AS avg_amount
FROM trips
GROUP BY payment_type;

-- Query 2
SELECT
    toDate(tpep_pickup_datetime) AS trip_day,
    COUNT(*) AS total_trips
FROM trips
GROUP BY trip_day
ORDER BY trip_day;

-- Query 3
SELECT
    passenger_count,
    AVG(trip_distance) AS avg_distance
FROM trips
GROUP BY passenger_count;

-- Query 4
SELECT
    VendorID,
    SUM(total_amount) AS revenue
FROM trips
GROUP BY VendorID;

-- Query 5
SELECT
    toHour(tpep_pickup_datetime) AS hour,
    COUNT(*) AS trip_count
FROM trips
GROUP BY hour
ORDER BY hour;
