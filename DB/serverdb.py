#coding:utf-8
from bottle import *
import MySQLdb
import sys

#log in to database
db = MySQLdb.connect("195.178.232.16", port=3306, user="ad5158", passwd="Werenice123!", db="ad5158");
cur = db.cursor(MySQLdb.cursors.DictCursor)

#APP
#Variable that runs with the server file.
app = app()

def get_article():
    query = ("SELECT Article_ID, Header, Ingress, Content, Pic_info, timenow FROM articles") 
    cur.execute(query)
    return cur.fetchall()

def single_article():
    query = ("SELECT Article_ID, Header, Ingress, Content, Pic_info FROM articles") 
    cur.execute(query)
    return cur.fetchall()

#Routes
#Här följer alla routes, dessa kan nås med ett / efter hemsidenamnet.

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')

@route("/")
def index():
    return template("indexdb", articlelist=get_article())
 
@route("/article")
def articlepage():
    return template("article", articlelist=get_article())

@route("/articlepage")
def articlepage():
    return template("articlepage", sin=single_article())

run(app=app)
