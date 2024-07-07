import route


def test_longueur():

    resultat = route.longueur()
    assert resultat == 6
    print(resultat)
def test_ajouter():
    global route
    couple = (7,6)
    resultat = route.ajouter(couple)
    assert resultat == [(11,0),(11,1),(11,2),(10,3),(9,4),(8,5),(7,6)]
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
if __name__ == '__main__':
    test_couple_est_present()