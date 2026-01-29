#Créer un fichier notes.txt contenant des note
with open("notes.txt","w") as f:
    f.write("20\n1\n16\n18")

# Lire le fichier et calculer la moyenne.
somme = 0 
nbr_note =0
with open("notes.txt","r") as f:
 for ligne in f:
    notes = float(ligne.strip())
    somme +=notes
    nbr_note += 1

moyenne = somme / nbr_note
print("Moyenne de classe :",moyenne)
# Écrire le résultat dans un fichier resultat.
f=open("resultat.txt", "w")
f.write("La moyenne de classe est: 13.75")
f.close()

