import sys

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]


def is_valid(var, choices):
    return var in choices


while True:

    user_choice = ""
    while not is_valid(var=user_choice, choices=MENU_CHOICES):
        user_choice = input(MENU)
        if not is_valid(var=user_choice, choices=MENU_CHOICES):
            print("Veuillez choisir une option valide...")

    if user_choice == "1":
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif user_choice == "2":
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            print(f"L'élément {item} a bien été supprimé de la liste.")
            LISTE.remove(item)
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3":
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4":
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":
        print("À bientôt !")
        sys.exit()

    continuer = ""
    while is_valid(var=continuer, choices=["o", "n"]):
        continuer = input("Souhaitez-vous ajouter un autre élément à la liste o/n ? ")
        if is_valid(var=continuer, choices=["o", "n"]):
            print("Je n'ai pas compris votre choix...")

    if continuer == "n":
        break

    print("-" * 50)

print("Fin")
