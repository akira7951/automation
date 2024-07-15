import pyodbc
import win32com.client

class ODBC_Connection:
    def __init__(self):
        if not hasattr(self,'pgConn'):
            self.DBConnection()
    
    def GetPDOConnStr(self,sTableName):
        return 'DSN='+sTableName
    
    def DBConnection(self):
        self.pgConn = pyodbc.connect(self.GetPDOConnStr('Deng64'))
    
    def DBClose(self):
        if hasattr(self,'pgConn'):
            self.pgConn.close()
