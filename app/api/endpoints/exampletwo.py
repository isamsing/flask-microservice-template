from flask import request, make_response, jsonify
from flask_restplus import Resource, fields, Namespace

example_two_name_space = Namespace('exampletwo', description='Example APIs')


@example_two_name_space.route("/")
class ExampleTwoEndpoint(Resource):

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

    @example_two_name_space.doc(responses={200: 'Ok',
                                           500: 'Internal Server Error'})
    def get(self):
        return make_response(self.__success([]), 200)

    model = example_two_name_space.model("arguments", {
        "arg": fields.String(required=True)
    })

    @example_two_name_space.doc(responses={200: 'Ok',
                                           400: 'Invalid Argument',
                                           500: 'Internal Server Error'},
                                body=model)
    def post(self):
        if request.is_json:
            payload = request.get_json()
            return make_response(self.__success(payload), 200)
        else:
            return make_response(self.__failure("Bad request"), 400)

    parser = example_two_name_space.parser()
    parser.add_argument('id', type=str, required=True, help='id')

    @example_two_name_space.doc(responses={200: 'Ok',
                                           404: 'Not Found',
                                           500: 'Internal Server Error'},
                                parser=parser)
    def delete(self):
        return make_response(self.__success(request.form.get("id")), 200)
