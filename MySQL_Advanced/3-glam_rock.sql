-- Sélectionne le nom du groupe et calcule la durée de vie en années
SELECT band_name, 
       (YEAR(split) - YEAR(formed)) AS lifespan
FROM bands
-- Filtre les groupes ayant le style principal "Glam rock"
WHERE main_style = 'Glam rock'
-- Trie les groupes par ordre décroissant de durée de vie
ORDER BY lifespan DESC;
