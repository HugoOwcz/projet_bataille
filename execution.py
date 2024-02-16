
# Owczarczak Hugo T4     Léger Angélo T5

from bataille import *

def partie_de_bataille(n_carte,n_manche,nj1,nj2):
    jeu=JeuCartes(n_carte)
    partie_bataille=Bataille(jeu,nj1,nj2)
    for cpt in range(n_manche):
        print(partie_bataille.joueur1.getNbCartes(),partie_bataille.joueur2.getNbCartes())
        if partie_bataille.joueur1.getNbCartes()<=0:
            return nj2,"a gagné la partie"
        elif partie_bataille.joueur2.getNbCartes()<=0:
            return nj1,"a gagné la partie"
        partie_bataille.jouer()
    return "À la fin des", n_manche ,"manche, il restait", partie_bataille.joueur1.getNbCartes() ,"cartes à", nj1 ,"et", partie_bataille.joueur2.getNbCartes() ,"cartes à", nj2
