"""
Fonctions pour calculer les nombres premiers
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Vérifie si un nombre est premier.

    :param p: Le nombre à vérifier.
    :return: True si le nombre est premier, False.

    >>> isprime(-1)
    'False'
    >>> isprime(0)
    'False'
    >>> isprime(1)
    False
    >>> isprime(2)
    True
    >>> isprime(5)
    True
    >>> fact(10)
    False
    """
    if p == 1:
        return False
    end = int(sqrt(p)) + 1
    for i in range(2, end):
        if p % i == 0 :
            return False
    return True

#### Fonction principale

def main():
    """ Test le fonctionnement de isprime
    """
    isprime(13)
    isprime(1)
    isprime(563)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
