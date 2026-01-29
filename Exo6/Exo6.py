#Créer un programme de division.
try:
 dividende =int(input("Entrez un nombre: "))
 diviseur = int(input("Entrez un chiffre: "))
 esultat = dividende / diviseur
except ValueError:
 print("Saisit invalide ce n'est pas un normbre")
except ZeroDivisionError:
 print("La division par zero n'est pas valide")



