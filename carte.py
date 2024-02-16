
couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')

noms = ['2', '3', '4', '5', '6',
        '7', '8', '9', '10', 'Valet', 'Dame', 'Roi','As']

valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

class Carte:
    # créer des cartes, fournis des informations sur celle-ci et permer de les comparées
    def __init__(self, nom, couleur):
        # créer la carte
        assert couleur in couleurs and nom in noms
        self.nom = nom # contient le nom de la carte
        self.couleur = couleur # contient la couleur de la carte
        self.valeur = valeurs[nom] # contient la valeur de la carte
    def setNom(self, nom):
        # permet de modifier le nom la carte et change sa valeur pour convenir au nom
        self.nom = nom
        self.valeur = valeurs[nom]
    def getNom(self):
        # donne le nom de la carte
        return self.nom
    def getCouleur(self):
        # donne la couleur de la carte
        return self.couleur
    def getValeur(self):
        # donne la valeur de la carte
        return self.valeur
    def egalite(self, carte):
        # vérifie si deux carte son égale ou non
        if self.valeur == carte.valeur:
            return True
        return False
    def estSuperieureA(self, carte):
        # vérifie si la carte donner est inférieur à la carte en possession
        if self.valeur > carte.valeur:
            return True
        return False
    def estInferieureeA(self, carte):
        # vérifie si la carte donner est supérieur à la carte en possession
        if self.valeur < carte.valeur:
            return True
        return False

def testCarte():
    valetCoeur = Carte('Valet', 'COEUR')
    print('Nom:', valetCoeur.getNom())
    print('Couleur:', valetCoeur.getCouleur())
    print('Valeur:', valetCoeur.getValeur())
    valetCoeur.setNom('Dame')
    print('Nom modifie:', valetCoeur.getNom())
    print('Valeur modifiee:', valetCoeur.getValeur())
    # Essai des exceptions: cette instruction conduit à une erreur
    dameCarreau = Carte('Dame', 'COooEUR')