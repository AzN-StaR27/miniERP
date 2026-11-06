from repository.customer import get_customers
from repository.order import (
    create_order,
    delete_order,
    get_order_by_id,
    get_orders,
    get_orders_by_client_id,
    update_order,
)
from utils.terminal import clear_terminal


def create_order_menu(conn):

    customer_id = input("Entrez l'id du client : ")
    # par la suite ajouter les autres champs après avoir ajouter la fonctionnalité "keepValueAndSkip"

    id = create_order(conn, customer_id)

    print(f"La commande a bien été créé avec l'ID : {id}")


def update_order_menu(conn):

    orders = get_orders(conn)

    print("Liste des commandes : ")
    for order in orders:
        print(order)

    print("---------------------------------")
    id = input("Entrez l'id de la commande à modifier : ")
    customer_id = input("Entrez l'id du client pour la nouvelle commande : ")
    status = input(
        "Entrez l'état de la nouvelle commande (draft,confirmed,cancelled,completed) : "
    )

    _ = update_order(conn, customer_id, status, id)

    print("Commande modifié avec succès !")


def delete_order_menu(conn):

    id = input("Entrez l'id de la commande à supprimer : ")
    count = delete_order(conn, id)
    print(f"{count} ligne ont été modifié")


def order_menu(conn):

    while True:
        clear_terminal()
        print("     ========= MENU COMMANDE =========")
        print("1. Liste des commandes")
        print("2. Rechercher une commande (par id)")
        print("3. Rechercher une commande (par id du client)")
        print("3. Créer une nouvelle commande")
        print("4. Mettre à jour une commande")
        print("5. Supprimer une commande")
        print("0. Retour au menu principal")

        choice = input(" ========= Entrez votre choix : ")

        match choice:

            case "1":
                orders = get_orders(conn)

                print("Liste des commandes : ")
                for order in orders:
                    print(order)

            case "2":
                order_id = input("ID de la commande : ")
                order = get_order_by_id(conn, order_id)

                print(order if order else "Commande introuvable.")

            case "3":

                print("Liste des clients :")
                customers = get_customers(conn)

                for customer in customers:
                    print(customer)
                print("---------------------------------")

                customer_id = input("ID du client : ")
                order = get_orders_by_client_id(conn, customer_id)

                print(order if order else "Commande introuvable")

            case "4":
                create_order_menu(conn)

            case "5":
                update_order_menu(conn)

            case "6":
                delete_order_menu(conn)

            case "0":
                break

            case _:
                print("Choix invalide.")
