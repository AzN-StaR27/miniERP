from psycopg import Connection


def get_customers(conn: "Connection"):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM customers")
        users = cursor.fetchall()
        return users


def get_customer_by_id(conn: "Connection", id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM customers WHERE id = %s", (id,))

        customer = cursor.fetchone()

        return customer


def create_customer(conn: "Connection", lastname, firstname, email, phone, address):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO customers (lastname, firstname, email, phone, address)
            VALUES (%s,%s,%s,%s,%s)
            RETURNING id
            """,
            (lastname, firstname, email, phone, address),
        )
        # customer_id = cursor.fetchone()[0]
        result = cursor.fetchone()

        if result is not None:
            customer_id = result[0]
        else:
            customer_id = None
            print("No product found")

        return customer_id


def update_customer(conn: "Connection", lastname, firstname, email, phone, address, id):
    with conn.cursor() as cursor:

        cursor.execute(
            """
            UPDATE customers 
            SET 
            lastname = %s,
            firstname = %s,
            email = %s,
            phone = %s,
            address = %s
            WHERE id = %s
            """,
            (lastname, firstname, email, phone, address, id),
        )
        count_rows = cursor.rowcount
        return count_rows


def delete_customer(conn: "Connection", id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM customers WHERE id = %s", (id,))
        count_rows = cursor.rowcount
        return count_rows
