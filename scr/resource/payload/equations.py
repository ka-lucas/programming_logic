from flask_restx import Namespace, fields

# Namespace
equations_ns = Namespace('equations')
analyse_ns = Namespace('analyse')

# Payload
equations_payload = equations_ns.model('EquationsPayload', {
    'number': fields.Integer(required=True)
}, strict=True)

analyse_payload = analyse_ns.model('AnalysePayload', {
    'number': fields.Integer(required=True)
}, strict=True)