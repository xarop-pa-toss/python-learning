import sqlite3

invntry_table = """CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY,
                ball_type TEXT NOT NULL,
                quantity INT NOT NULL
            );"""
                
sales_table = """CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                inventory_id INT NOT NULL,
                ball_type TEXT NOT NULL,
                date DATE NOT NULL,
                time TIME NOT NULL,
                quantity INT NOT NULL,
                FOREIGN KEY (inventory_id) REFERENCES inventory (id)
            );"""
            
purchases_table = """CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY,
                inventory_id INT NOT NULL,
                ball_type TEXT NOT NULL,
                date DATE NOT NULL,
                time TIME NOT NULL,
                quantity INT NOT NULL,
                FOREIGN KEY (inventory_id) REFERENCES inventory (id) 
            );"""
            
# try:
#     with sqlite3.connect("test.db") as conn:
#         print("Created database successfully.")
# except Exception as e:
#     print("Error creating database:", e)
    
def updt_invntry_table():
    try:
        with sqlite3.connect("test.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO inventory (ball_type, quantity) VALUES (?,?)", ("Tennis Balls", 30))
            conn.commit()
            cursor.execute("SELECT * FROM inventory")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print("Error inserting into inventory table:", e)
        
updt_invntry_table()
                   
# try:
#     with sqlite3.connect("test.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute(invntry_table)
#         cursor.execute(sales_table)
#         cursor.execute(purchases_table)
#         conn.commit()
#         print("Created tables successfully.")

# except Exception as e:
#     print("Error creating table:", e)