#!/usr/bin/python3
"""displays all values in the states where name matches the arguments"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    cur = db.cursor()

    cur.execute("SELECT * FROM state WHERE name={};".format(argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
