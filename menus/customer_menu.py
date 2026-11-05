from repository.customer import (
    create_customer,
    delete_customer,
    get_customer_by_id,
    get_customers,
    update_customer,
)


def create_customer_menu(conn):

    lastname = input("Entrez le nom du nouveau client : ")
    firstname = input("Entrez le prénom du nouveau client : ")
    email = input("Entrez l'email du nouveau client : ")
    phone = input("Entrez le N° de téléphone du nouveau client : ")
    address = input("Entrez l'adresse du nouveau client : ")

    id = create_customer(conn, lastname, firstname, email, phone, address)

    print(f"L'utilisateur a bien été créé avec l'ID : {id}")


def update_customer_menu(conn):

    customers = get_customers(conn)

    print("Liste des clients : ")
    for customer in customers:
        print(customer)

    print("---------------------------------")
    id = input("Entrez l'id du client à modifier : ")
    lastname = input("Entrez le nom : ")
    firstname = input("Entrez le prénom : ")
    email = input("Entrez l'email : ")
    phone = input("Entrez le N° de téléphone : ")
    address = input("Entrez l'adresse : ")

    count = update_customer(conn, lastname, firstname, email, phone, address, id)

    print("Client modifié avec succès !")
    # print(f"{count} lignes ont été modifié")


def delete_customer_menu(conn):

    id = input("Entrez l'id du client à supprimer : ")
    count = delete_customer(conn, id)
    print(f"{count} lignes ont été modifié")


def customer_menu(conn):

    while True:
        print(" ========= MENU CLIENT =========")
        print("1. Liste des clients")
        print("2. Rechercher un client (par id)")
        print("3. Créer un nouveau client")
        print("4. Mettre à jour un client")
        print("5. Supprimer un client")
        print("0. Retour au menu principal")

        choice = input(" ========= Entrez votre choix : ")

        match choice:

            case "1":
                customers = get_customers(conn)

                print("Liste des clients : ")
                for customer in customers:
                    print(customer)

            case "2":
                customer_id = input("ID du client : ")
                customer = get_customer_by_id(conn, customer_id)

                print(customer if customer else "Client introuvable.")

            case "3":
                create_customer_menu(conn)

            case "4":
                update_customer_menu(conn)

            case "5":
                delete_customer_menu(conn)

            case "0":
                break

            case _:
                print("Choix invalide.")
