#!/usr/bin/python3
"""displays safely values in the states where name matches the arguments"""
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

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id;"
    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
