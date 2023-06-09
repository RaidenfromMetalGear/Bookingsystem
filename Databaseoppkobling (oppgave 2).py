#import nødvendige moduler
from pymongo import MongoClient
import pymongo

#connect til databasen
database = "db_ak"
CONNECTION_STRING = "mongodb+srv://kvnvg2:Nesna=bra!@cluster1.1da3r.mongodb.net/test"
dbname = MongoClient(CONNECTION_STRING)
def leggbrukerinn():
#legg inn ny bruker
    brukernavn = input("Skriv inn nytt brukernavn: ")
    passord = input("Skriv inn nytt passord: ")

    collection = "Brukere"
    mydb = dbname[database]
    mycol = mydb[collection]
    try:
        bruker = {
            "brukernavn" : brukernavn,
            "passord": passord 
        }
        mycol.insert_one(bruker)
    except Exception as e:
        print(e)


    #print ut brukere
    collection = "Brukere"
    mydb = dbname[database]
    mycol = mydb[collection]
    cursor = mycol
    
    for document in cursor.find():
        print(document)

def booketrom():
#legg inn ny bruker
    rom = input("Skriv inn rom: ")
    dato = input("Skriv inn dato: ")

    collection = "Rom"
    mydb = dbname[database]
    mycol = mydb[collection]
    try:
        rom = {
            "rom" : rom,
            "dato": dato 
        }
        mycol.insert_one(rom)
    except Exception as e:
        print(e)


    #print ut brukere
    collection = "Rom"
    mydb = dbname[database]
    mycol = mydb[collection]
    cursor = mycol
    
    for document in cursor.find():
        print(document)

leggbrukerinn()
booketrom()