"""Programme qui regroupe tous les calculs vus sur les listes"""

liste = [32, 5, 12, 8, 3, 75, 2, 15]

somme = 0
plus_grand = liste[0]
plus_petit = liste[0]
indice_max = 0
indice_min = 0
ecart = 0

for indice, valeur in enumerate(liste):
    if valeur > plus_grand:
        plus_grand = valeur
        indice_max = indice
    
    if valeur < plus_petit:
        plus_petit = valeur
        indice_min = indice
        
    somme += valeur
    

nombre = len(liste)
moyenne = somme / nombre
ecart = plus_grand - plus_petit

print("=" * 25)
print("Analyse de la liste")
print("=" * 25)
print(f"{'\nNombre d\'éléments':<20} : {nombre}")
print(f"{'\n\nSomme':<21} : {somme}")
print(f"{'Moyenne':<19} : {moyenne}")
print(f"{'\nPlus grand':<20} : {plus_grand}")
print(f"{'Indice':<19} : {indice_max}")
print(f"{'\nPlus petit':<20} : {plus_petit}")
print(f"{'Indice':<19} : {indice_min}")
print(f"{'\n\nEcart':<21} : {ecart}")
