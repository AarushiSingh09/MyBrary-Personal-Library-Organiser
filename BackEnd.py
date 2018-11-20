import sqlite3
from datetime import *
import json
import difflib
from difflib import get_close_matches
data=json.load(open("076 data.json"))

def connect():
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS Books (SNo INTEGER PRIMARY KEY, Title text, Author TEXT, Issue_Date TEXT, Return_Date TEXT )")
    conn.commit()
    conn.close()

def Insert(title, author, idate, rdate):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO Books VALUES(NULL,?,?,?,?)", (title, author, idate, rdate))
    conn.commit()
    conn.close()

def View():
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM Books")
    rows=curr.fetchall()
    conn.close()
    return rows

def Delete(sno):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("DELETE FROM Books WHERE SNo=?",(sno,))
    conn.commit()
    conn.close()

def Update(SNO,T,A,I,R):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("UPDATE Books SET Issue_Date=?, Return_Date=? ,Title=? , Author=? WHERE SNo=?",(I,R,T,A,SNO))
    conn.commit()
    conn.close()

def Search(t="",a="",i="",r=""):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM Books where Title=? OR Author=? OR Issue_Date=? OR Return_Date=?",(t,a,i,r))
    rows=curr.fetchall()
    conn.close()
    return rows

def Fine_Generator(sno,fine):
    conn=sqlite3.connect("Books.db")
    curr=conn.cursor()
    curr.execute("SELECT Return_Date FROM Books where SNo=?",(sno,))
    rows=curr.fetchall()
    conn.close()
    L=list (map(int,rows[0][0].split('-')))
    now=datetime.now()
    fine_day=datetime(L[2],L[1],L[0],0,0,0,0)
    ans=now-fine_day
    if ans>0:
        return(ans.days*int(fine))
    else:
        return 0

def Find_Meaning(word):
    word=word.lower()
    
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        return(data[get_close_matches(word,data.keys())[0]])
    else:
        return ("Try Again")

connect() #everytime this function is executed
#print(Fine_Generator(1,23))
#Insert("Panchtantra","Vishnu Singh", "1-12-18","15-12-18")
#Update("12-12-12","15-12-12", "C++ And OOPS")
#print(View())
#FineGenerator("Panchtantra")
