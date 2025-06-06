import time
import inspect
import csv
import matplotlib.pyplot as plt
from typing import Callable, List, Tuple
from . import fonctions

def mesurer_temps(fonction: Callable, n: int) -> float:
    """Mesure le temps d'exécution d'une fonction pour une valeur n donnée."""
    debut = time.time()
    fonction(n)
    fin = time.time()
    return fin - debut

def comparer_fonctions(fonction1: Callable, fonction2: Callable, 
                      valeurs_n: List[int]) -> List[Tuple[int, float, float]]:
    """Compare les temps d'exécution de deux fonctions pour différentes valeurs de n."""
    resultats = []
    for n in valeurs_n:
        temps1 = mesurer_temps(fonction1, n)
        temps2 = mesurer_temps(fonction2, n)
        resultats.append((n, temps1, temps2))
    return resultats

def sauvegarder_csv(resultats: List[Tuple[int, float, float]], 
                   nom_fichier: str = "result/resultats.csv") -> None:
    """Sauvegarde les résultats dans un fichier CSV."""
    with open(nom_fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'fonction1', 'fonction2'])
        writer.writerows(resultats)

def generer_graphique(resultats: List[Tuple[int, float, float]], 
                     nom_fichier: str = "result/comparaison.png") -> None:
    """Génère un graphique comparatif des résultats."""
    n = [r[0] for r in resultats]
    temps1 = [r[1] for r in resultats]
    temps2 = [r[2] for r in resultats]

    plt.figure(figsize=(10, 6))
    plt.plot(n, temps1, 'b-', label='Fonction 1')
    plt.plot(n, temps2, 'r-', label='Fonction 2')
    plt.xlabel('Valeur de n')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.title('Comparaison des temps d\'exécution')
    plt.legend()
    plt.grid(True)
    plt.savefig(nom_fichier)
    plt.close()

def main() -> None:
    # Récupérer toutes les fonctions du module fonctions
    fonctions_disponibles = inspect.getmembers(fonctions, inspect.isfunction)
    
    if len(fonctions_disponibles) < 2:
        print("Il faut au moins deux fonctions dans le module fonctions.py")
        return

    # Sélectionner les deux premières fonctions
    fonction1 = fonctions_disponibles[0][1]
    fonction2 = fonctions_disponibles[1][1]

    # Valeurs de n à tester
    valeurs_n = [100, 200, 400, 800, 1600]

    # Comparer les fonctions
    resultats = comparer_fonctions(fonction1, fonction2, valeurs_n)

    # Sauvegarder les résultats
    sauvegarder_csv(resultats)
    generer_graphique(resultats)

    print("Analyse terminée ! Les résultats ont été sauvegardés dans 'resultats.csv'")
    print("Le graphique a été sauvegardé dans 'comparaison.png'")
