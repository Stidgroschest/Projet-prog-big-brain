
import math
#Voici la variable globale qui est la route
route = []

#Ce programme détermine la longueur de la route globale.
def longueur():
    global route
    longueur = len(route)
    return longueur

#Ce programme ajouter un couple dans la route globale.
def ajouter(couple):
    global route
    route.append(couple)

#Ce programme retourne le dernier couple présent dans la route globale.
def dernier_couple():
    global route
    couple_retourner = route[len(route)-1]
    return couple_retourner

#Ce programme détermine si un couple est contenu dans la route globale
def couple_est_present(couple):
    global route
    Status = False
    for i in range(len(route)):
        if route[i] == couple:
            Status = True
    return Status


#Ce programme supprimer le dernier couple présent dans la route globale.
def retirer_dernier_couple():
    global route
    route.pop(len(route)-1)

#Ce programme calcule le coût de construction d'un tronçon de route entre deux élévations.
def cout_troncon(depart,arrivee):
    global route
    cout_longueur = 0.00016
    cout_denivellation = 0.0003
    longueur2d =200
    denivellation = abs(arrivee-depart)
    longueur3d= math.sqrt((denivellation**2)+(longueur2d**2))
    cout = (longueur3d*cout_longueur)+(depart*cout_denivellation)
    return cout

#Ce programme calcule le coût de construction d'une route reçue en paramètre.
def cout_route(tab2d,tab1d):
    cout = 0
    if len(tab1d)<2:
        return cout
    for i in range(len(tab1d)-1):
        ligne1, colonne1 = tab1d[i]
        lign2, colonne2 = tab1d[i+1]
        cout = cout + cout_troncon(tab2d[ligne1][colonne1],tab2d[lign2][colonne2])
    return cout

#Ce programme retourne la liste contenant la route globale.