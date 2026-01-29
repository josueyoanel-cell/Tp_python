class Etudiant:
    def init(self,nom,matricule,notes):
        self.nom = nom
        self.matricule = matricule 
        self.notes = notes

    def calcul_moyenne(self):
         if len(self.notes) == 0:
             return 0
         return sum(self.notes) / len(self.notes)
    
    def affichage(self):
        print("Nom: ",self.nom)
        print("Matricule: ",self.matricule)
        print("Note: ",self.notes)
        print("Moyenne: ",self.calcul_moyenne())
             

        
    