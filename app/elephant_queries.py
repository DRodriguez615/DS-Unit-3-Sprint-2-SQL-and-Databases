
# app/elephant_queries.py

import json
import os
import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))


cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
print("CURSOR", type(cursor))


cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
for row in result:
    #breakpoint()
    print("------")
    print(type(row))
    print(row)







print("------------------")
query = f"""
CREATE TABLE IF NOT EXISTS test_table2 (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
);
"""
print("SQL:", query)
cursor.execute(query)

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

insertion_query = "INSERT INTO test_table2 (name, data) VALUES %s"
execute_values(cursor, insertion_query, [
    ('A rowww', 'null'),
    ('Another row, with JSONNN', json.dumps(my_dict)),
    ('Third row', "3")
])


connection.commit()

cursor.close()
connection.close()



exit()



insertion_query = f"INSERT INTO test_table2 (name, data) VALUES (%s, %s)"
cursor.execute(insertion_query,
  ('A rowwww', 'null')
  )
cursor.execute(insertion_query,
  ('Another row, with JSONNNNN', json.dumps(my_dict))
  )








