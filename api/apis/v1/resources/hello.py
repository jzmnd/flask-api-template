from flask_restx import Resource, Namespace

api = Namespace("hello", description="Saying hello world")


@api.route("/")
class HelloWorld(Resource):
    """Routes for Hello World"""

    def get(self):
        return {"hello": "world"}


@api.route("/extra/<int:happiness>")
@api.param("happiness", "Happiness score")
class HelloWorldExtra(Resource):

    def get(self, happiness):
        return {"hello": "world{}".format("!" * happiness), "happiness": happiness}
