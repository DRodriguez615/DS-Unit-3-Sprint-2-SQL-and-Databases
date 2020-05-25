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

#How many characters are there?
#How many of each specific subclass?
#How many total Items?
#How many of the Items are weapons? How many are not?
#How many Items does each character have? (Return first 20 rows)
#How many Weapons does each character have? (Return first 20 rows)
#On average, how many Items does each Character have?
#On average, how many Weapons does each character have?

 
# How many characters are there? -302
query = """
SELECT
	c.character_id
	,count(distinct c.character_id)
FROM
	charactercreator_character c
"""

# How many of each specific subclass?
#come back, takes too long to load, coding error?####### 
# cleric = 75
# figher = 68
# mage = 108
# thief = 51
# mage/necromancer = 11
query2 = """
SELECT
	c.character_id
	,c.name as character_name 
	,count(distinct cleric.character_ptr_id) as cleric_characters
	,count(distinct f.character_ptr_id) as fighter_characters
	,count(distinct mage.character_ptr_id) as mage_characters
	,count(distinct thief.character_ptr_id) as thief_characters
FROM charactercreator_character c 
LEFT JOIN charactercreator_cleric cleric ON cleric.character_ptr_id = cleric.character_ptr_id
LEFT JOIN charactercreator_fighter f ON f.character_ptr_id = f.character_ptr_id
LEFT JOIN charactercreator_mage mage ON mage.character_ptr_id = mage.character_ptr_id
LEFT JOIN charactercreator_thief thief ON thief.character_ptr_id = thief.character_ptr_id
"""

# How many total items?
query3 = """
SELECT
	ai.item_id
	,count(distinct ai.item_id)
FROM
	armory_item ai
"""

# How many Items are weapons? = 37 How many are not? 174-37= 137
query4 = """
SELECT
	ai.item_id
	,count(distinct ai.item_id) as items
	,count(distinct aw.item_ptr_id) as weapon_count
FROM armory_item ai
LEFT JOIN armory_weapon aw ON ai.item_id = ai.item_id
"""

# How many items does each character have?
query5 = """
SELECT
	c.character_id
	,c.name as character_name 
	,count(distinct ai.item_id) as item_count
FROM charactercreator_character c 
LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
LEFT JOIN armory_item ai ON ai.item_id = inv.item_id
GROUP BY c.character_id 
"""

# How many weapons does each character have?
query6 = """
SELECT
	c.character_id
	,c.name as character_name 
	,count(distinct w.item_ptr_id) as weapon_count
FROM charactercreator_character c 
LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
LEFT JOIN armory_weapon w ON w.item_ptr_id = inv.item_id
GROUP BY c.character_id 
"""

#
query4 = """

"""

result = cursor.execute(query)
print("RESULT", dict(result)) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", dict(result2))

result3 = cursor.execute(query2).fetchall()
print("RESULT 3", dict(result3))

