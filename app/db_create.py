import sqlite3

from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	c = connection.cursor()

	# c.execute("""DROP TABLE hangout""")

	c.execute("""CREATE TABLE hangout( hangout_id INTEGER PRIMARY KEY
		AUTOINCREMENT,
		title TEXT NOT NULL, level TEXT NOT NULL, language TEXT NOT NULL, hangout_date DATE NOT NULL, description TEXT NOT NULL, status INTEGER NOT NULL)""")

