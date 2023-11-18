#!/usr/bin/python3
"""python script that connects to MySQL db and
fetches data and prints it on the screen."""
import MySQLdb
import sys

args = sys.argv


def list_():
    """function that lists data fetched on the screen."""
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC;"
    cur.execute(query)
    results = cur.fetchall()

    for state in results:
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    list_()
