

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
DROP TABLE IF EXISTS titanic_table;

CREATE TABLE IF NOT EXISTS titanic_table (
    Survived INT,
    Pclass INT,
    Name varchar(60),
    Sex varchar(40) NOT NULL,
    Age INT,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare FLOAT
);
"""
print("SQL:", query)
cursor.execute(query)


#my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

insertion_query = "INSERT INTO titanic_table (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare) VALUES %s"
execute_values(cursor, insertion_query, [
    (0,3,'Mr. Owen Harris Braund', 'male',22,1,0,7.25),
    (1,1, 'Mrs. John Bradley (Florence Briggs Thayer) Cumings','female',38,1,0,71.2833),
    (1,3,'Miss. Laina Heikkinen','female',26,0,0,7.925),
    (1,1,'Mrs. Jacques Heath (Lily May Peel) Futrelle','female',35,1,0,53.1),
    (0,3,'Mr. William Henry Allen','male',35,0,0,8.05),
    (0,3,'Mr. James Moran','male',27,0,0,8.4583),
    (0,1,'Mr. Timothy J McCarthy','male',54,0,0,51.8625),
    (0,3,'Master. Gosta Leonard Palsson','male',2,3,1,21.075),
    (1,3,'Mrs. Oscar W (Elisabeth Vilhelmina Berg) Johnson','female',27,0,2,11.1333)
])

connection.commit()

cursor.close()
connection.close()














