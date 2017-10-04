import webapp2
import os
import jinja2
jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class MainHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('index.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class TestHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('test.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class EinsteinHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('einstein.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class EsferaHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('esfera.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class TrapecioHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('trapecio.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class TrianguloHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('triangulo.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class VelocidadHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('velocidad.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class PitagorasHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('pitagoras.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class CuboHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('cubo.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class CilindroHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('cilindro.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class PiramideHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('piramide.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
class FuerzaHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('fuerza.html')
    template_context = {}
    self.response.out.write(template.render(template_context))
app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/test', TestHandler),
  ('/einstein', EinsteinHandler),
  ('/esfera', EsferaHandler),
  ('/trapecio', TrapecioHandler),
  ('/triangulo', TrianguloHandler),
  ('/velocidad', VelocidadHandler),
  ('/pitagoras', PitagorasHandler),
  ('/cubo', CuboHandler),
  ('/cilindro', CilindroHandler),
  ('/piramide', PiramideHandler),
  ('/fuerza', FuerzaHandler)
], debug=True)

