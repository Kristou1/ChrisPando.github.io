"""Script qui recopie une chaîne (dans une nouvelle variable) en l'inversant.
Avant de vérifier si celle-ci est un palindrome ou non, elle supprime les espaces
à l'intérieur des chaînes"""

chaine = str(input("Entrez une chaîne de caractères : "))
new_chaine = ""

# Ici on supprime les espaces dans les chaînes de caractères
chaine2 = chaine.replace(" ", "")

# On procède à l'inversion des caractères dans la chaîne
for i in range(len(chaine2) - 1, - 1, -1):
    new_chaine += chaine2[i]

print(f"{new_chaine}")


# Puis nous vérifion s'il s'agit d'un palindrome ou non
if chaine2.lower() == new_chaine.lower():
    print("Cette chaîne de caractères est un palindrome :",
          "elle peut se lire dans les deux sens")
else:
    print("Cette chaîne de caractères ne peut pas se lire dans les deux sens :",
          "Il ne s'agit pas d'un palindrome")
