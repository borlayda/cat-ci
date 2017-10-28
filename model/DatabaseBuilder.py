"""
"""

import sqlite3

import logging
import sys

LOGGER = logging.getLogger("Initializer")
LOGGER.setLevel(logging.DEBUG)
SH = logging.StreamHandler(sys.stdout)
SH.setLevel(logging.DEBUG)
FORMATTER = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
SH.setFormatter(FORMATTER)
LOGGER.addHandler(SH)

def dict_factory(cursor, row):
    result = {}
    for idx, col in enumerate(cursor.description):
        result[col[0]] = row[idx]
    return result

class DatabaseBuilder(object):
    Database = None

    def __init__(self):
        if DatabaseBuilder.Database is None:
            DatabaseBuilder.Database = sqlite3.connect("cat-ci.db")
            DatabaseBuilder.Database.row_factory = dict_factory
        self.cursor = DatabaseBuilder.Database.cursor()

    def save(self, obj):
        self.cursor.execute("SELECT * FROM " + obj.__class__.__name__ + "s WHERE Name like '%s'" % obj.name)
        db_obj = self.cursor.fetchone()
        if not db_obj:
            obj_keys = [key for key in obj.__dict__ if key != 'db']
            obj_vals = []
            for key in obj.__dict__:
                if key != 'db':
                    value = obj.__dict__[key]
                    if isinstance(value, list):
                        value = ",".join(value)
                    obj_vals.append(value)
            LOGGER.debug("New object with data (%s)" % (obj_keys + obj_vals))
            insert_query = "INSERT INTO {table_name}s ('{key1}', '{key2}', '{key3}') VALUES ('{val1}','{val2}','{val3}')".format(
                table_name=obj.__class__.__name__,
                key1=obj_keys[0],
                key2=obj_keys[1],
                key3=obj_keys[2],
                val1=obj_vals[0].replace("'", ""),
                val2=obj_vals[1].replace("'", ""),
                val3=obj_vals[2].replace("'", "")
            )
            LOGGER.debug(insert_query)
            self.cursor.execute(insert_query)
            DatabaseBuilder.Database.commit()
        else:
            LOGGER.debug("Object already exists")

    def load(self, obj, name):
        self.cursor.execute("SELECT * FROM " + obj.__class__.__name__ + "s WHERE Name like '%s'" % name)
        print self.cursor.fetchone()
