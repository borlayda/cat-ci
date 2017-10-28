"""
 This module is for database functions
 -------------------------------------

 Cat CI uses MySQL database to store data about the users and
 pipelines.

"""

import sqlite3

def dict_factory(cursor, row):
    result = {}
    for idx, col in enumerate(cursor.description):
        result[col[0]] = row[idx]
    return result

class Database(object):
    Database = None

    def __init__(self):
        self.cursor = None

    def Cursor(self):
        if self.cursor is None:
            if Database.Database is None:
                Database.Database = sqlite3.connect("cat-ci.db")
                Database.Database.row_factory = dict_factory
            self.cursor = Database.Database.cursor()
        return self.cursor

    def initDb(self):
        print "Initialize Cat CI database ..."
        with open("init.sql", "r") as init_sql:
            for line in init_sql:
                if not line.startswith('#'):
                    print "Executing " + line.strip() + "..."
                    self.Cursor().execute(line)
                    print "Done"

    def selectFromDb(self, query):
