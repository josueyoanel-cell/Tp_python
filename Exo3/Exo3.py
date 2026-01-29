#Stocker une liste d’étudiants (nom, âge, moyenne).

etudiants = [
{"Nom":"Paul","Age":15,"Moyenne":17.5},

{"Nom":"Jean-Paul","Age":17,"Moyenne":15},

{"Nom":"Sylvanna","Age":18,"Moyenne":18.5},

{"Nom":"Blaze","Age":14,"Moyenne":12.5},

{"Nom":"Paul-Marie", "Age":15,"Moyenne":7.5}
]

#Afficher les étudiants admis (moyenne ≥ 10).
for  etudiant in etudiants:
    print("Nom :",etudiant["Nom"])
    print("moyenne :",etudiant["Moyenne"])
    if etudiant["Moyenne"] >= 10:
        print("Admis")
    else:
      print("Echoué")
#Calculer la moyenne générale de la classe.
Somme = 0

for etudiant in etudiants:
   Somme += etudiant["Moyenne"]
#
moyenne_general = Somme / len(etudiants)
print("la moyenne generale est: ",moyenne_general)