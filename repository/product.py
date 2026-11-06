from psycopg import Connection, Error


def get_products(conn: "Connection"):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return products


def get_product_by_id(conn: "Connection", id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE id = %s", (id,))

        product = cursor.fetchone()

        return product


def create_product(conn: "Connection", name, description, price, stock, min_stock):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO products (name, description, price, stock, min_stock)
            VALUES (%s,%s,%s,%s,%s)
            RETURNING id
            """,
            (name, description, price, stock, min_stock),
        )
        product_id = cursor.fetchone()[0]
        return product_id


def update_product(conn: "Connection", name, description, price, stock, min_stock, id):
    with conn.cursor() as cursor:

        cursor.execute(
            """
            UPDATE products 
            SET 
            name = %s,
            description = %s,
            price = %s,
            stock = %s,
            min_stock = %s
            WHERE id = %s
            """,
            (name, description, price, stock, min_stock, id),
        )
        count_rows = cursor.rowcount
        return count_rows


def delete_product(conn: "Connection", id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        count_rows = cursor.rowcount
        return count_rows
