from flask import request, make_response, jsonify, Blueprint
from flask_restplus import Resource, fields, Api

example_api = Api(Blueprint('api', __name__))
example_name_space = example_api.namespace('example', description='Example APIs')


@example_name_space.route("/")
class ExampleEndpoint(Resource):

    @staticmethod
    def __success(payload):
        return jsonify({
            "status": True,
            "payload": payload
        })

    @staticmethod
    def __failure(errors):
        return jsonify({
            "status": False,
            "errors": errors
        })

    @example_api.doc(responses={200: 'Ok',
                                500: 'Internal Server Error'})
    def get(self):
        return make_response(self.__success([]), 200)

    model = example_api.model("arguments", {
        "arg": fields.String(required=True)
    })

    @example_api.doc(responses={200: 'Ok',
                                400: 'Invalid Argument',
                                500: 'Internal Server Error'},
                     body=model)
    def post(self):
        if request.is_json:
            payload = request.get_json()
            return make_response(self.__success(payload), 200)
        else:
            return make_response(self.__failure("Bad request"), 400)

    parser = example_api.parser()
    parser.add_argument('id', type=str, required=True, help='id')

    @example_api.doc(responses={200: 'Ok',
                                404: 'Not Found',
                                500: 'Internal Server Error'},
                     parser=parser)
    def delete(self):
        return make_response(self.__success(request.form.get("id")), 200)
