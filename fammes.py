from person import Person
class   Fille(Person):
    def __init__(self,nom,prenom,age,forme):
        super().__init__(nom,prenom,age)
        self.forme = forme

    def afficher(self):
        print(f"les proprietes d'une femme sont : \n nom: {self.nom} \n prenom: {self.prenom} \n age: {self.age} \n taille: {self.forme}")

fille1 = Fille("Any", "Gogoua",25,1.67)
fille1.afficher()