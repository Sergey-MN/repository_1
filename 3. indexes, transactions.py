import random
from datetime import date, timedelta

import psycopg2

# Этап 1: Массовое наполнение базы
connection = psycopg2.connect(dbname='test_db', user='postgres', password='1234')

# with connection.cursor() as cursor:
#     cursor.execute(
#         "SELECT id FROM orders"
#     )
#     order_ids = cursor.fetchall()
#     order_ids = list(map(lambda x: x[0], order_ids))
#
# with connection.cursor() as cursor:
#     for _ in range(1_000):
#         name = ['Сергей', 'Алексей', 'Виктор', "Виниамин", "Юрий", "Василий", "Магомед", "Богдан", "Рудольф",
#                 "Аркадий", "Леонид", "Дмитрий", "Станислав", "Вячеслав", "Алесандр", "Петр", "Владимир", "Алан",
#                 "Андрей", "Рафаэль", "Нурсултан"]
#         last_name = ["Иванов", "Петров", "Сидоров", "Василиев", "Магомедов", "Дмитриев", "Александров", "Абрамович",
#                      "Ротенберг", "Дерипаска",
#                      "Путин", "Медведев", "Обама", "Трамп", "Клинтон", "Лукашенко", "Якубович", ]
#         insert_customers = "INSERT INTO customers (name, email)" \
#                            "VALUES (%s, %s)"
#         n = random.choice(name) + random.choice(last_name)
#         mail = n + str(random.randint(1, 1_000_000)) + random.choice(
#             ['@yandex.ru', '@ya.ru', '@mail.ru', '@rambler.ru', '@gmail.ru', '@list.ru', "@gmail.com"
#                                                                                          "@yahoo.com", "@outlook.com",
#              '@hotmail.com', '@live.com', "@icloud.com", '@me.com', '@mac.com'])
#         cursor.execute(insert_customers, (n, f'{mail}'))
#     connection.commit()
#
# with connection.cursor() as cursor:
#     for _ in range(50_000):
#         cus_id = random.randint(1, 1000)
#         start_date = date(2023, 1, 1)
#         end_date = date(2023, 12, 31)
#         random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
#         insert_orders = "INSERT INTO orders (customer_id, order_date)" \
#                         "VALUES (%s, %s)"
#         cursor.execute(insert_orders, (cus_id, random_date))
#     connection.commit()
#
# with connection.cursor() as cursor:
#     for _ in range(1_000_000):
#         order_id = random.choice(order_ids)
#         product_name = f"Товар {random.randint(1, 500)}"
#         quantity = random.randint(1, 10)
#         price = random.randint(100, 100_000)
#         insert_order_items = "INSERT INTO order_items (order_id, product_name, quantity, price)" \
#                              "VALUES (%s, %s, %s, %s)"
#         cursor.execute(insert_order_items, (order_id, product_name, quantity, price))
#
#     connection.commit()


# Этап 2: Установка индексов
# try:
#     with connection.cursor() as cursor:
#         index_customer_id = cursor.execute("CREATE INDEX index_customer_id ON orders (customer_id)")
#         index_order_price = cursor.execute("CREATE INDEX INDEX_order_id_price ON order_items (order_id, price)")
#         index_product_name = cursor.execute("CREATE INDEX index_product_name ON order_items (product_name)")
#         connection.commit()
#         print('indexes created')
# except psycopg2.Error as e:
#     print('Error create index:', e)


# Этап 3: Анализ использования индексов
# with connection.cursor() as cursor:
#     cursor.execute("EXPLAIN ANALYZE SELECT * FROM order_items "
#                    "WHERE price > 10000 and id = 1000123")
#     print(cursor.fetchall())
#     cursor.execute("EXPLAIN ANALYZE SELECT * FROM orders "
#                    "WHERE customer_id = 1")
#     print(cursor.fetchall())


# Этап 4: Удаление неэффективных индексов

#Этап 5: Бизнес-логика с использованием транзакций
try:
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO orders (customer_id, order_date) "
                       "VALUES (777, CURRENT_DATE) RETURNING id;")
        inserted_id = cursor.fetchone()[0]
        for _ in range(4):
            cursor.execute(
                "INSERT INTO order_items (order_id, product_name, quantity, price) "
                f"VALUES({inserted_id}, "
                # "(SELECT product_name FROM order_items ORDER BY RANDOM() LIMIT 1), "
                "NULL, "
                "(SELECT quantity FROM order_items ORDER BY RANDOM() LIMIT 1), "
                "(SELECT price FROM order_items ORDER BY RANDOM() LIMIT 1))")
        connection.commit()
except psycopg2.Error as e:
    print("Error:", e)
# finally:
#     connection.close()

#Продемонстрировать, что в случае сбоя никаких частичных данных не остаётся в базе
try:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM orders '
                       f'WHERE id = {inserted_id}')
        print(cursor.fetchone())
except psycopg2.Error as e:
    print('Продемонстрировать, что в случае сбоя никаких частичных данных не остаётся в базе:', e)
finally:
    connection.close()



