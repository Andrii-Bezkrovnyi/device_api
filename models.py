from peewee import CharField, ForeignKeyField, Model
from config import db

class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
        table_name = 'api_user'


class Location(Model):
    name = CharField()

    class Meta:
        database = db
        table_name = 'location'


class Device(Model):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref='devices')
    api_user = ForeignKeyField(User, backref='devices')

    class Meta:
        database = db
        table_name = 'device'

    @staticmethod
    def current_device_info(device):
        return {
            'id': device.id,
            'name': device.name,
            'type': device.type,
            'login': device.login,
            'password': device.password,
            'location_id': device.location.id,
            'api_user_id': device.api_user.id
        }
