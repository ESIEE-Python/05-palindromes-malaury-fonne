"""Ce fichier va permettre de vérifier si un mot est un palindrome
"""

#### Fonction secondaire


def ispalindrome(p):
    '''Permet de vérifier si un mot est un palindrome c'est à dire qu'on peut le lire dans les 
    deux sens 
    >>>ispalindrome("kayak")
    True
    >>>ispalindrome("bateau")
    False
    '''
    # votre code ici
    table = str.maketrans("çéèêëôöâäà","ceeeeooaaa","\t\n,!?-:;. '")
    p=p.lower()
    p=p.translate(table)
    s=p[::-1]
    if p==s:
        return True
    return False

#### Fonction principale


def main():
    '''
    Ici on va faire appel a la fonction 
    '''
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
