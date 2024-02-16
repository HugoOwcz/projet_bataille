
from carte import *

import random

class JeuCartes():
    # créer un jeu de carte, permet de le mélanger de distribuer les cartes er d'obtenier la taille du jeu de carte
    def __init__(self, nbCartes):
        # créer un jeu de carte
        assert nbCartes==32 or nbCartes == 52
        self.jeu = [] # liste qui va contenir le jee
        self.nbCartes = nbCartes # contient le nombre de carte du jeu
        self.creerJeu() # ajout des cartes dans la liste
    def getTailleJeu(self):
        return self.nbCartes
    def creerJeu(self):
        # ajoute les cartes dans le jeu
        if self.nbCartes == 32:
            for nom in range(5,len(noms)):
                for couleur in couleurs:
                    self.jeu.append(Carte(noms[nom],couleur))
        else:
            for nom in noms:
                for couleur in couleurs:
                    self.jeu.append(Carte(nom,couleur))
    def getJeu(self):
        # renvoie le jeu
        return self.jeu
    def melanger(self):
        # mélange le jeu
        random.shuffle(self.jeu)
    def distribuerCarte(self):
        # distribue une carte
        carteDistibuer=self.jeu.pop(0)
        return carteDistibuer
    def distribuerJeu(self, nbJoueurs, nbCartes):
        # distribue le jeu de carte en entier
        assert nbCartes*nbJoueurs<=self.getTailleJeu()
        carteJoueurs=[]
        carteJoueur=[]
        for i in range(nbJoueurs):
            carteJoueur=[]
            for j in range(nbCartes):
                carteJoueur.append(self.distribuerCarte())
            carteJoueurs.append(carteJoueur)
        return carteJoueurs

def testJeuCartes():
    jeu52 = JeuCartes(52)
    jeu52.melanger()
    L=jeu52.getJeu()
    carte= L[2] # le 3e carte
    print('Nom:', carte.getNom())
    print('Couleur:', carte.getCouleur())
    print('Valeur:', carte.getValeur())
    # Distribution de 4 cartes à 3 joueurs
    distribution_3j_4c = jeu52.distribuerJeu(3, 4)
    for i in range(3):
        print('Joueur', i+1, ':')
        listeCartes = distribution_3j_4c[i]
        for c in listeCartes:
            print(c.getNom(), 'de', c.getCouleur())
    # Distribution de 10 cartes à 6 joueurs pour générer une exception (6X10 >52)
    distribution_6_joueurs_10_cartes_par_joueur = jeu52.distribuerJeu(6, 10)