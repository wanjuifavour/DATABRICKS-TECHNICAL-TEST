-- Write a query that will display the results below (Note: some columns might be renamed
-- but use the column names above). It should only show 2020 data and order by driver
-- points.

SELECT race_year,
    driver_name,
    race_name,
    time,
    points
FROM races
WHERE race_year = 2020
ORDER BY points DESC;