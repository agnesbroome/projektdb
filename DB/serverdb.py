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
    query = "SELECT Header, Ingress, Content, Pic_info FROM Articles"
    cur.execute(query)
    return cur.fetchall()

def create_article():
    query = ("INSERT INTO articles (Header, Ingress, Content, Pic_info) VALUES ('Malmöpar blåste försäkringsbolag åtta gånger på ett år', 'En nyårsraket i foten, en spik i stortån och en arm som fastnade i en klädmangel. Malmöparet fick gång på gång ut pengar från sitt försäkringsbolag efter olika olyckor. Nu döms paret för en lång rad försäkringsbedrägerier.', 'År 2014 var ett oturens år för den 27-åriga kvinnan och hennes make, att döma av deras korrespondens med försäkringsbolaget. Förutom de nämnda olyckorna ska kvinnan även ha fått kokande vatten över sig och, ramlat i trapphuset och spräckt trumhinnan – samt brutit benet när hon fastnat i en grop under en joggingtur i Pildammsparken.Totalt anmälde paret tio olika olycksfallsskador – och ett inbrott i sitt källarförråd. Och i åtta av fallen fick paret pengar utbetalda, totalt runt 60 000 kronor. Försäkringsutredningen om den felriktade raketen som träffade kvinnans fot var ännu inte färdigställd när misstankarna mot dem uppdagades.', 'Paret anmälde bland annat en nyårsraket som skulle ha landat på kvinnans fot. Bild: HENRIK MONTGOMERY / TT')")
    cur.execute(query, (Header, Ingress, Content, Pic_info))
    db.commit()

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')

@route("/")
def index():
    return template("indexdb", articles=get_article())
 
@route("/article")
def articlepage():
    return template("article")






#Routes
#Här följer alla routes, dessa kan nås med ett / efter hemsidenamnet.


run(app=app)