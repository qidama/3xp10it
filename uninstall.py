import os
import re
from exp10it import execute_sql_in_db
from exp10it import get_string_from_command
from exp10it import configIniPath
if os.path.exists(configIniPath):
    db_name = "exp10itdb"
    result = get_string_from_command("mysql")
    if re.search(r"Can't connect", result, re.I):
        os.system("service mysql start")
    execute_sql_in_db("drop database %s" % db_name)
    os.system("rm config.ini")
else:
    print("%s not exist" % configIniPath)
    print(("请手动删除数据库exp10itdb"))

os.system("echo y | pip3 uninstall exp10it")
os.system("rm %s" % configIniPath)
modulePath = os.path.abspath(__file__)[:-len(__file__.split("/")[-1])]
os.system("cd ~ && rm -r %s" % modulePath)
print("uninstall finished")
