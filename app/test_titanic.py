
# app/titanic_queries.py

import json
import os
import pandas as pd
import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv

load_dotenv()

# Load csv to insert into titanic_table
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
df = pd.read_csv(CSV_FILEPATH)


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
CREATE TABLE IF NOT EXISTS test_titanic (
    Survived INT,
    Pclass INT,
    Name varchar(120),
    Sex varchar(40) NOT NULL,
    Age INT,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare FLOAT
);
"""
print("SQL:", query)
cursor.execute(query)

execute_values(cursor, """
    INSERT INTO test_titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES %s;
""", [tuple(row) for row in df.values])

connection.commit()
cursor.close()
connection.close()













#cursor.execute('SELECT * from test_table;')
#result = cursor.fetchall()
#for row in result:
    #breakpoint()
    #print("------")
    #print(type(row))
    #print(row)
