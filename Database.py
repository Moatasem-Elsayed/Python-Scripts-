import mysql.connector
from mysql.connector import errorcode
import pyautogui
import time

config = {
    'user': 'root',
    'password': 'Junction1.',
    'host': 'localhost'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

DB_NAME = 'JunctionFacebook'

groups = ["arduino.junction.297", 'Embedded.moatasem.elsayed', 'Arduino.from.one.to.done.junction.220',
          '1704995113130213', 'arduino.junction.187', '117581965590777', '705088266368688',
          'arduino.junction200', 'Embedded.system.diploma.junction218',
          '427954221497056', '749791112090508', '261626251224892', '1377913009030120',
          '1794458307340093', '594858277848685', '331021771111609', 'arduino.junction.212']

TABLES = {'groups': (
    "CREATE TABLE `groups` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `Name` varchar(300) NOT NULL,"
    # " `user` varchar(250) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)}
FacebooKGroups=[]

def create_database():
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))


def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({}) ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(err.msg)


def add_log(text):
    sql = f"INSERT INTO {DB_NAME}.groups(text) VALUES ( '{text}' )"
    print(sql)
    cursor.execute(sql)
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))


def get_logs():
    sql = (f"SELECT * FROM {DB_NAME}.groups ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()
    i=0;
    for row in result:
        FacebooKGroups.append(row[1])
        print(FacebooKGroups)


def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id))
    result = cursor.fetchone()

    for row in result:
        FacebooKGroups= row[1]
        print(FacebooKGroups)

def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text, id))
    db.commit()
    print("Log updated")


def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Log removed")


# create_database()
# create_tables()
#
# for i in groups:
#     add_log(i)
get_logs()
# get_log(2)
# update_log(2, 'Updated log')
# delete_log(2)
# get_logs()`

# groups = [ 'arduino.junction.297', 'Embedded.moatasem.elsayed', 'Arduino.from.one.to.done.junction.220',
#            '1704995113130213', 'arduino.junction.187', '117581965590777', '705088266368688',
#            'arduino.junction200', 'Embedded.system.diploma.junction218',
#           '427954221497056', '749791112090508', '261626251224892', '1377913009030120',
#           '1794458307340093', '594858277848685', '331021771111609', 'arduino.junction.212']

time.sleep(5)


def changelag():
    pyautogui.keyDown('shift')
    pyautogui.keyDown('alt')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('shift')


pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in FacebooKGroups:
    print( 'text')
    link = f'https://facebook.com/groups/{i}'
    print (link)
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    pyautogui.moveTo(550, 400)  # Move the mouse to the x, y coordinates 100, 150.
    time.sleep(5)
    pyautogui.doubleClick()  # Double click the mouse at the
    print("Writing post\n")
    time.sleep(2)
    pyautogui.typewrite("shorturl.at/cBI69")
    pyautogui.typewrite("\n")
    time.sleep(5)
    changelag()
    time.sleep(2)
    pyautogui.typewrite(";,vs ;hlg hkahx hggi lk h,g gd] gp] hgiot ,oghwi ofvi 5 skdk ")
    changelag()
    pyautogui.moveTo(600, 620)  # Move the mouse to the x, y coordinates 100, 150.
    time.sleep(5)
    pyautogui.doubleClick()  # Double click the mouse at the

    # # pyautogui.typewrite('p')
    # # time.sleep(2)
    # for j in range(1, 45):
    #     pyautogui.keyDown('tab')
    #     pyautogui.keyUp('tab')
    # pyautogui.keyDown('enter')
    # pyautogui.keyUp('enter')
    # j=0
    # for j in range(1, 13):
    #     pyautogui.keyDown('tab')
    #     pyautogui.keyUp('tab')
    #
    # pyautogui.keyDown('enter')
    # pyautogui.keyUp('enter')

    pyautogui.keyDown('Esc')
    pyautogui.keyup('Esc')

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

    time.sleep(3)

    pyautogui.write(['f6'])
    time.sleep(1)
