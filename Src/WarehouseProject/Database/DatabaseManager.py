import sqlite3 
import pandas as pd



class DatabaseManager:

    def __init__(self, db_path):
        self.db_path = db_path

    def get_products(self):
        with sqlite3.connect(self.db_path) as conn:
            return pd.read_sql_query("SELECT * FROM products", conn)


    def save_product(self, ware_id, weight_kg):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO products (ware_id, weight_kg)
                VALUES (?, ?)
                ON CONFLICT(ware_id) 
                DO UPDATE SET weight_kg=excluded.weight_kg
                """
            )

    def clear_products(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM products")

    