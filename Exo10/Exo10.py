import csv
import os

# Classe Etudiant
class Etudiant:
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes

    def moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

    def to_dict(self):
        return {
            "nom": self.nom,
            "matricule": self.matricule,
            "notes": ";".join(map(str, self.notes))
        }

# Classe de gestion
class GestionEtudiants:
    def __init__(self, fichier="etudiants.csv"):
        self.fichier = fichier
        self.etudiants = []
        self.charger()

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
        self.sauvegarder()

    def sauvegarder(self):
        with open(self.fichier, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nom", "matricule", "notes"])
            writer.writeheader()
            for e in self.etudiants:
                writer.writerow(e.to_dict())

    def charger(self):
        if not os.path.exists(self.fichier):
            return

        with open(self.fichier, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for ligne in reader:
                notes = list(map(float, ligne["notes"].split(";")))
                etudiant = Etudiant(ligne["nom"], ligne["matricule"], notes)
                self.etudiants.append(etudiant)

    def afficher_etudiants(self):
        for e in self.etudiants:
            print(f"{e.nom} ({e.matricule}) - Moyenne : {e.moyenne():.2f}")

    def moyenne_generale(self):
        if not self.etudiants:
            return 0
        total = sum(e.moyenne() for e in self.etudiants)
        return total / len(self.etudiants)


# Programme principal
gestion = GestionEtudiants()

# Ajout d'exemples
gestion.ajouter_etudiant(Etudiant("Alice", "ET001", [14, 15, 13]))
gestion.ajouter_etudiant(Etudiant("Bob", "ET002", [10, 12, 11]))

print("📋 Liste des étudiants :")
gestion.afficher_etudiants()

print("\n📊 Moyenne générale :", round(gestion.moyenne_generale(), 2))
