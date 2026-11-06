from psycopg import Connection


def get_orders(conn: "Connection"):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        return orders


def get_order_by_id(conn: "Connection", id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM orders WHERE id = %s", (id,))

        order = cursor.fetchone()

        return order


def get_orders_by_client_id(conn: "Connection", customer_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM orders WHERE customer_id = %s", (customer_id,))

        orders = cursor.fetchall()

        return orders


def create_order(
    conn: "Connection",
    customer_id,
):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO orders (customer_id)
            VALUES (%s)
            RETURNING id
            """,
            (customer_id,),
        )
        result = cursor.fetchone()

        if result is not None:
            order_id = result[0]
        else:
            order_id = None
            print("Erreur lors de la création de la commande.")

        return order_id



def update_order(conn: "Connection", customer_id,status, id):
    with conn.cursor() as cursor:

        cursor.execute(
            """
            UPDATE orders 
            SET 
            customer_id = %s,
            status = %s
            WHERE id = %s
            """,
            (customer_id, status, id),
        )
        count_rows = cursor.rowcount
        return count_rows




def delete_order(conn: "Connection", id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM orders WHERE id = %s", (id,))
        count_rows = cursor.rowcount
        return count_rows
