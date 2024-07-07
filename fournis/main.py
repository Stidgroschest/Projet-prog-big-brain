"""
Auteur   : Francis Bourdeau
Fichier  : main.py

Ce module lance une application permettant de tracer une route dans un terrain montagneux.
    - La carte topographique et la route sont géré par des sous-programme contenu dans le package "modele"
    - La logique de controle pour l'ajout et le retrait de troncon de route est stocké dans le package "controleur"
    - La visualisation de la carte topographique et de la route est gérée dans le package "vue".
"""
from controleur import application

# On lance l'application à partir du controleur.
if __name__ == '__main__':
    application.demarrer()
