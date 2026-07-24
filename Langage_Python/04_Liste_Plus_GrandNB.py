"""Programme qui recherche le plus grand élément prensent dans une liste dohnnée
Cette fois-ci nous n'utilisons pas la fonction max() et 
le programme affiche également l'indice de la valeur maximale"""

liste = [32, 5, 12, 8, 3, 75, 2, 15]

plus_grand = liste[0]
indice = 0

for i in range(len(liste)):
    if liste[i] > plus_grand:
        plus_grand = liste[i]
        indice = i

print(f"Le plus grand élément de cette liste vaut {plus_grand}")
print(f"Il se trouve à la position {indice + 1}")
