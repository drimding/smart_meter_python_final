from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import ValidationError

from smartMeter_server_app.models.user_model import User


# Custom validator
def input_validation(data):
    if not data:
        raise ValidationError("Data not provided.")


class UserSchema(SQLAlchemyAutoSchema):
    username = auto_field(validate=input_validation)
    email = auto_field(validate=input_validation)
    password = auto_field(validate=input_validation)

    class Meta:
        model = User
        exclude = ('id', 'is_admin', 'homes')
        load_instance = True
        load_only = ('password',)