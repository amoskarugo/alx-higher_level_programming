#!/usr/bin/python3
"""python script that connects to MySQL db and
fetches data. """
import MySQLdb
import sys

args = sys.argv


def list_():
    """function fetches filtered data and prints it.
        print all items on the screen
    """
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cur = db.cursor()

    cur.execute("""SELECT *
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC"""
                )
    results = cur.fetchall()

    print(", ".join([city[2]
                     for city in results
                     if city[4] == args[4]])

          )

    cur.close()
    db.close()


if __name__ == '__main__':
    list_()
