import sqlite3

# crimes_table = """CREATE TABLE crimes (
#     crime_id INTEGER PRIMARY KEY,
#     crime_type TEXT,
#     date TEXT,
#     location TEXT,
#     status TEXT
# );"""

# suspects_table = """CREATE TABLE suspects (
#     suspect_id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     height_cm INTEGER,
#     hair_color TEXT,
#     eye_color TEXT
# );"""

# testimonies_table = """CREATE TABLE testimonies (
#     testimony_id INTEGER PRIMARY KEY,
#     crime_id INTEGER,
#     witness_name TEXT,
#     statement TEXT
# );"""

# footage_table = """CREATE TABLE atm_footage (
#     footage_id INTEGER PRIMARY KEY,
#     crime_id INTEGER,
#     timestamp TEXT,
#     notes TEXT
# );"""

# vehicle_table = """CREATE TABLE vehicle_registry (
#     license_plate TEXT PRIMARY KEY,
#     owner_id INTEGER,
#     make TEXT,
#     model TEXT,
#     color TEXT,
#     year INTEGER
# );"""

# traffic_table = """CREATE TABLE traffic_footage (
#     capture_id INTEGER PRIMARY KEY,
#     timestamp TEXT,
#     location TEXT,
#     license_plate TEXT
# );"""

# try:
#     with sqlite3.connect("police_criminal.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute(crimes_table)
#         cursor.execute(suspects_table)
#         cursor.execute(testimonies_table)
#         cursor.execute(footage_table)
#         cursor.execute(vehicle_table)
#         cursor.execute(traffic_table)
# except Exception as e:
#         print("Error creating database:", e)
        
        
# # --  Data Population
# # -- ----------------------------------------------------------------

# # -- Populate 'crimes' table
# try:
#     with sqlite3.connect("police_criminal.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("""INSERT INTO crimes (crime_id, crime_type, date, location, status) VALUES
#                         (101, 'Vandalism', '2023-12-20', 'City Hall', 'Closed'),
#                         (102, 'ATM Robbery', '2024-01-15', '301 Pine Plaza', 'Open'),
#                         (103, 'Burglary', '2024-01-12', '456 Oak Avenue', 'Open'),
#                         (104, 'Car Theft', '2024-02-01', 'West End Garage', 'Closed'),
#                         (105, 'Shoplifting', '2024-02-05', 'Maple Street Mall', 'Open');""")
# except Exception as e:
#         print("Error inserting into crimes table:", e)
        
# # -- Populate 'suspects' table        
# try:
#     with sqlite3.connect("police_criminal.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("""INSERT INTO suspects (suspect_id, first_name, last_name, height_cm, hair_color, eye_color) VALUES
#                         (201, 'Isabella', 'Rossi', 165, 'Brown', 'Brown'),
#                         (202, 'Arthur', 'Finch', 182, 'Blonde', 'Blue'),
#                         (203, 'Caleb', 'Hayes', 175, 'Brown', 'Green'),
#                         (204, 'Sophia', 'Chen', 170, 'Black', 'Brown'),
#                         (205, 'Liam', 'Gallagher', 178, 'Brown', 'Blue'), 
#                         (206, 'Olivia', 'Patel', 160, 'Black', 'Brown'),
#                         (207, 'Jared', 'Olsen', 185, 'Light Brown', 'Hazel');""")
# except Exception as e:
#         print("Error inserting into suspects table:", e)


# # -- Populate 'testimonies' table
# try:
#     with sqlite3.connect("police_criminal.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("""INSERT INTO testimonies (testimony_id, crime_id, witness_name, statement) VALUES
#                         (301, 102, 'Eleanor Vance', 'I was walking my dog. I saw a tall man with what looked like blonde hair running from the ATM. He jumped into a dark green sedan and sped off.'),
#                         (302, 102, 'Marcus Thorne', 'It was a blue pickup truck, I''m sure of it. It drove away really fast right after the alarm went off.'),
#                         (303, 103, 'Susan Miller', 'My house was broken into. I only saw their back, but they had brown hair and were average height.'),
#                         (304, 105, 'Security Guard', 'A woman with black hair ran out of the store with a handbag.'),
#                         (305, 102, 'Anonymous Caller', 'Heard a loud bang around 10 PM. Didn''t see anything clearly, just a car leaving in a hurry.');""")
# except Exception as e:
#         print("Error inserting into testimonies table:", e)

# # -- Populate 'atm_footage' table
# try:
#     with sqlite3.connect("police_criminal.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("""INSERT INTO atm_footage (footage_id, crime_id, timestamp, notes) VALUES
#                         (401, 102, '22:05', 'Suspect is tall, wearing a dark hoodie which obscures the face. Hair appears to be light-colored under the cap.'),
#                         (402, 105, '14:32', 'Female suspect, black hair, seen leaving store without paying for merchandise.');""")
# except Exception as e:
#         print("Error inserting into atm_footage table:", e)

# # -- Populate 'vehicle_registry' table
# try:
#     with sqlite3.connect("police_criminal.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("""INSERT INTO vehicle_registry (license_plate, owner_id, make, model, color, year) VALUES
#                         ('LKA-409-JP', 202, 'Subaru', 'Legacy', 'Green', 2022),
#                         ('NVA-211-RB', 203, 'Ford', 'Focus', 'Blue', 2019),
#                         ('BWE-781-VT', 205, 'Ford', 'F-150', 'Blue', 2021),      
#                         ('FGT-555-SS', 204, 'Honda', 'Civic', 'Silver', 2023),
#                         ('RTY-109-LP', 201, 'Toyota', 'Camry', 'Black', 2020),
#                         ('MKL-332-CX', 206, 'Nissan', 'Sentra', 'White', 2021),
#                         ('PXC-884-TR', 207, 'Jeep', 'Cherokee', 'Grey', 2020);""")
# except Exception as e:
#         print("Error inserting into vehicle_registry table:", e)

# # -- Populate 'traffic_footage' table
# try:
#     with sqlite3.connect("police_criminal.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("""INSERT INTO traffic_footage (capture_id, timestamp, location, license_plate) VALUES
#                         (501, '22:07', 'Pine Plaza & 1st Avenue', 'LKA-409-JP'),
#                         (502, '22:08', 'Pine Plaza & 2nd Avenue', 'BWE-781-VT'),
#                         (503, '22:10', 'Oak Avenue & 5th Street', 'NVA-211-RB'),
#                         (504, '19:45', 'Main Street & 3rd', 'FGT-555-SS'),
#                         (505, '22:15', 'Highway 5 Overpass', 'LKA-409-JP'),     
#                         (506, '21:50', 'Main Street & 4th', 'PXC-884-TR');""")
# except Exception as e:
#         print("Error inserting into traffic_footage table:", e)
        
        

try:
    with sqlite3.connect("police_criminal.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM crimes WHERE crime_id =?", (102,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print("Error:", e)
               
try:
    with sqlite3.connect("police_criminal.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM testimonies WHERE testimony_id=?""", (301,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print("Error:", e)
             
try:
    with sqlite3.connect("police_criminal.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM atm_footage WHERE crime_id=?""", (102,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print("Error:", e)

try:
    with sqlite3.connect("police_criminal.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM vehicle_registry WHERE color=?""", ("Green",))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print("Error:", e)
        
try:
    with sqlite3.connect("police_criminal.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM traffic_footage WHERE license_plate=?""", ("LKA-409-JP",))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print("Error:", e)
        
try:
    with sqlite3.connect("police_criminal.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM suspects WHERE hair_color =?""", ("Blonde",))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except Exception as e:
    print("Error:", e)