# This debug.py is for developers.Do not run it if you just want to run 3xp10it but not develop it.
import os
import re
from exp10it import execute_sql_in_db
from exp10it import get_string_from_command
from exp10it import configIniPath
if os.path.exists(configIniPath):
    db_name = "exp10itdb"
    a = input("1.删除config.ini和exp10itdb\n2....\n>")
    if a == '1':
        result = get_string_from_command("mysql")
        if re.search(r"Can't connect", result, re.I):
            os.system("service mysql start")
        execute_sql_in_db("drop database %s" % db_name)
        os.system("rm config.ini")
else:
    print("%s not exist" % configIniPath)
