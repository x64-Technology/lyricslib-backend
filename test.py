import sqlite3, re
from dateutil import parser
from datetime import datetime

pattern = "[\[@_!#$%^&*()<>?/\\|}{~:]"

regex = re.compile(pattern=pattern)

def remove_special_with_hi(name, rem_space:bool = False):
    if regex.search(name) != None:
        name = regex.sub("", name)
    if rem_space:
        name = re.sub(pattern=" ", repl="-", string=name)
    return name

conn = sqlite3.connect("db.sqlite3")
connx = sqlite3.connect("dbc.sqlite3")


for x in connx.execute("select * from api_songlyric").fetchall():
    name = remove_special_with_hi(x[1])
    slug = remove_special_with_hi(x[1], rem_space=True).lower()


    conn.execute("insert into api_songlyric values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (None, name, x[2], x[3], x[4], x[5], slug, x[7], x[8], x[9], x[10]))
    conn.commit()

connx.close()
conn.close()