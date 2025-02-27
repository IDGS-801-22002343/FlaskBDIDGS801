from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField,SubmitField, RadioField
from wtforms import validators

class UserForm(Form):

    id = IntegerField("Id",[
        validators.DataRequired(message="El campo es requerido")
    ])
    nom = StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    ap = StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido")
    ])
    email = EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido")
    ])
