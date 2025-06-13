'''
===============================================================================    */
---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---    */
              -------------------------------------------------                    */
               PROJET: <TP1>          PAR: Dracken24                               */
              -------------------------------------------------                    */
               CREATED: 12-6th-2025                                                */
               MODIFIED BY: Dracken24                                              */
               LAST MODIFIED: 12-6th-2025                                          */
              -------------------------------------------------                    */
               FILE: tests_unitaires.py                                            */
              -------------------------------------------------                    */
---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---    */
===============================================================================    */
'''

from tp_1.benchmark import benchmark
from tp_1.datastructure import datastructure

import csv
import matplotlib.pyplot as plt
from typing import List, Tuple

# ------------------------------------------------------------------- #
# -----------------------------TESTS--------------------------------- #
# ------------------------------------------------------------------- #

results_get: List[Tuple[int, float, float, float, float]] = []
results_insert_head: List[Tuple[int, float, float, float, float]] = []
results_insert_mid: List[Tuple[int, float, float, float, float]] = []
results_insert_tail: List[Tuple[int, float, float, float, float]] = []
results_delete_head: List[Tuple[int, float, float, float, float]] = []
results_delete_mid: List[Tuple[int, float, float, float, float]] = []
results_delete_tail: List[Tuple[int, float, float, float, float]] = []

# ------------------------------------------------------------------- #

def test_with_capacity(data: datastructure, capacity: int) -> None:
    static_array = benchmark(data.static_array)
    dynamic_array = benchmark(data.dynamic_array)
    singly_linked_list = benchmark(data.singly_linked_list)
    doubly_linked_list = benchmark(data.doubly_linked_list)

    insert_capacity = [i for i in range(capacity)]

    result_1: float
    result_2: float
    result_3: float
    result_4: float

    print("******************** TEST WITH " + str(capacity) + " ELEMENTS *******************")

    print("\n----------------------------------------------------------------")
    print("-----------------------Get " + str(capacity) + "---------------------------------")
    print("----------------------------------------------------------------")
    # test get
    result_1 = static_array.test_get(insert_capacity)
    print("static array       get " + str(capacity) + ": " + str(result_1))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_2 = dynamic_array.test_get(insert_capacity)
    print("dynamic array      get " + str(capacity) + ": " + str(result_2))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_3 = singly_linked_list.test_get(insert_capacity)
    print("singly linked list get " + str(capacity) + ": " + str(result_3))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_4 = doubly_linked_list.test_get(insert_capacity)
    print("doubly linked list get " + str(capacity) + ": " + str(result_4))

    results_get.append((capacity, result_1, result_2, result_3, result_4))


    print("\n----------------------------------------------------------------")
    print("-----------------------Insert head " + str(capacity) + "-------------------------")
    print("----------------------------------------------------------------")
    # test insert head
    result_1 = static_array.test_insert_head(insert_capacity)
    print("static array       insert head " + str(capacity) + ": " + str(result_1))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_2 = dynamic_array.test_insert_head(insert_capacity)
    print("dynamic array      insert head " + str(capacity) + ": " + str(result_2))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_3 = singly_linked_list.test_insert_head(insert_capacity)
    print("singly linked list insert head " + str(capacity) + ": " + str(result_3))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_4 = doubly_linked_list.test_insert_head(insert_capacity)
    print("doubly linked list insert head " + str(capacity) + ": " + str(result_4))

    results_insert_head.append((capacity, result_1, result_2, result_3, result_4))

    print("\n----------------------------------------------------------------")
    print("-----------------------Insert mid " + str(capacity) + "--------------------------")
    print("----------------------------------------------------------------")
    # test insert mid
    result_1 = static_array.test_insert_mid(insert_capacity)
    print("static array       insert mid " + str(capacity) + ": " + str(result_1))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_2 = dynamic_array.test_insert_mid(insert_capacity)
    print("dynamic array      insert mid " + str(capacity) + ": " + str(result_2))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_3 = singly_linked_list.test_insert_mid(insert_capacity)
    print("singly linked list insert mid " + str(capacity) + ": " + str(result_3))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_4 = doubly_linked_list.test_insert_mid(insert_capacity)
    print("doubly linked list insert mid " + str(capacity) + ": " + str(result_4))

    results_insert_mid.append((capacity, result_1, result_2, result_3, result_4))

    print("\n----------------------------------------------------------------")
    print("-----------------------Insert tail " + str(capacity) + "-------------------------")
    print("----------------------------------------------------------------")
    # test insert tail
    result_1 = static_array.test_insert_tail(insert_capacity)
    print("static array       insert tail " + str(capacity) + ": " + str(result_1))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_2 = dynamic_array.test_insert_tail(insert_capacity)
    print("dynamic array      insert tail " + str(capacity) + ": " + str(result_2))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_3 = singly_linked_list.test_insert_tail(insert_capacity)
    print("singly linked list insert tail " + str(capacity) + ": " + str(result_3))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_4 = doubly_linked_list.test_insert_tail(insert_capacity)
    print("doubly linked list insert tail " + str(capacity) + ": " + str(result_4))

    results_insert_tail.append((capacity, result_1, result_2, result_3, result_4))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete head " + str(capacity) + "-------------------------")
    print("----------------------------------------------------------------")
    # test delete head
    result_1 = static_array.test_delete_head(insert_capacity)
    print("static array       delete head " + str(capacity) + ": " + str(result_1))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_2 = dynamic_array.test_delete_head(insert_capacity)
    print("dynamic array      delete head " + str(capacity) + ": " + str(result_2))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_3 = singly_linked_list.test_delete_head(insert_capacity)
    print("singly linked list delete head " + str(capacity) + ": " + str(result_3))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_4 = doubly_linked_list.test_delete_head(insert_capacity)
    print("doubly linked list delete head " + str(capacity) + ": " + str(result_4))

    results_delete_head.append((capacity, result_1, result_2, result_3, result_4))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete mid " + str(capacity) + "--------------------------")
    print("----------------------------------------------------------------")
    # test delete mid
    result_1 = static_array.test_delete_mid(insert_capacity)
    print("static array       delete mid " + str(capacity) + ": " + str(result_1))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_2 = dynamic_array.test_delete_mid(insert_capacity)
    print("dynamic array      delete mid " + str(capacity) + ": " + str(result_2))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_3 = singly_linked_list.test_delete_mid(insert_capacity)
    print("singly linked list delete mid " + str(capacity) + ": " + str(result_3))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_4 = doubly_linked_list.test_delete_mid(insert_capacity)
    print("doubly linked list delete mid " + str(capacity) + ": " + str(result_4))

    results_delete_mid.append((capacity, result_1, result_2, result_3, result_4))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete tail " + str(capacity) + "-------------------------")
    print("----------------------------------------------------------------")
    # test delete tail
    result_1 = static_array.test_delete_tail(insert_capacity)
    print("static array       delete tail " + str(capacity) + ": " + str(result_1))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_2 = dynamic_array.test_delete_tail(insert_capacity)
    print("dynamic array      delete tail " + str(capacity) + ": " + str(result_2))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_3 = singly_linked_list.test_delete_tail(insert_capacity)
    print("singly linked list delete tail " + str(capacity) + ": " + str(result_3))
    print("- - - - - - - - - - - - - - - - - - - -")
    result_4 = doubly_linked_list.test_delete_tail(insert_capacity)
    print("doubly linked list delete tail " + str(capacity) + ": " + str(result_4))

    results_delete_tail.append((capacity, result_1, result_2, result_3, result_4))

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

"""Sauvegarde les résultats dans un fichier CSV."""
def sauvegarder_csv(resultats: List[Tuple[int, float, float, float, float]], 
    nom_fichier: str = "result/resultats.csv") -> None:

    with (open(nom_fichier, 'w', newline='') as f):
        writer = csv.writer(f)
        writer.writerow(['n', 'Static Array', 'Dynamic Array', 'Singly Linked List', 'Doubly Linked List'])
        writer.writerows(resultats)

# ------------------------------------------------------------------- #

"""Génère un graphique comparatif des résultats."""
def generer_graphique(resultats: List[Tuple[int, float, float, float, float]], name_graphique: str,
    nom_fichier: str) -> None:

    n = [r[0] for r in resultats]
    temps1 = [r[1] for r in resultats]
    temps2 = [r[2] for r in resultats]
    temps3 = [r[3] for r in resultats]
    temps4 = [r[4] for r in resultats]

    plt.figure(figsize=(10, 6))

    plt.plot(n, temps1, 'r-', label='Static Array')
    plt.plot(n, temps2, 'g-', label='Dynamic Array')
    plt.plot(n, temps3, 'b-', label='Singly Linked List')
    plt.plot(n, temps4, 'y-', label='Doubly Linked List')

    plt.xlabel('Valeur de n')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.title('Comparaison des temps d\'exécution pour ' + name_graphique)
    plt.legend()
    plt.grid(True)
    plt.savefig(nom_fichier)
    plt.close()

# ------------------------------------------------------------------- #

def generer_all_graphiques() -> None:
    generer_graphique(results_get, "Get", "result/comparaison_get.png")
    generer_graphique(results_insert_head, "Insert Head", "result/comparaison_insert_head.png")
    generer_graphique(results_insert_mid, "Insert Mid", "result/comparaison_insert_mid.png")
    generer_graphique(results_insert_tail, "Insert Tail", "result/comparaison_insert_tail.png")
    generer_graphique(results_delete_head, "Delete Head", "result/comparaison_delete_head.png")
    generer_graphique(results_delete_mid, "Delete Mid", "result/comparaison_delete_mid.png")
    generer_graphique(results_delete_tail, "Delete Tail", "result/comparaison_delete_tail.png")

    sauvegarder_csv(results_get, "result/comparaison_get.csv")
    sauvegarder_csv(results_insert_head, "result/comparaison_insert_head.csv")
    sauvegarder_csv(results_insert_mid, "result/comparaison_insert_mid.csv")
    sauvegarder_csv(results_insert_tail, "result/comparaison_insert_tail.csv")
    sauvegarder_csv(results_delete_head, "result/comparaison_delete_head.csv")
    sauvegarder_csv(results_delete_mid, "result/comparaison_delete_mid.csv")
    sauvegarder_csv(results_delete_tail, "result/comparaison_delete_tail.csv")
