"""
Auteur   : ...
Fichier  : ...

Ce module est responsable ...
"""
import matplotlib.pyplot as plt

#
# Les objets représentant la figure, les données topographique et les routes tracées.
#
fig = None
ax = None
line = None

#
# Deux variables globales permettant de conserver le cout total des routes afin de les affichées
# dans le titre du graphe.
#
cout_manuelle = 0
cout_optimale = 0


#
# Le type de route qui peut être tracée.
#
MANUELLE = 0
OPTIMALE = 1

#
# Constante permettant une manipulation plus claire des couples.
#
LIGNE = 0
COLONNE = 1


def creer(carte, procedure_interruption):
    """
    Ce sous-programme permet de créer le graphe contenant la carte topographique de l'application.
    Une réfère vers la procédure d'interruption est également reçu pour activer l'écoute des actions de souris.

    Arguments :
        carte : Le tableau2d contenant toutes les données topographiques.
        procedure_interruption : Le nom de la procedure qui doit être appelé lorsque l'on clique sur le graphe

    Retourne :
        Rien.
    """
    global fig, ax

    #
    # On crée la figure, on y ajoute les données et on définit le titre initiale de la figure.
    #
    fig, ax = plt.subplots()
    ax.imshow(carte)

    #
    # On désactive l'autoscale pour que le graphe ne change pas de taille lorsque des tronçons sont
    # ajouté en bordure du graphe
    #
    ax.set_autoscalex_on(False)
    ax.set_autoscaley_on(False)

    #
    # On connecte la souris à sa procédure d'intérupption
    #
    fig.canvas.mpl_connect("button_press_event", procedure_interruption)

    # On affihce le graphe
    plt.show()
