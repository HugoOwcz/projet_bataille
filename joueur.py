
from jeu_de_carte import *

class Joueur():
    ''' créer un joueur, permet de montrer sa main, de donner le nombre de carte lui restant en main
        et de lui retirer/ajouter des cartes'''
    def __init__(self,nom,nbCartes,mainJoueur):
        # créer un joueur
        self.nom = nom # contient le nom du joueur
        self.nbCartes = nbCartes # contient le nombre de carte dans la main du joueur
        self.main = [] # liste qui va contenir les cartes du joueur
        self.setMain(mainJoueur) # ajout des cartes de départ dans la main du joueur
    def setMain(self,mainJoueur):
        # créer la main de départ du joueur
        for carte in mainJoueur:
            self.main.append(carte)
    def getNom(self):
        # donne le nom du joueur
        return self.nom
    def getNbCartes(self):
        # donne le nombre de carte dans la main du joueur
        return self.nbCartes
    def jouerCartes(self):
        # joue une carte de la main du joueur
        if self.nbCartes<=0:
            return None
        else:
            cartejouer=self.main.pop(0)
            self.nbCartes-=1
            return cartejouer
    def insererMain(self,carteGagne):
        # ajoute une carte dana la main du joueur
        self.main.append(carteGagne)
        self.nbCartes+=1

def testJoueur():
    jeu52 = JeuCartes(52)
    jeu52.melanger()
    L=jeu52.getJeu()
    distribution_3j_4c = jeu52.distribuerJeu(3, 4)
    joueur=Joueur('Patrick',len(distribution_3j_4c[1]),distribution_3j_4c[1])
    print(joueur.getNom())
    print(joueur.getNbCartes())
    carte=joueur.jouerCartes()
    print(carte.getNom())
    print(carte.getCouleur())
    joueur.insererMain(carte)
