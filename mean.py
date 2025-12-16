def moyenne(valeurs):
    """
    Calcule la moyenne des valeurs d'une liste.
    """
    if not valeurs:
        raise ValueError("La liste ne peut pas être vide")

    return sum(valeurs) / len(valeurs)


liste = [1, 2, 3, 4]
print("Moyenne :", moyenne(liste))

