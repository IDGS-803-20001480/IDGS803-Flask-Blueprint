
import flask

from Alumnos.routes import alumnos
from Directivos.routes import dir
from Maestros.routes import maestros

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return flask.jsonify({'Datos': 'Home'}) #mandar un json

app.register_blueprint(alumnos)
app.register_blueprint(dir)
app.register_blueprint(maestros)

if __name__ == '__main__':
    app.run()
