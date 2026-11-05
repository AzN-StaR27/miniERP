from repository.customer import get_customers,get_customer_by_id,create_customer,update_customer,delete_customer
from db.db import get_connection
from menus.main_menu import main_menu

if __name__ == "__main__":
    
    with get_connection() as conn:
            main_menu(conn)

