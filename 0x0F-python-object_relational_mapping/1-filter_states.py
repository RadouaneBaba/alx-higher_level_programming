#!/usr/bin/python3

"""lists all states with a name starting with N (upper N) from db"""
import sys
import MySQLdb

db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

cur = db.cursor()
# Execution...
cur.execute("SELECT * FROM states WHERE name LIKE N%;")
rows = cur.fetchall()

for row in rows:
    print(row)
# clean up
cur.close()
db.close()
