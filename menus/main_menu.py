from menus.customer_menu import customer_menu
from menus.order_menu import order_menu
from menus.product_menu import product_menu
from utils.terminal import clear_terminal, pause_terminal


def main_menu(conn):

    while True:

        try:
            clear_terminal()
            print("     ========= MENU PRINCIPAL =========")
            print("1. Gestion des clients")
            print("2. Gestion des produits")
            print("3. Gestion des commandes")
            print("0. Quitter")

            choice = input("Votre choix : ")

            match choice:

                case "1":
                    customer_menu(conn)

                case "2":
                    product_menu(conn)

                case "3":
                    order_menu(conn)

                case "0":
                    print("À bientôt !")
                    break

                case _:
                    print("Choix invalide !")
                    pause_terminal()

        except Exception as e:
            print(f"Erreur : {e}")
            pause_terminal()
