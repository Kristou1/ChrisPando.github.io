"""Programme qui calcul la période d'un pendule simple de longueur donnée.
L'utilisateur peux choisir de donner cette longueur soit en centimètres
soit en mètres"""
from math import pi, sqrt

ACCELERATION_PESANTEUR = 9.81  # En m/s²


def demander_longueur(unite):
    """Demande une longueur strictement positive, dans l'unité indiquée."""
    while True:
        try:
            longueur = float(
                input(f"Saisissez la longueur du pendule en {unite} : ")
            )

            if longueur <= 0:
                print("Erreur : la longueur doit être supérieure à 0.\n")
            else:
                return longueur

        except ValueError:
            print("Erreur : veuillez saisir une valeur numérique valide.\n")


def calculer_periode_pendule(longueur):
    """Calcule la période d'un pendule simple, exprimée en secondes."""
    return 2 * pi * sqrt(longueur / ACCELERATION_PESANTEUR)


def demander_recommencer():
    """Demande à l'utilisateur s'il souhaite recommencer."""
    while True:
        choix = input(
            "\nVoulez-vous effectuer un nouveau calcul ? (o/n) : "
        ).strip().lower()

        if choix == "o":
            return True

        if choix == "n":
            return False

        print("Réponse invalide : saisissez 'o' ou 'n'.")


def afficher_resultat(longueur_metres, periode):
    """Affiche les données et le résultat du calcul."""
    print("\n--- Résultat ---")
    print(f"Longueur du pendule          : {longueur_metres:.2f} m")
    print(
        f"Accélération de la pesanteur : "
        f"{ACCELERATION_PESANTEUR:.2f} m/s²"
    )
    print(f"Période du pendule           : {periode:.2f} s")


def main():
    """Fonction principale du programme."""
    while True:
        choix = input(
            "\nChoisissez l'unité de la longueur :\n"
            "1 - Centimètres\n"
            "2 - Mètres\n"
            "Votre choix : "
        ).strip()
        
        if choix == "1":
            longueur_cm = demander_longueur("centimètres")
            longueur_metres = longueur_cm / 100
                        
        elif choix =="2":
            longueur_metres = demander_longueur("mètres")
            
        else:
            print("Choix invalide : saisissez '1' ou '2'.")
            continue
        
        periode = calculer_periode_pendule(longueur_metres)
        afficher_resultat(longueur_metres, periode)

        if not demander_recommencer():
            print("\nFin du programme. À bientôt !")
            return


if __name__ == "__main__":
    main()
