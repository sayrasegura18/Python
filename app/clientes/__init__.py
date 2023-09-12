from flask import Blueprint
clientes = Blueprint ('clientes',
                       __name__,
                       url_prefix = '/clientes',
                       template_folder = 'templates')

#Vincular el archivo de rutas
from . import routes