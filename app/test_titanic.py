

# app/test_titanic.py

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
DROP TABLE test_titanic;

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

#How many passengers survived, and how many died?
query2 = """
SELECT 
	t.survived
	,count(t.survived)
FROM 
	test_titanic t
GROUP BY 1
"""


#How many passengers were in each class?
query3 = """
SELECT 
	t.pclass
	,count(t.pclass)
FROM 
	test_titanic t
GROUP BY 1
"""

#How many passengers survived/died within each class?
query4 = """
SELECT 
	t.survived
	,t.pclass
	,count(t.survived)
FROM 
	test_titanic t
GROUP BY t.survived, t.pclass
"""

#What was the average age of survivors vs nonsurvivors?
#What was the average age of each passenger class?
#What was the average fare by passenger class? By survival?
#How many siblings/spouses aboard on average, by passenger class? By survival?
#How many parents/children aboard on average, by passenger class? By survival?

#Do any passengers have the same name?
query10 = """
SELECT 
	t.name
	,count(distinct t.name)
FROM 
	test_titanic t
GROUP BY 1
"""
result1 = cursor.execute(query2).fetchall()
print("RESULT 1", dict(result1))

result2 = cursor.execute(query3).fetchall()
print("RESULT 2", dict(result2))

result3 = cursor.execute(query4).fetchall()
print("RESULT 3", dict(result3))

result4 = cursor.execute(query5).fetchall()
print("RESULT 4", dict(result4))

result5 = cursor.execute(query6).fetchall()
print("RESULT 5", dict(result5))










