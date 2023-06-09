#import nødvendige moduler
from pymongo import MongoClient
import pymongo

#connect til databasen
database = "db_ak"
CONNECTION_STRING = "mongodb+srv://kvnvg2:Nesna=bra!@cluster1.1da3r.mongodb.net/test"
dbname = MongoClient(CONNECTION_STRING)


#meny
def meny():
    print("1: Book et rom ")
    print("2: Registrer ny bruker ")
    print("3: Slett en booking ")
    print("4: List ut alle rom")

#funksjon for å logge på først før main
def login():
    while True:
        brukernavn = input("Skriv inn brukernavn")
        passord = input("Skriv inn passord")
        #kode her som sjekker opp mot database at brukernavn & passord er korrekt
        login = True
        try:
            if login == True:
                break
            
            elif login == False:
                print("Feil passord eller brukernavn, prøv på nytt.")
                input("")
        except Exception as e:
            print(e)

#funksjon for book et rom
def booketrom():
    rom = input("Hvilket rom vil du booke?: ")
    dato = input(f"Hvilken dato vil du booke " + rom + "?: ")
    #kode her som sjekker om rom er tilgjengelig
    #hvis tilgjengelig
    collection = "Rom"
    mydb = dbname[database]
    mycol = mydb[collection]
    try:
        bookrom = {
            "rom" : rom,
            "dato": dato 
        }
        mycol.insert_one(bookrom)
    except Exception as e:
        print(e)
    
    #hvis rom ikke er tilgjengelig
    print("Rom ikke tilgjengelig, vennligst velg annet rom eller dato.")

#funksjon registrer ny bruker
def regbruker():
    brukernavn = input("Skriv inn brukernavn på ny bruker: ")
    passord = input("skriv inn passord på bruker: ")
    #kode her som sjekker om rom er brukernavn er tilgjengelig
    #hvis tilgjengelig
    collection = "brukere"
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

#list ut alle rom
def listutrom():
    collection = "Rom"
    mydb = dbname[database]
    mycol = mydb[collection]
    cursor = mycol
  
    for document in cursor.find():
        print(document)

#rediger en booking
def slettbooking():
    romnr = input("Skriv inn romnummer på booking du vil redigere: ")
    
    #kanskje legge til tilfeldig id eller passord som kommer med hvert rom som bare person som booker vet om
    #sånn at folk kanke bare gå å kuke rundt med andre rom

    #if romnr korrekt med id / passord
    collection = "Rom"
    mydb = dbname[database]
    mycol = mydb[collection]
    #slett booking
    mycol.delete_one({"rom" : romnr})

    #if romnr feil eller id / passord feil
    print("feil romnmr / passord.")


#main
def main():
    while True:
        meny()
        valg = input(": ")
        if valg == "1":
            booketrom()
        elif valg == "2":
            regbruker()
        elif valg == "3":
            slettbooking
        elif valg == "4":
            listutrom
        elif valg == "5":
            break
        else:
            print("ugyldig input.")
    

#kjør program

login()
main()