
#Voici la variable globale qui est la route
route = [(11,0),(11,1),(11,2),(10,3),(9,4),(8,5)]

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


