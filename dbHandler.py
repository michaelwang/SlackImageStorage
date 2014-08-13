import pg

class DBHandler:
    def __init__(self):
        self.connection = self.get_db_connection()

    def excute(self,query):
       return self.connection.query(query)

        
    def get_db_connection(self):
        try:
           conn = pg.connect(dbname = 'filesCenter', host = 'localhost', user = 'postgres', passwd = '123123')
        except Exception, e:
           print e.args[0]
           return    
        return conn        

   
