#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""


def get_cities(userName, passWord, dbName, stateName):
    """ Takes 4 arguments: mysql username, mysql password, database name and
    state name
    ARGS:
        userName: the username
        passWord: the password
        dbName: the name of the database to access
        stateName: the name of the state to check
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

    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON states.id = cities.state_id "
                "WHERE states.name LIKE %s \
                ORDER BY cities.id;", (stateName,))
    query_rows = cur.fetchall()
    print(", ".join([city[0] for city in query_rows]))
    cur.close()
    db.close()


if __name__ == "__main__":
    """ Take in arguments and passes to get states from db """
    from sys import argv

    get_cities(argv[1], argv[2], argv[3], argv[4])
