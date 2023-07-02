-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin AS country,
       COUNT(*) AS fan_count
FROM bands
WHERE main_style = 'Glam rock'
GROUP BY origin
ORDER BY fan_count DESC;
