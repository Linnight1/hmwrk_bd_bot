import sqlite3

def initiate_db(id, title, description, price):
    connection = sqlite3.connect("../Lib/Bot/database.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INT NOT NULL
    );
    ''')
    add_product = cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
    if add_product.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products VALUES ("{id}", "{title}", "{description}", "{price}")
''')
    connection.commit()
    connection.close()
def get_all_products(product):
    connection = sqlite3.connect("../Lib/Bot/database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM Products WHERE id=?", (product,))
    get_product = cursor.fetchall()
    # get_description = cursor.fetchone()[1]
    # get_price = cursor.fetchone()[2]
    #
    # return f"Название: {get_title} | Описание: {get_description} | Цена: {get_price}"
    return get_product



initiate_db(1,"Название: Бальзам-ополаскиватель 'Лошадиная сила'", "Счастье для волос", "Стоимость:100" )
initiate_db(2,"Название: Маска для волос 'Лошадиная сила'", "Счастье для ваших волос", "Стоимость: 100")
initiate_db(3,"Название: Гель 'Лошадиная сила'", "Гель с конским каштаном и экстрактом пиявки","Стоимость: 200 руб")
initiate_db(4,"Название: Детский шампунь 'Лошадиная сила'", "Описание: Лошадиная сила для ваших детей", "Стоимость: 250 руб")
# connection = sqlite3.connect("../Lib/Bot/database.db")
# cursor = connection.cursor()
#
# cursor.execute("DELETE FROM Products WHERE id = ?", ( 4, ))
# connection.commit()
# connection.close()
