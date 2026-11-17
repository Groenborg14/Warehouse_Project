import sqlite3

connection = sqlite3.connect('Warehouse_Project/Src/WarehouseProject/Data/warehouse.db')

connection.execute("""
    CREATE TABLE IF NOT EXISTS products (
        ware_id TEXT PRIMARY KEY,
        weight_kg REAL,
        sales_per_month INTEGER,
        length_cm REAL,
        width_cm REAL,
        height_cm REAL
    )
""")

connection.commit()
connection.close()

