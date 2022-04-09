from sqlite3 import Error

from .connection import create_connection
from .sql.tables import instructions 

    
def create_tables():
    conn = create_connection() # conectarnos a la base de datos
    
    path = instructions[0]
    
    #read_file(path)
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(path)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at create_tables(): {str(e)}" )
    finally:
        if conn:
            cursor.close()  # cerramos el cursoe
            conn.close()    # cerramos la conexión
            