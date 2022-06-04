
from flask import Flask
from flask_restx import Api

from scr.resource.equations import Equations
from scr.resource.payload.equations import equations_ns

# configs
app = Flask(__name__)
api = Api(app)

# namespaces
api.add_namespace(equations_ns)
api add_namespace(analyse_ns)

# routes
equations_ns.add_resource(Equations, '')
analyse_ns.add_resource(Analyse,'')
