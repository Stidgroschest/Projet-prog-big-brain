"""
Auteur   : ...
Fichier  : ...

Ce module est responsable ...
"""
import modele.carte
import fournis.vue.graphe


#
# Déclaration de la variable global qui contiendra la carte topologique.
#
carte = []

#
# Les constantes définissant les types de clics fait avec la souris.
#
CLIC_GAUCHE = 1
CLIC_DROIT = 3


def demarrer():
    """
    Ce sous-programme permet de lire les données de la carte topographique et de les stocker en mémoire.
    Les données sont ensuite affiché grâce à la vue.
    On enregistre la procédure d'interruption qui permettra la gestion des clics de souris.

    Arguments :
        Aucuns.

    Retourne :
        Rien.
    """
    global carte
    carte = modele.carte.charger('modele/_carte.csv')
    fournis.vue.graphe.creer(carte, interruption_cliquer)


def interruption_cliquer(event):
    """
    Ce sous-programme permet de faire la gestion d'un clic droit ou d'un clic gauche dans la carte topographique.
    Un clic droit déclange le calcul de la route optimale.
    Un clic gauche ajoute ou retire un troncon de la route manuelle.

    Arguments :
        event : Les données fournis par python concerant le clic de souris (sa position, droite/gauche, etc.)

    Retourne :
        Rien.
    """

    #
    # La route optimale est calculée dès que l'utilisateur effectue un clic droit de souris
    #
    if event.button == CLIC_DROIT:
        trouver_route_optimale()

    #
    # La route manuelle est modifiée à toute les fois que l'utilisateur effectue un clic guache de souris
    #
    elif event.button == CLIC_GAUCHE:

        # On crée un tupple contenant le numéro de ligne et le numéro de colonne associé à la position de la souris
        # lorsque le clic a été fait.
        colonne = int(round(event.xdata))
        ligne = int(round(event.ydata))
        couple = (ligne, colonne)

        # On modifie la route en fonction de ces coordonnées.
        modifier_route_manuellement(couple)


def trouver_route_optimale():
    global carte

    print(f'TODO : trouver la route optimale (phase5) dans la carte ...')
    print(carte)
    print(f'\n')


def modifier_route_manuellement(couple):
    global carte

    print(f'TODO : ajout manuelle (phase4) au point ')
    print(f'ligne = {couple[0]}')
    print(f'colonne = {couple[1]}')
    print(f'\n')