from flask import Blueprint
from flask_restx import Api

from .resources.hello import api as hello_api
from .resources.person import api as person_api

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
    blueprint, version="1.0", title="Template API", description="A simple template", doc="/docs/"
)

api.add_namespace(hello_api)
api.add_namespace(person_api)
