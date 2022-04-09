from sqlite3 import Error
import mysql.connector as conexion
from .sql.config import Config

def create_connection():

    conn = None
    
    try:
        conn = conexion.connect( host= Config.host,
                                 user= Config.user,
                                 password= Config.password,
                                 database= Config.database
                                 )
        
    except Error as e:
        print('Error connecting ti database: ' + str(e))
    
    return conn




