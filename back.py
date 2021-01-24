import sqlite3

def connect():
    conn = sqlite3.connect('diary.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS diary (Id INTEGER PRIMARY KEY , date text , time text , study text, hour integer , note text , log text)")
    conn.commit()
    conn.close()

def insert(date , time , study , hour , note , log):
    conn = sqlite3.connect('diary.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO diary VALUES (NULL , ?,?,?,?,?,?)" , (date , time , study , hour , note , log))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('diary.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM diary")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('diary.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM diary WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , time='' , study='' , hour='' , note='' , log=''):
    conn = sqlite3.connect('diary.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM diary WHERE date=?  OR time=? OR study=? OR hour=? OR note=? OR log=?" , (date , time , study , hour , note , log))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
