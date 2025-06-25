#Этап 1: Создание структуры базы данных
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50),
#     email VARCHAR(50) UNIQUE
# );
#
# CREATE TABLE orders (
#     id SERIAL PRIMARY KEY,
#     customer_id INTEGER REFERENCES customers(id),
#     order_date DATE
# );
#
# CREATE TABLE order_items (
# 	id SERIAL PRIMARY KEY,
# 	order_id INTEGER REFERENCES orders(id),
# 	product_name VARCHAR(50),
# 	quantity INTEGER,
# 	price DECIMAL
# );
#
#Этап 2: Наполнение тестовыми данными
# INSERT INTO customers (name, email)
# VALUES ('NIF NIF', 'nif_nif@yandex.ru'),
# ('NAF NAF', 'naf_naf@yandex.ru'),
# ('Иван Иванов', 'ivanov@yandex.ru'),
# ('NUF NUF', 'nuf_nuf@yandex.ru');
#
#
# INSERT INTO orders (customer_id, order_date)
# VALUES (1, '2025-05-13'),
# (2, '2025-05-14'),
# (3, '2025-05-15'),
# (3, '2025-05-17'),
# (4; '2025-05-18')
#
# INSERT INTO order_items (order_id, product_name, quantity, price)
# VALUES (1, 'brick', 3, 1000),
# (2, 'tree', 4, 2000),
# (3, 'herb', 5, 3000),
# (4, 'cement', 6, 13000),
# (4, 'iron', 7, 7000);
#
# Этап 3: Запросы на чтение
# SELECT customers.id, order_date
# FROM orders
# JOIN customers ON orders.customer_id = customers.id
# WHERE name = 'NUF-NUF';
#
# SELECT product_name, quantity, price
# FROM order_items
# WHERE order_id = 4
# ORDER BY PRICE DESC;
#
# Задание 3: Группировка + фильтрация
# SELECT name, SUM(price*quantity) AS total_spent
# FROM customers
# JOIN orders ON orders.customer_id = customers.id
# JOIN order_items ON order_items.order_id = orders.id
# GROUP BY name
# HAVING SUM(price*quantity) > 5000

