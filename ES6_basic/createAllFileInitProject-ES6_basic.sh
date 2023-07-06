#!/bin/bash

# Liste des fichiers à créer (un fichier par ligne)
fichiers=(
    "0-constants.js"
    "1-block-scoped.js"
    "2-arrow.js"
    "2-main.js"
    "3-default-parameter.js"
    "3-main.js"
    "4-rest-parameter.js"
	"5-spread-operator.js"
	"6-string-interpolation.js"
	"7-getBudgetObject.js"
	"8-getBudgetCurrentYear.js"
	"9-getFullBudget.js"
	"10-loops.js"
	"11-createEmployeesObject.js"
	"12-createReportObject.js"
	"100-createIteratorObject.js"
	"101-iterateThroughObject.js"
)

# Fonction pour extraire le numéro du nom de fichier
function extraire_numero_fichier() {
    local nom_fichier="$1"  # Nom de fichier passé en paramètre

    # Extraire le numéro en utilisant une expression régulière
    local numero=$(echo "$nom_fichier" | grep -oE '^[0-9]+')
    echo "$numero"
}

# Fonction pour extraire l'extension du nom de fichier
function extraire_extension_fichier() {
    local nom_fichier="$1"  # Nom de fichier passé en paramètre

    # Extraire l'extension en utilisant une expression régulière
    local extension=$(echo "$nom_fichier" | grep -oE '\.[^.]+$' | sed 's/\.//')
    echo "$extension"
}

# Fonction pour créer un fichier
function creer_fichier() {
    local nom_fichier="$1"  # Nom du fichier à créer passé en paramètre

    # Vérifier si le fichier existe déjà
    if [ ! -e "$nom_fichier" ]; then
        touch "$nom_fichier"
        echo "Fichier créé : $nom_fichier"
        return 0
    else
        echo "Erreur : Impossible de créer le fichier $nom_fichier. Il existe déjà."
        return 1
    fi
}

# Fonction pour créer le fichier "main"
function creer_fichier_main() {
    local nom_fichier="$1"  # Nom du fichier à partir duquel créer le fichier "main"

    local numero=$(extraire_numero_fichier "$nom_fichier")
    local extension=$(extraire_extension_fichier "$nom_fichier")
    local fichier_main="${numero}-main.${extension}"

    # Vérifier si le fichier "main" existe déjà
    if [ ! -e "$fichier_main" ]; then
        touch "$fichier_main"
        echo "Fichier créé : $fichier_main"
    else
        echo "Erreur : Impossible de créer le fichier $fichier_main. Il existe déjà."
    fi
}

# Boucle pour créer les fichiers
for fichier_base in "${fichiers[@]}"
do
    if creer_fichier "$fichier_base"; then
        creer_fichier_main "$fichier_base"
    fi
    sleep 2
done

echo "Terminé."
