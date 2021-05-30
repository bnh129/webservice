import tornado.web
import tornado.template

class MainHandler(tornado.web.RequestHandler):

	def initialize(self, path, logger):
		self.path = path
		self.logger = logger
		self.logger.info("Initialized.")

	def get(self):
		self.render(self.path + 'index.html')
