# 1) afficher hello world dans le terminal

print("Hello World")

# 2) afficher les résultat des opérations dans le terminal

calcul = 3*3
print(calcul)
calcul2 = 12/1
print(calcul2)
calcul3 = 4+9+78
print(calcul3)
calcul4 = 12-7
print(calcul4)
calcul5 = 5e4
print(calcul5)

# 3) Ecrivez un programme qui demande son nom à l'utilisateur puis lui répond un message de bienvenue avec son nom.

nom = input("votre nom")
print("Bienvenue " + nom + " !")

# 4) Déclarer les variables 'nom' et 'prenom' et leur assigner votre nom et prénom.

nom_1 = ("Henaux")
prénom = ("Nathan")
print("Bonjour " + prénom + " " + nom_1)

# 5) Déclarer la variable myNumber = "123"
# Modifier son type String en type Integer. Assurez-vous d'avoir correctement modifié son type en l'affichant dans le terminal.

myNumber = "123"
myNumber_int = int(myNumber)
print(myNumber_int)

# 6) Ecrire un programme permettant de mettre en majuscule le contenu d'une String donnée par l'utilisateur. Même chose pour mettre le en minuscule. Vous affichez donc dans le terminal la chaîne rentrée à la fois en minuscule et en majuscule.

minuscule = "bonjour !"
minuscule.upper()
print(minuscule.upper())

majuscule = "LE"
majuscule.lower()
print(majuscule.lower())
