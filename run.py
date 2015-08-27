from app import create_app
from pprint import PrettyPrinter


app = create_app()

app.plugins['toaster'].do_plugin_stuff()

printer = PrettyPrinter(indent=4)
printer.pprint(app.plugins.__repr__())
