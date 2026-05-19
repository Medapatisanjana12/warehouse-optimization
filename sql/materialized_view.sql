CREATE MATERIALIZED VIEW mv_daily_revenue
ENGINE = SummingMergeTree()

PARTITION BY trip_day

ORDER BY trip_day

AS

SELECT
    toDate(tpep_pickup_datetime) AS trip_day,
    SUM(total_amount) AS revenue
FROM trips_optimized
GROUP BY trip_day;
