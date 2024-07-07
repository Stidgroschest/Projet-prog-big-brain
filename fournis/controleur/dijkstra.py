#import math
#from pytest import approx
#
#
#def test_dijkstra():
#    carte = [[10, 10, 10], [10, 1000, 25]]
#
#    depart = (0, 0)
#    tab_distance, tab_precedent = algorithme_dijkstra(carte, depart)
#
#    assert(tab_precedent == [-1, 0, 1, 0, -1, 1])
#    assert(tab_distance == approx([0, 0.032, 0.064, 0.032, math.inf, 0.06858], abs=0.0001))
#
#
#def algorithme_dijkstra(carte, depart):
#    """
#    Ce sous-programme interpréte la carte topographique reçu et trouve la meilleur manière
#    d'atteindre chacune des cases de la carte à partir d'un point de départ..
#
#    Arguments :
#        carte       : La carte topographique à analyser
#        depart      : Les coordonnées de la case à partir duquel on désire démarer une route.
#
#    Retourne :
#        tab_precedent: Un tableau indiquant à partir de quelle case on doit provenir pour atteindre de
#                       manière optimale n'importe quelle case.
#        tab_cout     : Le coût pour atteindre chaque case de la carte topographique à partir du départ. .
#    """
#
#    # On initialise les tableaux de travail avec (nb_colonnes * nb_colonnes) noeuds.
#    nb_noeuds = len(carte) * len(carte[0])
#    tab_cout, tab_precedent, tab_visite = initialiser_tableaux_travail(nb_noeuds)
#
#    # On débute l'analyse du graphe par le point de départ. Son coût est nul.
#    indice_depart = indice_carte2d_a_1d(depart)
#    tab_cout[indice_depart] = 0
#    tab_precedent[indice_depart] = -1
#
#    # On visite tous les noeuds du graphes.
#    for i in range(nb_noeuds):
#        # On trouve le prochain noeud à traiter. Celui-ci est le noeud le plus
#        # près de la source qui est encore non visité.
#        noeud_courant = prochain_noeud_a_visiter(tab_cout, tab_visite)
#
#        # On ajuste la distance de chacun des voisins du noeud courant.
#        traiter_voisins_noeud(carte, tab_cout, tab_precedent, noeud_courant)
#
#        # On marque le noeud comme étant visité.
#        tab_visite[noeud_courant] = True
#
#    return tab_cout, tab_precedent
#
#
#def meilleure_route_partant_de_depart(carte, depart):
#    """
#        Ce sous-programme utilise l'algorithme de disjkstra, à partir des coordonnées de la cases de
#        départ reçu, et trouve la meilleur route possible permettant d'atteindre l'autre bordure
#        de la carte topographique.
#
#        Arguments :
#            carte       : La carte topographique à analyser
#            depart      : Les coordonnées de la case à partir duquel on désire démarer une route.
#
#        Retourne :
#            route       : Les coordonnées optimales pour parcourir la carte tographique de
#                          gauche à droite.
#    """
#
#    # On trouve tous les chemins les plus courts partant du couple couple_depart.
#    tab_cout, tab_precedent = algorithme_dijkstra(carte, depart)
#
#    # On trouve le noeud d'arrivée qui permet de traverser la carte tout en coûtant le
#    # moins cher.
#    meilleur_noeud_arrivee = meilleure_destination(tab_cout)
#
#    # On conserve la route qui va du point de départ au point d'arrivée.
#    arrivee = indice_carte1d_a_2d(meilleur_noeud_arrivee)
#    chemin_en_ordre = remettre_chemin_en_ordre(tab_precedent, depart, arrivee)
#    route = transformer_chemin_route(chemin_en_ordre)
#
#    return route
#
#
#def remettre_chemin_en_ordre(tab_precedent, depart, destination):
#    """
#    Ce sous-programme interpréte le tableau des noeuds précédents produit par l'algorithme de
#    Dijkstra pour retrouver le chemin allant du noeud de depart au noeud de destination.
#
#    Arguments :
#        tab_precedent : Le résultat de l'algorithme de Dijkstra.
#        depart        : Les coordonnées de la case à partir duquel on désire un chemin.
#        destination   : Les coordonnées de la case qui termine le chemin.
#
#    Retourne :
#        chemin : Une liste contenant tous les numéros de cases permettant d'aller du noeud de
#                 départ au noeu finale.
#    """
#
#    # Le chemin est actuellement vide.
#    chemin_inverse = []
#
#    # On analysera des numéros de case plutôt qu'un couple de coordonnée.
#    indice_source = indice_carte2d_a_1d(depart)
#    indice_destination = indice_carte2d_a_1d(destination)
#
#    # La destination est ajoutée au chemin et l'on retrouvera notre chemin en revenant sur nos
#    # pas jusqu'à la case de départ.
#    #
#    # Le chemin sera donc dans l'ordre destination --> depart
#    chemin_inverse.append(indice_destination)
#    noeud_courant = indice_destination
#    while tab_precedent[noeud_courant] != indice_source:
#        chemin_inverse.append(tab_precedent[noeud_courant])
#        noeud_courant = tab_precedent[noeud_courant]
#
#    # On replace les cases dans l'ordre départ --> destination.
#    chemin = []
#    for i in range(len(chemin_inverse)):
#        chemin.append(chemin_inverse[len(chemin_inverse)-i-1])
#
#    return chemin
#
#
#def transformer_chemin_route(chemin):
#    """
#        Ce sous-programme prend le chemin (une série de numéro de cases) et le transforme en
#        une route (une série de coordonnées).
#
#        Arguments :
#            chemin : Le chemin à convertir.
#
#        Retourne :
#            route : Les numéros de cases du chemin transformé en coordonnées (ligne, colonne).
#    """
#
#    # On ajoute à la route chaque numéros de case du chemin, convertit en coordonnées (ligne, colonne).
#    route = []
#    for i in range(len(chemin)):
#        couple_courant = indice_carte1d_a_2d(chemin[i])
#        route.append(couple_courant)
#
#    return route
#