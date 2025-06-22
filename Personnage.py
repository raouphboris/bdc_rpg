class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie, force, intelligence):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence


    def afficher_info(self):
        print(f"Nom:{self.nom}")
        print(f"classe:{self.classe}")
        print(f"Niveau:{self.niveau}")

#stupide