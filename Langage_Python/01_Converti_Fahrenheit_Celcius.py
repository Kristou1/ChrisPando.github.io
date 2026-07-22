"""Programme qui converti en degrés Celsius une température exprimée
au départ en degrés Fahhrenheit, ou l'inverse."""

def demande_valeur(nom):
    while True:
        try:
            valeur = float(input(f"Veuillez donner une valeur pour {nom} : "))
            return valeur
        except ValueError:
            print("Erreur : la valeur de la variable doit être obligatoirement un nombre.\n")


def conversion_fahrenheit_celsius(nom):
    degres_celsius = (nom - 32) / 1.8
    print(f"La valeur de {nom}°F équivaut à {degres_celsius:.2f}°C")


def conversion_celsius_fahrenheit(nom):
    degres_fahrenheit = (nom * 1.8) + 32
    print(f"La valeur de {nom}°C équivaut à {degres_fahrenheit:.2f}°F")


def main():
    """Fonction principale du programme"""
    choix = input(
        "1 - Fahrenheit vers Celsius.\n"
        "2 - Celsius vers Fahrenheit.\n"
        "Votre choix : ")
    
    if choix == "1":
        degres_F = demande_valeur("degres_fahrenheit")
        conversion_fahrenheit_celsius(degres_F)
        
    elif choix == "2":
        degres_C = demande_valeur("degres_celsius")
        conversion_celsius_fahrenheit(degres_C)
    
    else:
        print("Choix invalide.")
   


if __name__ == "__main__":
    main()
    
