-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT band_name,
       CASE
           WHEN split IS NULL THEN YEAR(CURRENT_DATE()) - YEAR(formed)
           ELSE YEAR(split) - YEAR(formed)
       END AS lifespan
FROM bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
