from flask import Flask
from database import setup
from resources.tasks import tasks_bp 
from database.sql.config import debug_mode

app = Flask(__name__)   # __name__ --> nos permite saber si el archivo es ejecutado de forma
                        # directa o si es ejecutado desde otro archivo
# creamos la tabla
setup.create_tables()

app.register_blueprint(tasks_bp)


"""Página principal"""
@app.route('/')
def home():
    return 'subiendo el proyecto usando heroku y conectando con base de datos de heroku!'

"""Manejanndo rutas no creadas"""
def not_exist(error):
    return "<h1>Te pasastes compae, esta ruta no existe</h1>", 404


# Decimos que si el archivo es ejecutado de manera directa
if __name__=='__main__':
    app.config.from_object(debug_mode['development'])
    app.register_error_handler(404, not_exist)
    app.run()