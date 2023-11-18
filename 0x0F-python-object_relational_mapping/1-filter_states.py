#!/usr/bin/python3
"""python script that connects to MySQL db and
fetches data."""
import MySQLdb
import sys

args = sys.argv


def list_():
    """function fetches filtered data and prints it."""
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    cur.execute(query)
    results = cur.fetchall()

    for state in results:
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    list_()