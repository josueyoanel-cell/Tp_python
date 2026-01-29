#Demander une phrase à l’utilisateur.
users = input("Veuiller saisir une phrase: ").split()

#Compter le nombre de mots.
nbr_mots = len(users)
print("Le nombre de mot est: ",nbr_mots)
#Trouver le mot le plus long
mot_plus_long = ""
for user in users:
    if len(user) > len(mot_plus_long):
        mot_plus_long = user 

print("Le mot le plus long est: ",mot_plus_long)
#Vérifier si la phrase est un palindrome
palindrome = user.replace(" ","").lower()
if palindrome == palindrome[::-1]:
    print(" La phrase est un palindrome")
else:
    print("La phrase n'est pas un palindrome")