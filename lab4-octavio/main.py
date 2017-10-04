
import webapp2
import os
import jinja2


#permite acceso al sistema de archivos
jinja_env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_env.get_template('index.html')
		template_context = {}
		self.response.out.write(template.render(template_context))

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)