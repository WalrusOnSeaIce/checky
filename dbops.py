import sqlite3
from datetime import datetime

db = sqlite3.connect("db")
cur = db.cursor()

def savetodb(record):
	#table creation command: CREATE TABLE checksums (id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, file VARCHAR(255), hash VARCHAR(12), original_checksum VARCHAR(60), file_checksum VARCHAR(60), result VARCHAR(30));
	cur.execute("CREATE TABLE IF NOT EXISTS checksums (id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, file VARCHAR(255), hash VARCHAR(12), original_checksum VARCHAR(60), file_checksum VARCHAR(60), result VARCHAR(30))")
	date = datetime.now().strftime("%Y-%m-%d")
	record.insert(0, date)
	cur.execute("INSERT INTO checksums (date, file, hash, original_checksum, file_checksum, result) VALUES(?, ?, ?, ?, ?, ?)", (record[0], record[1], record[2], record[3], record[4], record[5]))
	record.clear()
	db.commit()


def gethist():
	hist = cur.execute("SELECT * FROM checksums")
	record = hist.fetchall()
	for k in record:	print(k)


def delhist():
	cur.execute("DELETE FROM checksums")
	db.commit()