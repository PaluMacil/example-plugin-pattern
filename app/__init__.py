from importlib import import_module
from os import path, listdir


def create_app():
    app = Application()
    plugin_dir = path.join(path.dirname(__file__), 'plugins')

    import_string_list = [''.join(['.plugins.', d]) for d
                          in listdir(plugin_dir)
                          if path.isdir(path.join(plugin_dir, d))
                          and not d.startswith('__')]

    print(str(len(import_string_list)) + " imports to do...")

    for import_string in import_string_list:
        module = import_module(import_string, __package__)
        app.plugins.update({module.__name__.split('.')[2]: module})

    print(str(len(app.plugins)) + " plugins in the app")
    return app


class Application:
    def __init__(self):
        self.plugins = {}
