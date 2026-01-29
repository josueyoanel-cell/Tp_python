#Saisit du nom et et l'age
nom = input("Veuillez entrer votre nom: ")
age = int(input("Entrez votre age: "))

#Verification si l'utilisateur est mineur au majeur 
if age < 18:
    print("L'utilisateur est mineur")
else:
    print("L'utilisateur est majeur")

#Affichons les nbrs pair entre 1-100
for i in range(1,100):
    if i % 2 == 0:
        print(f"{i} est pair")
    else:
        print(f"{i} est impair")
#Affichage
#print(f"L'utilisateur se nomme{nom} qui a {age} ans")
#print("Les multilples de 2 sont: ",i)