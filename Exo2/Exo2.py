def calcule_moyenne(liste_de_notes):
    if len(liste_de_notes) == 0:
        return 0

    # Somme des notes
    somme = 0
    for note in liste_de_notes:
        somme += note

    # Calcul de la moyenne
    moyenne = somme / len(liste_de_notes)
    return moyenne


# Fonction mention
def mention(moyenne):
    if moyenne < 10:
        return "Ajourné"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 15:
        return "Bien"
    else:
        return "Très bien"


# Test
liste_notes = [15, 15, 17]

moyenne = calcule_moyenne(liste_notes)
resultat = mention(moyenne)

# Affichage
print("Notes :", liste_notes)
print("Moyenne :", moyenne)
print("Mention :", resultat)
