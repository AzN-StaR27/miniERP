from menus.customer_menu import get_customer_by_id


def get_valid_id(prompt):

    while True:

        try:

            value = int(input(prompt))

            if value <= 0:
                print("Erreur : l'identifiant doit être supérieur à 0.")
                continue

            return value

        except ValueError:
            print("Erreur : veuillez saisir un nombre entier.")


def get_existing_customer_id(conn, prompt):
    while True:
        customer_id = get_valid_id(prompt)

        customer = get_customer_by_id(conn, customer_id)

        if customer is not None:
            return customer_id

        print("Erreur : aucun client ne correspond à cet identifiant.")