from flask import request
from flask_restx import Resource

from scr.core.equations import EquationsCore
from scr.resource.payload.equations import equations_ns, equations_payload

equations_core = EquationsCore()
analyse_core = AnalyseCore()

class Equations(Resource):
    @equations_ns.expect(equations_payload, validate=True)
    def post(self):
        data = request.get_json()
        result = equations_core.calculate(data)
        return result
class Analyse(Resource):
    @equations_ns.expect(analyse_payload, validate=True)
    def post(self):
        data = request.get_json()
        result = analyse_core.vector(data)
        return result
