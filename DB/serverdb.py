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

def get_article(amount):
    query = ("SELECT Article_ID, Header, Ingress, Content, Pic_info, time_now FROM articles") 
    cur.execute(query)
    return cur.fetchall()

def create_article():
    query = ("INSERT INTO articles (Header, ingress, content, pic_info) VALUES ('Efter skadorna - MFF lägger locket på', 'Fyra spelare skadade sig i samband med mötet mot Hammarby. Men MFF vill inte ge några uppdateringar kring spelarnas situation. -Går i nuläget inte in på detaljer kring skadorna, skriver MFF:s naprat Wilner Registre i ett sms.', 'Skadeläget i Malmö FF förvärrades avsevärt i samband med matchen mot Hammarby igår. I samtliga fall rör det sig om ljumskskador.Rasmus Bengtsson och Guillermo Molins skadade sig båda på uppvärmingen. Den sistnämnde ströks därmed ur startelvan i sista stund. Vikarierande ytterbacken Oscar Lewicki signalerade direkt för byte i den 70:e minuten och la sig ner på plan. Han lidades men kunde gå av plan utan stöd - och var inte orolig för sin EM-medverkan. – Det är en liten känning i ljumsken, men det känns inte som något allvarligt. Jag ville inte förvärra något, jag gick ut direkt, sa han till Sydsvenskan efter matchen. För Jo Inge Berget rör det sig om samma ljumskskada han ådrog sig i derbyt mot Helsingborgs IF den 8 maj. Han stod över i matchen mot Gefle, men bedömdes spelklar igen till gårdagens möte med Hammarby, men tvingades bryta redan innan paus. - Det högg till i ljumsken och gick inte att spela vidare, sa Berget till Expressen. MFF:s naprapat Wilner Registre var förvånad efter matchen. - Det är väldigt olyckligt och ungefär samma ställe i ljumsken på alla fyra. Men vad det beror på tar vi mer internt, det är inget jag vill spekulera i, sa han till Expressen. Även Guillermo Molins var brydd. - Fyra ljumskskador. Mystiskt, något konstigt är det. Kanske konstgräsmattan. Den är stenhård, sa anfallaren till TT. Om sin egen skada sa Guillermo Molins efter matchen: – Det är såklart tråkigt men förhoppningsvis ska det inte vara så farligt. Vi får se hur allvarligt det är efter bilderna (magnetkameraundersökning) i morgon, sade Molins. När Sydsvenskan når Wilner Registre på torsdagen vill han inte utveckla läget kring skadorna. - I nuläget går jag inte in på detaljer. Övergripande är att det blir behandling, vila och alternativ träning för vissa av våra spelare, skriver MFF-naprapaten i ett sms. Malmö FF flyger tillbaka till Malmö från Stockholm idag. - Kommer se över vissa ytterligare i eftermiddag, skriver Wilner Regsitre. Malmö FF möter Falkenberg hemma på måndag och Östersund borta lördagen därpå.', 'Rasmus Bengtsson, Jo Inget Berget, Guillermo Molins och Oscar Lewicki skadade sig alla i Stockholm i går.')
    cur.execute(query, (Header, ingress, content, pic_info))
    db.commit()


def single_article(SE):
    query = ("SELECT Article_ID, Header, Ingress, Content, Pic_info FROM articles \ ORDER BY time_now ASC") 
    cur.execute(query)
    return cur.fetchall()

#Routes
#Här följer alla routes, dessa kan nås med ett / efter hemsidenamnet.

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')

@route("/")
def index():
    return template("indexdb", articlelist=get_article('12'))
 
@route("/article")
def articlepage():
    return template("article")

@route("/articlepage")
def articlepage():
    return template("articlepage", sin=single_article())

run(app=app)