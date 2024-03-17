#!/usr/bin/python3
"""a script that lists all states from database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


def list_db():
    """lists argv arguments

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_db()
