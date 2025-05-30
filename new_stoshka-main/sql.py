import sqlite3


def create_table():
    conn = sqlite3.connect("data_base.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS clients (
         id INTEGER PRIMARY KEY  AUTOINCREMENT,
         posluha TEXT,
          marka TEXT,
         time TEXT,
        date TEXT, 
         city TEXT    )''')
    
def fill_quiz(path_to_db):
    n = int(input("Введіть кількість тем: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()

    for i in range(n):
        name = input(f"Тема під номером {i}: ")
        cur.execute('''INSERT INTO quiz (name) VALUES (?)''', [name])
        conn.commit()
    conn.close()

    
    conn.commit()
    conn.close()
    
    
def fill_item(path_to_db):
    n = int(input("Введіть кількість послуг: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    for i in range(n):
        name = input(f"Введіть назву: ")
        desc = input(f"Введіть опис: ")
        img = input(f"Введіть фото: ")
        price = int(input(f"Введіть ціну: "))
        cur.execute('''INSERT INTO item (name, desc, img, price) VALUES (?,?,?,?)''', [name, desc, img, price])
        conn.commit()
    conn.close()


# create_table()
# #fill_category("data_base.db")
# fill_item("data_base.db")

def print_items(path_to_db):
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()
    i = 1
    cur.execute("SELECT * FROM item")
    items = cur.fetchall()
    pprint.pprint(items)
    for item in items:
        print(item)

    conn.close()
    return items
def get_items_list_by_category(category_id):
    conn = sqlite3.connect('data_base.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM item WHERE category_id = (?)", [category_id])
    data = cur.fetchall()
    conn.close()
    return data
print(get_items_list_by_category(1))

def insert_into(car, posluga, time, city):
    conn = sqlite3.connect('data_base.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO clients VALUES (?,?,?,?) ", [car, posluga, time, city])
    conn.commit()
    conn.close()


create_table()