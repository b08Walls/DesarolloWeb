import webapp2
import os
import jinja2
import json
import sys
from google.appengine.ext import ndb
from models import Usuarios
from models import Tweets
from models import Beers
from models import Foods

##usuarios ################
class ModelClass(object):
 pass

def ObjectClass(obj):
 return obj.__dict__

jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class MainHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('index.html')
    template_context = {}
    self.response.out.write(template.render(template_context))

class CreateUserHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()

    try:
      myEmail = self.request.get('email')
      myPasswd = self.request.get('password')
      myNicknm = self.request.get('nickname')
      myEdad = self.request.get('edad')
      myPhotoU = self.request.get('photourl')

      myNuevoUsuario = Usuarios(email = myEmail, password = myPasswd,nickname = myNicknm, edad = myEdad,photourl = myPhotoU)
      myUsuarioKey = myNuevoUsuario.put()

      c.message = "inserted"
      c.key = myUsuarioKey.urlsafe()
    except:
      c.message = "Exeption.."
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class ReadAllUserHandler(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Controll-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    myList = []
    try:
      lstUsers = Usuarios.query().fetch()
      for i in lstUsers:
        c = ModelClass()
        c.id = i.key.urlsafe()
        c.email = i.email
        c.passwd = i.password
        c.nickname = i.nickname
        c.edad = i.edad
        c.photourl = i.photourl
        myList.append(c)
    except:
        c = ModelClass()
        c.message = "Exception ..."
        myList.append(c)
    json_string = json.dumps(myList, default = ObjectClass)
    self.response.write(json_string)

class ReadOneUserHandler(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()
    try:
      userkey = self.request.get('key')
      id_userkey = ndb.Key(urlsafe=userkey)
      myUser = Usuarios.query(Usuarios.key == id_userkey).get()
      c.key = userkey
      if myUser is not None:
        c.email = myUser.email
        c.passwd = myUser.password
        c.nickname = myUser.nickname
        c.edad = myUser.edad
        c.photourl = myUser.photourl
      else:
        c.message = "error: not found"
    except:
      c.message = "Exception"
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class UpdateUserHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()
    try:
      userkey = self.request.get('key')
      myEmail = self.request.get('email')
      myPasswd = self.request.get('password')
      myNicknm = self.request.get('nickname')
      myEdad = self.request.get('edad')
      myPhotoU = self.request.get('photourl')
      id_userkey = ndb.Key(urlsafe = userkey)
      myUser = Usuarios.query(Usuarios.key == id_userkey).get()
      c.key = userkey
      if myUser is not None:
        myUser.email = myEmail
        myUser.password = myPasswd
        myUser.nickname = myNicknm
        myUser.edad = myEdad
        myUser.photourl = myPhotoU
        myUser.put()
        c.message = "updated"
      else:
        c.message = "error: not found"
    except:
      c.message = "Exception ..."
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class DeleteUserHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin','*')
    self.response.headers['Content-Type'] = 'application/json'

    c = ModelClass()

    try:
      userkey = self.request.get('key')
      id_userkey = ndb.Key(urlsafe = userkey)
      myUser = Usuarios.query(Usuarios.key == id_userkey).get()
      c.key = userkey

      if myUser is not None:
        myUser.key.delete()
        c.message = "DELETED"
      else:
        c.message = "error: not found"
    except:
      c.message = "Exceptionm ..."

    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class AddTweetHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin','*')
    self.response.headers['Content-Type'] = 'application/json'

    c = ModelClass()

    #try:
    myUsuario = self.request.get('usuario')
    myTweet = self.request.get('tweet')

    myNuevoTweet = Tweets(usuario = myUsuario, tweet = myTweet)
    myTweetKey = myNuevoTweet.put()

    c.message = "insertado"
    c.key = myTweetKey.urlsafe()
    #except:
     # c.message = "Exception...."

    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class ReadAllTweets(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin','*')
    self.response.headers['Content-Type'] = 'application/json'

    myList = []
    try:
      lstTwits = Tweets.query().fetch()
      for i in lstTwits:
        c = ModelClass()
        c.id = i.key.urlsafe()
        c.tweet = i.tweet
        c.usuario = i.usuario
        myList.append(c)
    except:
        c = ModelClass()
        c.message = "Exception..."
        myList.append(c)
    json_string = json.dumps(myList, default = ObjectClass)
    self.response.write(json_string)


class ReadOneTweetHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()
    try:
      tweetkey = self.request.get('key')
      id_tweetkey = ndb.Key(urlsafe=tweetkey)
      myTweet = Tweets.query(Tweets.key == id_tweetkey).get()
      c.key = tweetkey
      if myTweet is not None:
        c.tweet = myTweet.tweet
        c.usuario = myTweet.usuario
      else:
        c.message = "error: not found"
    except:
      c.message = "Exception"
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class UpdateTweetHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'

    c = ModelClass()
    try:
      tweetkey = self.request.get('key')
      myTweetM = self.request.get('tweet')
      myUsuario = self.request.get('usuario')
      id_tweetkey = ndb.Key(urlsafe = tweetkey)
      myTweet = Tweets.query(Tweets.key == id_tweetkey).get()
      c.key = tweetkey
      if myTweet is not None:
        myTweet.tweet = myTweetM
        myTweet.usario = myUsuario
        myTweet.put()
        c.message = "updated"
      else:
        c.message = "error: not found"
    except:
      c.message = "Exception ..."
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class DeleteTweetHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin','*')
    self.response.headers['Content-Type'] = 'application/json'

    c = ModelClass()

    try:
      tweetkey = self.request.get('key')
      id_tweetkey = ndb.Key(urlsafe = tweetkey)
      myTweet = Tweets.query(Tweets.key == id_tweetkey).get()
      c.key = tweetkey

      if myTweet is not None:
        myTweet.key.delete()
        c.message = "DELETED"
      else:
        c.message = "error: not found"
    except:
      c.message = "Exceptionm ..."

    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)


class CreateBeerHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()

    try:
      myMarca = self.request.get('marca')
      myTipo = self.request.get('tipo')
      myMl = self.request.get('ml')
      myPresentacion = self.request.get('presentacion')

      myNuevaCerveza = Beers(marca =  myMarca, tipo = myTipo, ml = myMl, presentacion = myPresentacion)
      myCervezaKey = myNuevaCerveza.put()

      c.message = "Guardado"
      c.key = myCervezaKey.urlsafe()
    except:
      c.message = "Error..."
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class ReadAllBeerHandler(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Controll-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    myList = []
    try:
      lstBeers = Beers.query().fetch()
      for i in lstBeers:
        c = ModelClass()
        c.id = i.key.urlsafe()
        c.marca = i.marca
        c.tipo = i.tipo
        c.ml = i.ml
        c.presentacion = i.presentacion
        myList.append(c)
    except:
        c = ModelClass()
        c.message = "Exception ..."
        myList.append(c)
    json_string = json.dumps(myList, default = ObjectClass)
    self.response.write(json_string)

class ReadOneBeerHandler(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()
    try:
      beerkey = self.request.get('key')
      id_beerkey = ndb.Key(urlsafe=beerkey)
      myBeer = Beers.query(Beers.key == id_beerkey).get()
      c.key = beerkey
      if myBeer is not None:
        c.marca = myBeer.marca
        c.tipo = myBeer.tipo
        c.ml = myBeer.ml
        c.presentacion = myBeer.presentacion
      else:
        c.message = "error: chela no encontrada"
    except:
      c.message = "Error..."
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class UpdateBeerHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()
    try:
      beerkey = self.request.get('key')
      myMarca = self.request.get('marca')
      myTipo = self.request.get('tipo')
      myMl = self.request.get('ml')
      myPresentacion = self.request.get('presentacion')
      id_beerkey = ndb.Key(urlsafe = beerkey)
      myBeer = Beers.query(Beers.key == id_beerkey).get()
      c.key = beerkey
      if myBeer is not None:
        myBeer.marca = myMarca
        myBeer.tipo = myTipo
        myBeer.ml = myMl
        myBeer.presentacion = myPresentacion
        myBeer.put()
        c.message = "Chela actualizada"
      else:
        c.message = "error:Chela not found"

    except:
      c.message = "Exception only chela..."

    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class DeleteBeerHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin','*')
    self.response.headers['Content-Type'] = 'application/json'

    c = ModelClass()

    try:
      beerkey = self.request.get('key')
      id_beerkey = ndb.Key(urlsafe = beerkey)
      myBeer = Beers.query(Beers.key == id_beerkey).get()
      c.key = beerkey

      if myBeer is not None:
        myBeer.key.delete()
        c.message = "CERVEZA BORRADA..."
      else:
        c.message = "error: chela not found"
    except:
      c.message = "Exception beer ..."

    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class CreateFoodHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()

    try:
      myNombre = self.request.get('nombre')
      myPrecio = self.request.get('precio')
      myIngredientes = self.request.get('ingredientes')
      myTiempo = self.request.get('tiempo')

      myNuevaCerveza = Foods(nombre =  myNombre, precio = myPrecio, ingredientes = myIngredientes, tiempo = myTiempo)
      myCervezaKey = myNuevaCerveza.put()

      c.message = "Guardado"
      c.key = myCervezaKey.urlsafe()
    except:
      c.message = "Error..."
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class ReadAllFoodHandler(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Controll-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    myList = []
    try:
      lstFoods = Foods.query().fetch()
      for i in lstFoods:
        c = ModelClass()
        c.id = i.key.urlsafe()
        c.nombre = i.nombre
        c.precio = i.precio
        c.ingredientes = i.ingredientes
        c.tiempo = i.tiempo
        myList.append(c)
    except:
        c = ModelClass()
        c.message = "Exception ..."
        myList.append(c)
    json_string = json.dumps(myList, default = ObjectClass)
    self.response.write(json_string)

class ReadOneFoodHandler(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()
    try:
      foodkey = self.request.get('key')
      id_foodkey = ndb.Key(urlsafe=foodkey)
      myFood = Foods.query(Foods.key == id_foodkey).get()
      c.key = foodkey
      if myFood is not None:
        c.nombre = myFood.nombre
        c.precio = myFood.precio
        c.ingredientes = myFood.ingredientes
        c.tiempo = myFood.tiempo
      else:
        c.message = "error: comida no encontrada"
    except:
      c.message = "Error... food"
    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class UpdateFoodHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    c = ModelClass()
    try:
      foodkey = self.request.get('key')
      myNombre = self.request.get('nombre')
      myPrecio = self.request.get('precio')
      myIngredientes = self.request.get('ingredientes')
      myTiempo = self.request.get('tiempo')
      id_foodkey = ndb.Key(urlsafe = foodkey)
      myFood = Foods.query(Foods.key == id_foodkey).get()
      c.key = foodkey
      if myFood is not None:
        myFood.nombre = myNombre
        myFood.precio = myPrecio
        myFood.ingredientes = myIngredientes
        myFood.tiempo = myTiempo
        myFood.put()
        c.message = "Comida actualizada"
      else:
        c.message = "error:Comida not found"

    except:
      c.message = "Exception only comida..."

    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)

class DeleteFoodHandler(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin','*')
    self.response.headers['Content-Type'] = 'application/json'

    c = ModelClass()

    try:
      foodkey = self.request.get('key')
      id_foodkey = ndb.Key(urlsafe = foodkey)
      myFood = Foods.query(Foods.key == id_foodkey).get()
      c.key = foodkey

      if myFood is not None:
        myFood.key.delete()
        c.message = "COMIDA BORRADA..."
      else:
        c.message = "error: comida not found"
    except:
      c.message = "Exception food ..."

    json_string = json.dumps(c, default = ObjectClass)
    self.response.write(json_string)


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/createUser', CreateUserHandler),
  ('/readAllUser', ReadAllUserHandler),
  ('/readOneUser', ReadOneUserHandler),
  ('/updateUser', UpdateUserHandler),
  ('/deleteUser', DeleteUserHandler),
  ('/addTweet',AddTweetHandler),
  ('/readAllTweets',ReadAllTweets),
  ('/readOneTweet',ReadOneTweetHandler),
  ('/updateTweet',UpdateTweetHandler),
  ('/deleteTweet',DeleteTweetHandler),
  ('/createBeer', CreateBeerHandler),
  ('/readAllBeer', ReadAllBeerHandler),
  ('/readOneBeer', ReadOneBeerHandler),
  ('/updateBeer', UpdateBeerHandler),
  ('/deleteBeer', DeleteBeerHandler),
  ('/createFood', CreateFoodHandler),
  ('/readAllFood', ReadAllFoodHandler),
  ('/readOneFood', ReadOneFoodHandler),
  ('/updateFood', UpdateFoodHandler),
  ('/deleteFood', DeleteFoodHandler)

], debug=True)
