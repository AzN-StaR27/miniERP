from repository.customer import (
    create_customer,
    delete_customer,
    get_customer_by_id,
    get_customers,
    update_customer,
)
from utils.terminal import clear_terminal, pause_terminal
from helpers.input_helpers import get_existing_customer_id


def create_customer_menu(conn):

    lastname = input("\nEntrez le nom du nouveau client : ")
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
    
    customer_id = get_existing_customer_id(conn,"Entrez l'id du client à modifier :")
    # id = int(input("Entrez l'id du client à modifier : "))
    lastname = input("Entrez le nom : ")
    firstname = input("Entrez le prénom : ")
    email = input("Entrez l'email : ")
    phone = input("Entrez le N° de téléphone : ")
    address = input("Entrez l'adresse : ")

    _ = update_customer(conn, lastname, firstname, email, phone, address, customer_id)

    print("Client modifié avec succès !")
    # print(f"{count} lignes ont été modifié")


def delete_customer_menu(conn):

    id = input("Entrez l'id du client à supprimer : ")
    count = delete_customer(conn, id)
    print(f"{count} lignes ont été modifié")


def customer_menu(conn):

    while True:
        clear_terminal()
        print("     ========= MENU CLIENT =========")
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

                max_last_name = max(3, max(len(str(c[1])) for c in customers))
                max_first_name = max(6, max(len(str(c[2])) for c in customers))
                max_mail = max(5, max(len(str(c[3])) for c in customers))
                max_phone = max(12, max(len(str(c[4])) for c in customers))

                print("\nListe des clients :\n")
                for customer in customers:

                    id, last_name, first_name, mail, phone, _, date = customer
                    print(f"id : {id} | nom : {last_name:<{max_last_name}} | prénom : {first_name:<{max_first_name}} | email : {mail:<{max_mail}} | N° de tel : {phone:<{max_phone}} | date d'adhésion : {date.strftime("%d/%m/%Y")}")

            case "2":

                    customers = get_customers(conn)

                    max_last_name = max(3, max(len(str(c[1])) for c in customers))
                    max_first_name = max(6, max(len(str(c[2])) for c in customers))
                    max_mail = max(5, max(len(str(c[3])) for c in customers))
                    max_phone = max(12, max(len(str(c[4])) for c in customers))

                    print("\nListe des clients :\n")

                    ids = []
                    for customer in customers:

                        
                        id, last_name, first_name, mail, phone, _, date = customer
                        ids.append(int(id)) 
                        print(f"id : {id} | nom : {last_name:<{max_last_name}} | prénom : {first_name:<{max_first_name}} | email : {mail:<{max_mail}} | N° de tel : {phone:<{max_phone}} | date d'adhésion : {date.strftime("%d/%m/%Y")}")


                    while True:

                        try:

                            customer_id = int(input("\n ========= ID du client : "))

                            if customer_id in ids: 
                                 break

                            print("\n ID invalide !")


                        except ValueError: 
                            print("\n ID invalide !")
                    
                    customer = get_customer_by_id(conn, customer_id)

                    if customer:
                        id, last_name, first_name, mail, phone, _, _ = customer
                        print(
                            f"\n infos :\n nom : {last_name}\n prénom : {first_name}\n email : {mail}\n N° de téléphone : {phone}"
                        )
                    else:
                        print("Client introuvable.")

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

        pause_terminal()
