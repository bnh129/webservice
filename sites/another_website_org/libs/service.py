import tornado.web

def create(logger, pages_path):
	settings = {
		"static_path": pages_path,
	}

	app = tornado.web.Application([
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

