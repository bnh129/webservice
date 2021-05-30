import tornado.web
import sites.my_webapp_com.libs.SiteHandlers as site

def create(logger, pages_path):
	settings = {
		"static_path": pages_path,
	}

	app = tornado.web.Application([
		(
            r"/",
            site.MainHandler,
            dict(
				path=settings['static_path'],
				logger=logger,
			),
		),    
		(
			r"/(.*)",
			tornado.web.StaticFileHandler,
			dict(
				path=settings['static_path'],
				default_filename="index.html",
			),
		),
	], **settings)

	return app

