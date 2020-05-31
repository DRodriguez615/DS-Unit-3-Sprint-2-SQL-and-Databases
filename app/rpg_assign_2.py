
# app/rpg_assign_2.py

import json
import os
import pandas as pd
#import sqlite3
import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv

load_dotenv()


DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))


cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
print("CURSOR", type(cursor))

print("------------------")
query = f"""

CREATE TABLE IF NOT EXISTS rpg_db (
    item_id SERIAL PRIMARY KEY,
    name varchar(30),
    value INT,
    weight INT
);
"""
print("SQL:", query)
cursor.execute(query)

execute_values(cursor, """
    INSERT INTO rpg_db
    (item_id, name, value, weight)
    VALUES %s;
""", [tuple(row) for row in DB_FILEPATH.armory_item.values])

connection.commit()
cursor.close()
connection.close()