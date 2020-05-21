import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "rpg.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row 
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)
 
query = """
SELECT
	charactercreator_character.character_id,
	count(distinct charactercreator_character.character_id)
FROM
	charactercreator_character_inventory
INNER JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id
"""
query2 = """
SELECT
	charactercreator_character.character_id,
	count(distinct charactercreator_character.character_id)
FROM
	charactercreator_character_inventory
INNER JOIN charactercreator_character ON charactercreator_character_inventory.character_id = charactercreator_character.character_id
"""

result = cursor.execute(query)
print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", dict(result2))

result3 = cursor.execute(query2).fetchall()
print("RESULT 3", dict(result3))

