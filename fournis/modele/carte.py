""""
Auteur   : Francis Bourdeau
Fichier  : carte.py

Ce module charge une carte topographique contenu dans un fichier csv.
Les données doivent être chargées en mémoire au début de l'application, puis on y accède grâce au tableau2d retourné
par la fonction charger.
"""
import csv


def charger(nom_fichier):
    """
    Ce sous-programme permet de lire les données de la carte topgraphique contenur dans le fichier possédant le nom
    reçu en paramètre.

    Arguments :
        nom_fichier : Le nom du fichier csv contenant la carte topgraphique.

    Retourne :
        carte : La carte topgraphique lue dans le fichier csv .
    """

    # On ouvre le fichier en lecture.
    carte = []
    with open(nom_fichier) as f:
        reader = csv.reader(f)

        # Chaque valeur de chaque ligne du fichier est ajoutée à la carte topographqiue.
        for ligne in reader:
            carte.append([int(valeur) for valeur in ligne])

    return carte
