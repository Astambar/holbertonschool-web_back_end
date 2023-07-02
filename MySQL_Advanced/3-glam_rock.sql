-- Sélectionne le nom du groupe et calcule la durée de vie en années
SELECT band_name, 
       (YEAR(split) - YEAR(formed)) AS lifespan
FROM metal_bands
-- Filtre les groupes ayant le style principal "Glam rock"
WHERE style LIKE '%Glam rock%'
-- Trie les groupes par ordre décroissant de durée de vie
ORDER BY lifespan DESC;
