import route


def test_longueur():

    resultat = route.longueur()
    assert resultat == 0
    print(resultat)
def test_ajouter():
    global route
    couple = (1,1)
    resultat = route.ajouter(couple)
    assert resultat == [(1,1)]
    print(resultat)

def test_dernier_couple():
    global route
    resultat = route.dernier_couple()
    assert resultat == (8,5)

def test_couple_est_present():
    global route
    resultat1 = route.couple_est_present((10,3))
    resultat2 = route.couple_est_present((15,5))
    assert resultat1 == True
    assert resultat2 == False

def test():
    global route
    couple1 = (1,1)
    route.ajouter(couple1)
    print(route.longueur())
    print(route.dernier_couple())
    couple2 = (2,2)
    route.ajouter(couple2)
    print(route.longueur())
    print(route.dernier_couple())
    print(f"Le couple {couple2} est t'il present: {route.couple_est_present(couple2)}")
    route.retirer_dernier_couple()
    print(route.longueur())
    print(route.dernier_couple())
    print(f"Le couple {couple2} est t'il present: {route.couple_est_present(couple2)}")
if __name__ == '__main__':
    test()
