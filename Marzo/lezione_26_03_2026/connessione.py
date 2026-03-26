import mysql.connector

class Connessione:
    
    def __init__(self):
        pass

    def connetti(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'magazzino'
        )
        
        if self.db:
            print("Sei connesso al DB")
            return self.db
        else:
            print("Non connesso")

    def chiudi(self):
        if self.db.is_connected():
            self.db.close()

if __name__ == '__main__':
    conn = Connessione
    conn.connetti()
    conn.chiudi()
