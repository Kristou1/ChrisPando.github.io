"""
=========================================================
Projet : Générateur de figures géométriques avec Turtle
Auteur : Christophe P.
Langage : Python 3
Bibliothèque : turtle

Description :
Application permettant de dessiner différentes figures
géométriques (polygones, étoile, spirales, rosace, dessin
personnalisé) avec personnalisation de la couleur, de
l'épaisseur du trait et sauvegarde au format PostScript.

Objectif pédagogique :
- Fonctions
- Menus interactifs
- Validation des saisies
- Boucles
- Paramètres de fonctions
- Factorisation du code
- Utilisation du module Turtle
=========================================================
"""

from turtle import *

def demander_entier(nom):
    """Demande à l'utilisateur un nombre entier pour l'unité correspondante."""
    while True:
        try:
            saisie = int(input(f"Entrez {nom} : "))

            if saisie <= 0:
                print("Erreur : la valeur doit être supérieure à 0.\n")
            else:
                return saisie

        except ValueError:
            print("Erreur : veuillez saisir uniquement un nombre entier.\n")


def dessiner_polygone(nombre_cotes):
    distance = demander_entier("distance")
    # L'angle extérieur d'un polygone régulier est égal à 360 / nombre de côtés.
    angle = 360 / nombre_cotes
       
    for _ in range(nombre_cotes):
        forward(distance)
        left(angle)
    
    

def dessiner_rectangle():
    largeur = demander_entier("la largeur")
    longueur = demander_entier("la longueur")
        
    for _ in range(2):
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)


def dessiner_etoile():
    distance = demander_entier("distance")

    for _ in range(5):
        forward(distance)
        left(144)


def dessiner_spirale_carree():
    distance = demander_entier("la distance")
        
    for _ in range(24):
        forward(distance)
        left(90)
        distance += 5


def dessiner_spirale():
    distance = demander_entier("la distance")
        
    for _ in range(50):
        forward(distance)
        left(91)
        distance += 5


def dessiner_rosace():
    longueur = demander_entier("la longueur des rayons")
    nombre_rayons = demander_entier("le nombre de rayons")
    # L'angle extérieur de la rosace est égal à 360 / nombre de rayons.
    angle = 360 / nombre_rayons

    for _ in range(nombre_rayons):
        forward(longueur)
        backward(longueur)
        left(angle)


def dessiner_fleur():
    rayon = demander_entier("le rayon des pétales")
    for _ in range(12):
        circle(rayon, 60)
        left(120)
        circle(rayon, 60)
        left(150)
        

def demander_recommencer():
    """Demande à l'utilisateur s'il souhaite recommencer."""
    while True:
        choix = input(
            "\nVoulez-vous réaliser un nouveau dessin ? (o/n) : "
        ).strip().lower()

        if choix == "o":
            return True

        if choix == "n":
            return False

        print("Réponse invalide : saisissez 'o' ou 'n'.")


def demander_sauvegarde():
    """Demande si le dessin doit être sauvegardé."""
    while True:
        choix = input(
            "\nVoulez-vous sauvegarder le dessin ? (o/n) : "
        ).strip().lower()

        if choix == "o":
            return True

        if choix == "n":
            return False

        print("Réponse invalide : saisissez 'o' ou 'n'.")


def demander_nom_fichier():
    """Demande un nom valide pour le fichier PostScript."""
    while True:
        nom = input(
            "\nEntrez le nom du fichier à sauvegarder : "
        ).strip()

        if not nom:
            print("Erreur : le nom du fichier ne peut pas être vide.")
            continue

        if not nom.lower().endswith(".ps"):
            nom += ".ps"

        return nom


def main():
    """Fonction principale du programme"""
    while True:
        choix = input(
            "\nChoisissez le dessin que vous voulez produire :\n"
            "1 - dessiner un carré\n"
            "2 - dessiner un rectangle\n"
            "3 - dessiner un triangle\n"
            "4 - dessiner une étoile\n"
            "5 - dessiner un pentagone\n"
            "6 - dessiner un hexagone\n"
            "7 - dessiner un octogone\n"
            "8 - dessiner un décagone\n"
            "9 - dessiner une spirale carrée\n"
            "10 - dessiner une spirale\n"
            "11 - dessiner une rosace\n"
            "12 - dessiner une fleur\n"
            "13 - dessin libre\n"
            "14 - effacer l'écran\n"
            "15 - changer la couleur\n"
            "16 - changer l'épaisseur\n"
            "17 - lever le stylo\n"
            "18 - reposer le stylo\n"
            "Votre choix : "
        ).strip()
        
        if choix == "1":
            dessiner_polygone(4)
                        
        elif choix =="2":
            dessiner_rectangle()
        
        elif choix == "3":
            dessiner_polygone(3)
            
        elif choix == "4":
            dessiner_etoile()
        
        elif choix == "5":
            dessiner_polygone(5)
        
        elif choix == "6":
            dessiner_polygone(6)
        
        elif choix == "7":
            dessiner_polygone(8)
        
        elif choix == "8":
            dessiner_polygone(10)
        
        elif choix == "9":
            dessiner_spirale_carree()
        
        elif choix == "10":
            dessiner_spirale()
        
        elif choix == "11":
            dessiner_rosace()
        
        elif choix == "12":
            dessiner_fleur()
        
        elif choix == "13":
            nombre = demander_entier("nombre")
            distance = demander_entier("distance")
            angle = demander_entier("angle de rotation")
    
            for _ in range(nombre):
                forward(distance)
                left(angle)
                
        elif choix == "14":
            clear()
            home()
            
            continue
            
        elif choix == "15":
            couleurs = {
                "1": "red",
                "2": "yellow",
                "3": "green",
                "4": "blue",
            }
            
            couleur = input(
                "\nChoisissez la couleur du stylo :\n"
                "1 - rouge\n"
                "2 - jaune\n"
                "3 - vert\n"
                "4 - bleu\n"
                "Votre choix : "
            ).strip()

            if couleur in couleurs:
                color(couleurs[couleur])
            else:
                print("Choix invalide.")
            
            continue
                
        elif choix == "16":
            while True:
                try:
                    epaisseur = int(input("Saisissez un nombre entre 1 et 6 : "))
                    
                    if epaisseur < 1 or epaisseur > 6:
                        print("Erreur : la taille du stylo doit être comprise entre 1 et 6.")
                    else:
                        pensize(epaisseur)
                        break
                    
                except ValueError:
                    print("Erreur : veuillez entrer uniquement une valeur numérique.")
            
            continue
                    
        elif choix == "17":
            penup()
            
            continue
            
        elif choix == "18":
            pendown()
            
            continue
                
        else:
            print("Choix invalide : saisissez un nombre entre '1' et '18'.")
            continue
        
        if not demander_recommencer():
            print("\nFin de la création des dessins.")
            break
    
    if demander_sauvegarde():
        nom_fichier = demander_nom_fichier()

        try:
            canvas = getcanvas()
            canvas.postscript(file=nom_fichier)
            print(f"Dessin sauvegardé dans « {nom_fichier} ».")

        except OSError as erreur:
            print(f"Erreur lors de la sauvegarde : {erreur}")
    else:
        print("Le dessin n'a pas été sauvegardé.")

    print("À bientôt !")
    # Maintient la fenêtre Turtle ouverte afin que
    # l'utilisateur puisse observer le dessin.
    done()
    


if __name__ == "__main__":
    main()
