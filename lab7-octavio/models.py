from protorpc import remote
from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb
#import endpoints

class CustomBaseModel(EndpointsModel):
    def populate(self, data):
        super(self.__class__, self).__init__()
        for attr in self._message_fields_schema:
            if hasattr(data, attr):
                setattr(self, attr, getattr(data, attr))

#####USUARIOS#########
class Usuarios(CustomBaseModel):
    _message_fields_schema = ('email', 'password','nickname','edad','photourl')
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    nickname = ndb.StringProperty()
    edad = ndb.StringProperty()
    photourl = ndb.StringProperty()

class Beers(CustomBaseModel):
    _message_fields_schema = ('marca','tipo','ml','presentacion')
    marca = ndb.StringProperty()
    tipo = ndb.StringProperty()
    ml = ndb.StringProperty()
    presentacion = ndb.StringProperty()

class Foods(CustomBaseModel):
    _message_fields_schema = ('nombre','precio','ingredientes','tiempo')
    nombre = ndb.StringProperty()
    precio = ndb.StringProperty()
    ingredientes = ndb.StringProperty()
    tiempo = ndb.StringProperty()

class Tweets(CustomBaseModel):
    _message_fields_schema = ('usuario','tweet')
    usuario = ndb.StringProperty()
    tweet = ndb.StringProperty()

   

