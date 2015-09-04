from importlib import import_module
from os import path, listdir


def create_app():
    app = Application()
    plugin_dir = path.join(path.dirname(__file__), 'plugins')

    for d in listdir(plugin_dir):
        if path.isdir(path.join(plugin_dir, d)) and not d.startswith('__'):
            module = import_module(''.join(['.plugins.', d]), __package__)
            app.plugins.update({module.__name__.split('.')[-1]: module})

    print("{} plugins loaded.".format(len(app.plugins)))
    return app


class Application:
    def __init__(self):
        self.plugins = {}
