from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email, Length

class BaseClientesForm(FlaskForm):
    username = StringField("Digite el nombre del cliente:", validators=[
        InputRequired(message="Nombre del cliente requerido"),
        Length(min=8, max=10, message="El nombre debe tener entre 8 y 10 caracteres.")
    ])
    password = StringField("Digite la contraseña del cliente:", validators=[
        InputRequired(message="Contraseña del cliente requerida"),
        Length(min=8, max=10, message="La contraseña debe tener entre 8 y 10 caracteres.")
    ])
    email = StringField("Digite el email del cliente:", validators=[
        InputRequired(message="Email del cliente requerido"),
        Email("Debe ser un email válido.")
    ])

class RegistrarClientesForm(BaseClientesForm):
    pass

class NewClientesForm(BaseClientesForm):
    submit = SubmitField("Guardar")

class EditClientesForm(BaseClientesForm):
    submit = SubmitField("Actualizar")
