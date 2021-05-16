from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from smartMeter_server_app.models.smartMeter_model import SmartMeter


class SmartMeterSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SmartMeter
        exclude = ('id', 'home_id')
        load_instance = True
        include_fk = True
