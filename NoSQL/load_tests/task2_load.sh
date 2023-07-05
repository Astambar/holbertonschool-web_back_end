#!/bin/bash

# Exécuter la tâche en boucle pour effectuer un test de charge
for i in {1..100}; do
  # Exécuter la tâche ici
  if bash "tasks/task2.sh" > /dev/null 2>&1; then
    echo "SUCCESS"
  else
    echo "FAIL"
  fi

  # Enregistrer l'utilisation du CPU
  top -b -n 1 | grep "Cpu(s)" >> "logs/cpu.log"

  # Enregistrer l'utilisation de la mémoire
  free -m | grep "Mem:" >> "logs/memory.log"

  sleep 1
done
