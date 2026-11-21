import sqlite3 
import pandas as pd
from pathlib import Path



class DatabaseManager:

    def __init__(self, db_path, schema_path):
        self.db_path = Path(db_path)
        self.schema_path = Path(schema_path)

        #ensure the database file exists
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        self.initialize_database()


    def get_connection(self):
        connection = sqlite3.connect(self.db_path)
        connection.execute("PRAGMA foreign_keys = ON;")

        connection.row_factory = sqlite3.Row
        return connection

    

    def initialize_database(self):
        schema_sql = self.schema_path.read_text(encoding='utf-8')

        with self.get_connection() as conn:
            conn.executescript(schema_sql)




    def get_products(self):
        with self.get_connection() as conn:
            rows = conn.execute("SELECT * FROM products").fetchall()
            return [dict(row) for row in rows]


    def save_product(self, ware_id, weight_kg, sales_per_month):
        with self.get_connection() as conn:
            conn.execute(
                """
                INSERT INTO products (ware_id, weight_kg, sales_per_month)
                VALUES (?, ?, ?)
                ON CONFLICT(ware_id) 
                DO UPDATE SET weight_kg=excluded.weight_kg, sales_per_month=excluded.sales_per_month
                """,
                (ware_id, weight_kg, sales_per_month)
            )

    def clear_products(self):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM products")

    