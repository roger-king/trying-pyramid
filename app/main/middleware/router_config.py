def includeme(config):
    # Adding hello module routes.
    config.add_route('home','/')
    config.add_route('hello', '/howdy')
    config.scan('..modules.hello.hello_route')

