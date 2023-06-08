class Person():
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

femme = Person("Kouadio","Affoue Ange",27)
print(" Bonjour tout le monde je me nome " + femme.nom + " " + femme.prenom + " et j'ai " + str(femme.age) + " ans")
