import csv
#Lire un fichier CSV d’employés
employes = []

with open("employes.csv", newline="", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        ligne["salaire"] = float(ligne["salaire"])
        employes.append(ligne)
salaires_par_departement = {}

#Calculer le salaire moyen par départ
for emp in employes:
    dept = emp["departement"]
    salaire = emp["salaire"]

    if dept not in salaires_par_departement:
        salaires_par_departement[dept] = []

    salaires_par_departement[dept].append(salaire)

moyennes = {}

for dept, salaires in salaires_par_departement.items():
    moyennes[dept] = sum(salaires) / len(salaires)

rapport = "RAPPORT RH – SALAIRE MOYEN PAR DÉPARTEMENT\n"
rapport += "-" * 45 + "\n"

#Générer un rapport textuel.

for dept, moyenne in moyennes.items():
    rapport += f"Département : {dept}\n"
    rapport += f"Salaire moyen : {moyenne:.2f} FCFA\n\n"
