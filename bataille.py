
from joueur import *

class Bataille():
    # contient une table de jeu avec un jeu et des joueurs et permet de jouer une manche
    def __init__(self,jeuCarte,nj1,nj2):
        # créer la table
        self.jeu=jeuCarte # contient le jeu
        self.jeu.melanger() # mélange le jeu
        cartedistribuer = self.jeu.distribuerJeu(2,int(self.jeu.getTailleJeu()/2)) #distribue le jeu
        self.joueur1=Joueur(nj1,(self.jeu.getTailleJeu())/2,cartedistribuer[0]) # créer un joueur
        self.joueur2=Joueur(nj2,(self.jeu.getTailleJeu())/2,cartedistribuer[1]) # créer un deuxième joueur

    def jouer(self):
        # joue une manche de bataille
        assert self.joueur1.getNbCartes()>0 and self.joueur2.getNbCartes()>0
        cartejouer=[]
        gagnant=None
        while gagnant==None:
            cartejouer.append(self.joueur1.jouerCartes())
            cartejouer.append(self.joueur2.jouerCartes())
            if cartejouer[-2].estSuperieureA(cartejouer[-1]): # vérifie si la carte du joueur 1 est > à celle du joueur 2
                gagnant='j1'
            elif cartejouer[-2].estInferieureeA(cartejouer[-1]): # vérifie si la carte du joueur 1 est < à celle du joueur 2
                gagnant='j2'
            else:
                print('Bataille')
                if self.joueur1.getNbCartes()<2:
                    gagnant='j2'
                    for cpt in range(int(self.joueur1.getNbCartes())):
                        cartejouer.append(self.joueur1.jouerCartes())
                    break
                if self.joueur2.getNbCartes()<2:
                    gagnant='j1'
                    for cpt in range(int(self.joueur2.getNbCartes())):
                        cartejouer.append(self.joueur2.jouerCartes())
                    break
                cartejouer.append(self.joueur1.jouerCartes())
                cartejouer.append(self.joueur2.jouerCartes())
        for cpt in range(len(cartejouer)): # ajoute les cartes dans la main du joueur gagnant
            if gagnant=='j1':
                self.joueur1.insererMain(cartejouer[cpt])
            else:
                self.joueur2.insererMain(cartejouer[cpt])

def testBataille():
    jeu=JeuCartes(52)
    bataille=Bataille(jeu,'h','a')
    while bataille.joueur1.getNbCartes()>0 and bataille.joueur2.getNbCartes()>0:
        bataille.jouer()
