# installation instructions can be found at
# https://gist.github.com/rduplain/1293636

import pyodbc
from azure_sql_config import *

# server = <server>
# database = <database>
# username = <username>
# password = <password>
cnxn = pyodbc.connect("DRIVER=FreeTDS;SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};TDS_Version=8.0;".format(server=server,database=database,username=username,password=password))
cursor = cnxn.cursor()

for row in cursor.execute("SELECT * FROM Test"):
    print(row)
