#!/usr/bin/python3
"""python script that connects to MySQL db and
fetches data. Data is filtered by selecting items with the
name  passed as argument """
import MySQLdb
import sys

args = sys.argv


def list_():
    """function fetches filtered data and prints it.
        print all items with name passed as argument
    """
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cur = db.cursor()

    cur.execute(f"SELECT * FROM states WHERE BINARY "
                f"name = '{'{}'.format(args[4])}' ORDER BY id ASC")
    results = cur.fetchall()

    for state in results:
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    list_()
