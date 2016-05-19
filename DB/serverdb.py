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

def get_article(handler):
    query = "SELECT Header, Ingress, Content, Pic_info FROM articles \
        WHERE Article_ID = '%s' \
        ORDER BY timenow ASC" % (handler)
    cur.execute(query)
    return cur.fetchall()

def single_article(SE):
    query = "SELECT * FROM articles \
    WHERE article_ID = '%s'" % (SE)
    cur.execute(query)
    return cur.fetchall()

#Routes
#Här följer alla routes, dessa kan nås med ett / efter hemsidenamnet.

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')

@route("/")
def index():
    return template("indexdb", articles=get_article('12'))
 
@route("/article")
def articlepage():
    return template("article")

@route("/articlepage/<handler>")
def articlepage():
    return template("articlepage", sin=single_article(handler))

run(app=app)