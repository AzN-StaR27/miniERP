from menus.customer_menu import customer_menu
from menus.product_menu import product_menu

# from menus.product_menu import product_menu
# from menus.order_menu import order_menu


def main_menu(conn):

    while True:

        try:

            print("\n========= MENU PRINCIPAL =========")
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
                    # order_menu(conn)
                    pass

                case "0":
                    print("À bientôt !")
                    break

                case _:
                    print("Choix invalide.")
        except Exception as e:
            print(f"Erreur : {e}")
