from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField ,SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import  InputRequired, NumberRange

class Productoform():
    nombre = StringField("Nombre del producto:", validators = [InputRequired(message = "Nombre del producto requerido")])
    precio = IntegerField("Precio del producto:", validators = [InputRequired(message = "Precio del producto requerido"),
                                                                NumberRange( min = 10,
                                                                             max = 10000,
                                                                       message = "Precio Fuera del rango" )])

    
class NewProductForm(FlaskForm, Productoform):
    imagen = FileField("Seleccione la imagen del producto", validators = [
                                                            FileRequired(message = "Debe seleccionar una imagen"),
                                                            FileAllowed(['jpg' , 'png'], 
                                                                        "Solo se permiten imagenes")])
    submit = SubmitField("Guardar")
    
    
class EditProductoForm(FlaskForm, Productoform):
     submit = SubmitField("Actualizar")