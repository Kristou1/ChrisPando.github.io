"""Programme qui donne à l'utilisateur le choix de convertir des miles/h en km/h et m/s
ou des km/h en miles/h et m/s suivant un nombre fourni par celui-ci"""

def demander_valeur(nom):
    # Demande une valeur numérique strictement positive.
    while True:
        try:
            valeur = float(input(f"Saisissez une vitesse à convertir en {nom} : "))
                
            if valeur <= 0:
                print("Erreur : la valeur doit être supérieure à 0.\n")
            else:
                return valeur
            
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.\n")


def conversion_km_heure(miles):
    # Converti en kilomètres une valeur donnée en miles
    return miles * 1609 / 1000


def conversion_miles_vers_m_s(miles):
    # Converti en mètres une valeur donnée en miles
    return miles * 1609 / 3600


def conversion_miles(kilometre):
    # Converti en miles une valeur donnée en kilomètres
    return kilometre * 1000 / 1609


def main():
    # Demande à l'utilisateur s'il veut convertir des miles/h en km/h ou inversement
    choix = input("Choisissez le type de conversion ? \n1 - Miles/h -> km/h et m/s \n2 - km/h -> Miles/h et m/s :\n")
        
    if choix =="1":
        miles = demander_valeur("miles")
        kilometre = conversion_km_heure(miles)
        metre = conversion_miles_vers_m_s(miles)
            
        print(f"Vitesse saisie     : {miles:.2f} miles/h")
        print(f"Conversion en Km/h : {kilometre:.2f}")
        print(f"Conversion en m/s  : {metre:.2f}")
    elif choix == "2":
        nb_kilometres = demander_valeur("kilometres")
        nb_miles = conversion_miles(nb_kilometres)
        nb_metres = conversion_miles_vers_m_s(nb_miles)
            
        print(f"Vitesse saisie     : {nb_kilometres:.2f} km/h")
        print(f"Conversion en Miles/h : {nb_miles:.2f}")
        print(f"Conversion en m/s  : {nb_metres:.2f}")
    else:
        print("Erreur : saisir uniquement '1' ou '2' pour définir le type de conversion\n" )
        


if __name__ == "__main__":
    main()
