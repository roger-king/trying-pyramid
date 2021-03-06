from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('.middleware.router_config')
    return config.make_wsgi_app()
