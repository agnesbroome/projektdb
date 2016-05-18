#coding:utf-8
from bottle import *
import MySQLdb
import sys

#log in to database


#APP
#Variable that runs with the server file.
app = app()

#Link to the static file with images, javascript, css
@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')

@route("/")
def index():
    return template("indexdb")
 
@route("articlepage")
def articlepage():
    return template("articlepage")






#Routes
#Här följer alla routes, dessa kan nås med ett / efter hemsidenamnet.


run(app=app)