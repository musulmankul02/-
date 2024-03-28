import sqlite3

connection = sqlite3.connect("hw.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR (200) NOT NULL,
    price DOUBLE (6 , 3) NOT NULL DEFAULT 0.0,
    quantity INT NOT NULL DEFAULT 0.0
    )""")