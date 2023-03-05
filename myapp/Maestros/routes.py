from flask import Blueprint

maestros = Blueprint('maestros', __name__)

@maestros.route('/getmeas', methods=['GET'])
def getalum():
    return {'Key':'Maestros'}