"""Programme qui calcul le périmètre et l'aire d'un triangle quelconque
l'utilisateur fourni les 3 côtés
Ici on améliore le programme précédent de façon que celui-ci demande à l'utilisateur
s'il désire recommencer si les données qu'il a saisit ne permettent pas de former
un triangle"""

from math import sqrt

def demander_valeur(nom):
    """Demande une valeur numérique strictement positive."""
    while True:
        try:
            valeur = float(input(f"Saisissez la valeur du côté {nom} : "))
                
            if valeur <= 0:
                print("Erreur : la valeur doit être supérieure à 0.\n")
            else:
                return valeur
            
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.\n")


def perimetre_triangle(cote_a, cote_b, cote_c):
    """Calcule le périmètre d'un triangle"""
    return cote_a + cote_b + cote_c


def aire_triangle_qcq(cote_a, cote_b, cote_c):
    """Calcule l'aire d'un triangle quelconque"""
    perimetre = perimetre_triangle(cote_a, cote_b, cote_c)
    demi_perimetre = perimetre / 2

    return sqrt(
        demi_perimetre
        * (demi_perimetre - cote_a)
        * (demi_perimetre - cote_b)
        * (demi_perimetre - cote_c)
    )

def triangle_valide(cote_a, cote_b, cote_c):
    """Vérifie les inégalités triangulaires."""
    return(cote_a + cote_b > cote_c
           and cote_b + cote_c > cote_a
           and cote_a + cote_c > cote_b
           )


def demander_recommencer():
    """Demande à l'utilisateur s'il souhaite recommencer."""
    while True:
        choix = input("\nVoulez-vous recommencer ? (o/n) : ").strip().lower()

        if choix == "o":
            return True

        if choix == "n":
            return False

        print("Réponse invalide : saisissez 'o' ou 'n'.")


def main():
    """Fonction principale du programme"""
    while True:
        cote_a = demander_valeur("a")
        cote_b = demander_valeur("b")
        cote_c = demander_valeur("c")
    
        if triangle_valide(cote_a, cote_b, cote_c):
            perimetre = perimetre_triangle(cote_a, cote_b, cote_c)
            aire = aire_triangle_qcq(cote_a, cote_b, cote_c)
            
            print("=" * 60)
            print("PROGRAMME QUI CALCULE LE PERIMETRE ET L'AIRE D'UN TRIANGLE")
            print("=" * 60)
            print(f"\nValeur du côté a        : {cote_a:.2f}")
            print(f"Valeur du côté b        : {cote_b:.2f}")
            print(f"Valeur du côté c        : {cote_c:.2f}")
            print(f"\nPérimètre du triangle   : {perimetre:.2f}")
            print(f"Aire du triangle        : {aire:.2f}")
                        
        else:       
            print(
            "\nErreur : ces trois côtés ne permettent pas "
            "de former un triangle."
            )
        
        if not demander_recommencer():
            print("Fin du programme.")
            return
        
        
if __name__ == "__main__":
    main()
