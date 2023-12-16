#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()

    cur.execute("""SELECT cities.name
            FROM cities INNER JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %s
            ORDER BY cities.id;""", (sys.argv[4],))
    rows = [col[0] for col in cur.fetchall()]

    print(', '.join(rows))

    cur.close()
    db.close()
