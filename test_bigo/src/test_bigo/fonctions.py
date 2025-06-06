# ------------------------------------------------------------------------------- #

def fonction_linéaire(n: int) -> int:
    """Fonction avec une complexité O(n)"""
    somme = 0
    for i in range(n):
        somme += i
    return somme

# ------------------------------------------------------------------------------- #

def fonction_quadratique(n: int) -> int:
    """Fonction avec une complexité O(n²)"""
    somme = 0
    for i in range(n):
        for j in range(n):
            somme += i * j
    return somme

# ------------------------------------------------------------------------------- #
