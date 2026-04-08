import mysql.connector

def connetti():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "Chinook"
    )
    
    return db

def interroga(db, query):
    #query = f"select * from {tabella};"
    cursore = db.cursor()
    cursore.execute(query)
    results = cursore.fetchall()
    cursore.close()
    return results

def main():
    db = connetti()
    if db:
        print("Connesso con successo")
        risultati_query = interroga(db, "select * from employee;")
        print(risultati_query)
    else:
        print("Connessione non riuscita")
        
    
    
if __name__ == "__main__":
    main()