import mysql.connector


class DBConnection(object):
    def __init__(self, user='admin', password='sMgKLRX2PjmX',host='192.168.59.103', port='8036',database='test'):
        cnx = mysql.connector.connect(user=user, password=password,host=host, port=port,database=database)
        self.DBConnection = cnx
    def getConnection(self):
        return self.DBConnection
    def closeConnection(self):
        return self.DBConnection.close()
