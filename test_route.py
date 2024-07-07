import route


def test_longueur():

    resultat = route.longueur()
    assert resultat == 6
    print(resultat)


if __name__ == '__main__':
    test_longueur()