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

# 7) Réalisez un programme qui demande au visiteur l'année actuelle, son année de naissance puis calcule l'âge du visiteur et l'affiche dans un message à l'écran.

annee = int(input("En quel année somme nous ?"))
naissance = int(input("Quel est votre année de naissance ?"))
age = annee - naissance
print("Vous avez {}".format(age))

# Pour aller plus loin, demandez dans le terminal l'âge de la personne à côté de vous et afficher dans un message le cumul de vos deux âges.

age2 = 40
ageFinal = age2 + age
print("La somme des deux âge est {}".format(ageFinal))

# 9) Marc fait un peu de shopping. Il achète des chaussures à 70€, un jean à 59€ et un t-shirt à 20€.
#    Heureusement pour son portefeuille, il bénéficie d'une réduction de 20%.
#    Déclarez chacun des articles achetés dans une variable différente (prix1, prix2, etc.). Déclarez une dernière variable 'total' qui aura pour valeur la somme des achats, et l'afficher dans le terminal.


prix1 = (70*20)/100
prix1_0 = 70 - prix1
prix2 = (59*20)/100
prix2_0 = 59 - prix2
prix3 = (20*20)/100
prix3_0 = 20 - prix3
prixTotal = prix1_0 + prix2_0 + prix3_0
print("Le prix total est de {}".format(prixTotal))

# 10) Vous allez créer une mini calculatrice qui permet d'additionner des nombres. Quand le visiteur ouvre le programme vous lui demandez les nombres à additionner avec deux inputs différents, puis vous affichez le résultat à l'écran.
#     Attention il est possible de rentrer des nombres à virgule !

num1 = float(input("Veuillez saisir le premier numéro à additionner "))
num2 = float(input("Veuillez saisir le deuxième numéro à additionner "))
calculTotal = num1 + num2
print("Le résultat est {}".format(calculTotal))

# 11) Demander son prénom au visiteur.
#     Demander son nom au visiteur.

visitor_name = input("Quel est votre nom ?").upper()
visitorName = input("Quel est votre prénom ?").upper()

#Afficher dans un message la lettre par laquelle son prénom commence et la lettre par laquelle il termine. Ces lettres seront forcément affichées majuscules.

visitor_name_1 = visitor_name[0] + visitor_name[-1]
print("Voici la première et la dernière lettre de votre nom " + visitor_name_1)
visitorName_1 =  visitorName[0] + visitorName[-1]
print("Voici la première et la dernière lettre de votre prénom " + visitorName_1)

print("Vos initiales " + visitor_name_1 + visitorName_1)

age = int(input("Quel est votre âge ?"))
age = round(age/33)

print("Votre âge diviser par 33 est " + str(age))
