SELECT band_name,
       CASE
           WHEN split IS NULL THEN YEAR(CURRENT_DATE()) - YEAR(formed)
           ELSE YEAR(split) - YEAR(formed)
       END AS lifespan
FROM bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
