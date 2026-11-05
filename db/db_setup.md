
# Mini ERP - Database Setup

## 1. Création de la base de données

À exécuter dans pgAdmin :

```sql
CREATE DATABASE mini_erp;
```

Sélectionner ensuite la base `mini_erp` dans pgAdmin.

## 2. Création des tables

### Customers

```sql
CREATE TABLE customers (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    country VARCHAR(50) NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_customers PRIMARY KEY (id),
    CONSTRAINT uq_customers_email UNIQUE (email),
    CONSTRAINT ck_customers_last_name_length CHECK (LENGTH(last_name) >= 3),
    CONSTRAINT ck_customers_first_name_length CHECK (LENGTH(first_name) >= 3),
    CONSTRAINT ck_customers_email_format CHECK (email ~* '^[A-Z0-9._+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$')



);
```

### Products

```sql
CREATE TABLE products (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    min_stock INTEGER NOT NULL DEFAULT 5,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_products PRIMARY KEY (id),
    CONSTRAINT ck_products_price_positive CHECK (price >=0),
    CONSTRAINT ck_products_stock CHECK (stock >= 0),
    CONSTRAINT ck_products_min_stock CHECK (min_stock >= 0)


);
```

### Orders

```sql
CREATE TABLE orders (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'draft',
    total_amount NUMERIC(12, 2) NOT NULL DEFAULT 0,

    CONSTRAINT pk_orders PRIMARY KEY (id),
    CONSTRAINT ck_orders_status CHECK (status IN (
        'draft',
        'confirmed',
        'cancelled',
        'completed'
    )),
    CONSTRAINT ck_orders_total_amount CHECK (total_amount >= 0)

    CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE RESTRICT
);
```

### Order Lines

```sql
CREATE TABLE order_lines (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL,

    subtotal NUMERIC(12, 2)
        GENERATED ALWAYS AS (quantity * unit_price) STORED,


    CONSTRAINT pk_order_lines PRIMARY KEY (id),
    CONSTRAINT ck_order_lines_quantity_above_zero CHECK (quantity > 0),
    CONSTRAINT ck_unit_price_positive CHECK (unit_price >= 0),

    CONSTRAINT fk_line_order
        FOREIGN KEY (order_id)
        REFERENCES orders(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_line_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON DELETE RESTRICT,

    CONSTRAINT unique_product_per_order
        UNIQUE (order_id, product_id)
);
```


## 3. Insertion des données de test

### Customers

```sql
INSERT INTO customers (last_name, first_name, email, phone, country, address)
VALUES
('Dupont', 'Alice', 'alice@gmail.com', '0470000001','Belgium','10, rue des pâquerettes'),
('Martin', 'Bob', 'bob@gmail.com', '0470000002','France','265, rue du Congrès'),
('Bernard', 'Charlie', 'charlie@gmail.com', '0470000003','Malawie','50, Avenue du parc');
```

### Products

```sql
INSERT INTO products (name, description, price, stock, min_stock)
VALUES
('Laptop Dell', 'Dell Latitude 5540', 899.99, 10, 3),
('Mouse Logitech', 'Wireless Mouse', 29.99, 50, 10),
('Keyboard Logitech', 'Mechanical Keyboard', 79.99, 20, 5),
('Monitor Samsung', '27 inch Monitor', 249.99, 8, 3);
```

## 4. Requêtes de vérification

### Afficher les commandes avec les clients

```sql
SELECT
    o.id,
    c.name AS customer,
    o.order_date,
    o.status,
    o.total_amount
FROM orders o
JOIN customers c ON c.id = o.customer_id;
```

### Afficher les produits avec un stock faible

```sql
SELECT name, stock, min_stock
FROM products
WHERE stock <= min_stock;
```

### Calculer le chiffre d'affaires

```sql
SELECT SUM(total_amount) AS revenue
FROM orders
WHERE status = 'completed';
```

## 5. Règles métier à implémenter dans la BLL

- Un email client doit être unique.
- Le prix d'un produit ne peut pas être négatif.
- Une commande doit appartenir à un client existant.
- Le stock doit être suffisant pour confirmer une commande.
- La confirmation d'une commande doit déduire le stock.
- L'annulation d'une commande confirmée doit restaurer le stock.
- Une commande terminée doit avoir été confirmée.
- Le montant total doit être recalculé à partir des lignes de commande.

**Important :** les opérations de création, confirmation et annulation de commandes doivent être exécutées dans des transactions PostgreSQL.