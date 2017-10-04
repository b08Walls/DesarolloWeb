import webapp2
import os
import jinja2
import json
import sys
from google.appengine.ext import ndb
from models import Usuarios
from models import Tweets

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
  ('/deleteTweet',DeleteTweetHandler)
], debug=True)
