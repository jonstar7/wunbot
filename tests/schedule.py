import datetime
import glob
# import os
import sqlite3

sqlFilename = "testdatabase.db"
tableName = "table0"
field = "column0"
fieldType = "INTEGER"



conn = sqlite3.connect(sqlFilename)
c = conn.cursor()
#  Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=tableName, nf=field, ft=fieldType))


conn.commit()
conn.close()