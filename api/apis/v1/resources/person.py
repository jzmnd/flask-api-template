from flask_restx import Resource, Namespace

api = Namespace("person", description="Saying hello to a person")


@api.route("/<name>")
@api.param("name", "The person's name")
class HelloPerson(Resource):
    """Routes for Hello Person"""

    def get(self, name):
        return {"hello": name}
