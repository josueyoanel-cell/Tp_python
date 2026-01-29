#Implementation du tri à bulles
def tri_a_bulles(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab
#Implementation de la recherche lineaire 
def recherche_lineaire(tab, valeur):
    for i in range(len(tab)):
        if tab[i] == valeur:
            return i
    return -1
#3. Comparer le temps d’exécution avec les fonctions Python