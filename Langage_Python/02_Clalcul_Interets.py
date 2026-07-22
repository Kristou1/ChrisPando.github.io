"""Programme qui calcul les intérêts accumulés chaque année, par capitalisation 
La valeur du capital, du taux et de la durée sont fournies par l'utilisateur.
Il affiche le capital et les intérêts gagnés chaque année ainsi que les gains totaux."""

def demande_valeur(nom):
    while True:
        try:
            valeur = float(input(f"Veuillez donner une valeur pour {nom} : "))
            if valeur <= 0:
                print(f"Erreur : la valeur de {nom} doit être supérieure à zéro.\n")
            else:
                return valeur
        except ValueError:
            print("Erreur : la valeur de la variable doit être obligatoirement un nombre.\n")



def calcul_interet(capital, interet, duree):
    # calcul des intérêts par capitalisation
    capital_depart = capital
    for annee in range(1, duree + 1):        
        capital_initial = capital
        capital = capital * (1 + interet/100)        
        interet_annuel = capital - capital_initial
        
        gain_total = capital - capital_depart
                   
        print(f"Année {annee:2} : "
              f"Capital = {capital:.2f} € | "
              f"Intérêt gagné = {interet_annuel:.2f} €"
              f" | Gain total = {gain_total:.2f} €")



def main():            
    capital = demande_valeur("capital")
    taux_interet = demande_valeur("intéret")
    duree = int(demande_valeur("duree"))
    
    calcul_interet(capital, taux_interet, duree)


if __name__ == "__main__":
    main()
    
