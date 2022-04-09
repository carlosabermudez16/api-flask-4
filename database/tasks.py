"""Interactuamos con la base de datos"""
from sqlite3 import Error
from .connection import create_connection

"""Mostrar todos datos de la base de datos"""
def select_all_tasks():
    conn = create_connection()
    
    sql = "SELECT * FROM tasks"

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        
        resultado = cursor.fetchall()
        
        return resultado
    except Error as e:
        print(f'Error at select_all_tasks: {str(e)}')
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()


"""Inserta datos"""
def insert_task(title,created_date):
    conn = create_connection()
    
    try:
        cursor = conn.cursor(dictionary=True)
        valores = (title,created_date)
        
        sql = "insert into tasks(title,created_date) VALUES(%s,%s)"
        cursor.execute(sql,valores)
        conn.commit()
        
        return cursor.lastrowid     # retorna el id del registro 
    except Error as e:
        print(f"Error at insert_task(): {str(e)}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

"""Mostrar datos del último registro"""
def select_task_by_id(_id):
    conn = create_connection()
    
    sql = f"SELECT * FROM tasks WHERE id = {_id}"
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        resultado = cursor.fetchone()
        print(resultado)

        return resultado
    except Error as e:
        print(f'Error at select_task_by_id: {str(e)}')
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

"""Actualizar datos"""
def update_task(_id,title):
    conn = create_connection()
    
    sql = "UPDATE tasks SET title=%s WHERE id=%s"
    data = (title,_id)
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, data)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at update_task(): {str(e)}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()
    
"""Eliminar dato"""
def delete_task(_id):
    conn = create_connection()
    
    sql = f"DELETE FROM tasks WHERE id={_id}"

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        conn.commit()
        return True
        
    except Error as e:
        print(f"Error at delete_task(): {str(e)}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

"""Completar Tareas """
def complete_task(_id, completed):
    conn = create_connection()
    
    sql = f"""UPDATE tasks SET completed = {completed}
              WHERE id = {_id}
           """
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at completed_task(): {str(e)} ")
    finally:
        if conn:
            cursor.close()
            conn.close()
    

