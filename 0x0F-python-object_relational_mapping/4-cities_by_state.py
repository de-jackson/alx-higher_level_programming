#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""


def get_cities(userName, passWord, dbName):
    """ Takes 3 arguments: mysql username, mysql password and database name
    Results must be sorted in ascending order by cities.id.
    ARGS:
        userName: the username
        passWord: the password
        dbName: the name of the database to access
    """

    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=userName,
        passwd=passWord,
        db=dbName,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities LEFT JOIN states "
                "ON cities.state_id = states.id "
                "ORDER BY cities.id ASC;")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """ Take in arguments and passes to get cities from db """
    from sys import argv

    get_cities(argv[1], argv[2], argv[3])
