from repository.product import(
    create_product,
    delete_product,
    get_product_by_id,
    get_products,
    update_product
)

def create_product_menu(conn):

    name = input("Entrez le nom du nouveau produit : ")
    description = input("Entrez une description pour le nouveau produit : ")
    price = input("Entrez le prix du nouveau produit : ")
    stock = input("Entrez le nombre de produit en stock : ")
    min_stock = input("Entrez le nombre de produit minimal à avoir en stock : ")

    id = create_product(conn, name, description, price, stock, min_stock)

    print(f"Le produit a bien été créé avec l'ID : {id}")

def update_product_menu(conn):

    produits = get_products(conn)

    print("Liste des produits : ")
    for produit in produits:
        print(produit)

    print("---------------------------------")
    id = input("Entrez l'id du produit à modifier : ")
    name = input("Nom du produit : ")
    description = input("Description du produit : ")
    price = input("Prix : ")
    stock = input("Combien en stock ? : ")
    min_stock = input("Stock minimal avant alerte : ")


    count = update_product(conn, name, description, price, stock, min_stock, id)

    print("Produit modifié avec succès !")

def delete_product_menu(conn):

    id = input("Entrez l'id du produit à supprimer : ")
    count = delete_product(conn, id)
    print(f"{count} ligne ont été modifié")

def product_menu(conn):

    while True:
        print(" ========= MENU PRODUIT =========")
        print("1. Liste des produits")
        print("2. Rechercher un produit (par id)")
        print("3. Créer un nouveau produit")
        print("4. Mettre à jour un produit")
        print("5. Supprimer un produit")
        print("0. Retour au menu principal")

        choice = input(" ========= Entrez votre choix : ")

        match choice:

            case "1":
                products = get_products(conn)

                print("Liste des produits : ")
                for product in products:
                    print(product)

            case "2":
                product_id = input("ID du produit : ")
                product = get_product_by_id(conn, product_id)

                print(product if product else "Produit introuvable.")

            case "3":
                create_product_menu(conn)

            case "4":
                update_product_menu(conn)

            case "5":
                delete_product_menu(conn)

            case "0":
                break

            case _:
                print("Choix invalide.")
