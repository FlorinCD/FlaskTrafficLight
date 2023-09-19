from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse, abort
import logging

logging.basicConfig(filename='florin.log', filemode='a', encoding='utf-8', level=logging.DEBUG)


app = Flask(__name__)
api = Api(app)

curr_states_put_args = reqparse.RequestParser()
curr_states_put_args.add_argument("s1", type=str, help="First value required!", required=False)
curr_states_put_args.add_argument("s2", type=str, help="Second value required!", required=False)
curr_states_put_args.add_argument("cc", type=str, help="Second value required!", required=False)

curr_states = {0: {0:"0", 1:"1", 2: 0}}  # state1 : string, state2: string, car_count: int
paramsInfoTeatru = ["Red", "Green", 0]
states = []


# add pages here
@app.route('/')
def index():
    global states
    return render_template("home.html", names=states)


@app.route('/home')
def home():
    global states
    return render_template("home.html", names=states)


@app.route('/info')
def info():
    global states
    return render_template("info.html", names=states)


@app.route('/discover')
def discover():
    return render_template("discover.html", names=states)


@app.route('/infoTeatru')
def infoTeatru():
    global paramsInfoTeatru
    return render_template("infoTeatru.html", names=paramsInfoTeatru)


@app.route('/apiFlorin', methods=['GET'])
def api_florin():
    args = [i for i in request.args.keys()]  # list with parameters
    d = {element: request.args.get(str(element)) for element in args}  # dict with parameter: argument(using get method)
    logging.info(f'Am primit datele {d}')  # display info in log
    return render_template("apiFlorin.html", names=d)


@app.route('/apiFlorin2', methods=['POST'])
def api_florin2():
    try:
        print(f"test3: {request.data}")
    except Exception as ex:
        print(f"Date eronate:{ex}")
    args = [i for i in request.args.keys()]
    for i in request.args.keys():
        print(f"Date {i}")
    d = {element: request.args.post(str(element)) for element in args}
    logging.info(f'Am primit datele {d}')
    return render_template("apiFlorin.html", names=d)


class State(Resource):

    def get(self, state_id):
        if state_id in curr_states:
            return curr_states[state_id]
        else:
            return abort(404, message="Not a good id!")

    def put(self, state_id):
        curr_states[state_id] = curr_states_put_args.parse_args()
        paramsInfoTeatru[0], paramsInfoTeatru[1], paramsInfoTeatru[2] = curr_states[state_id]["s1"], curr_states[state_id]["s2"], curr_states[state_id]["cc"]
        return curr_states[state_id], 201


api.add_resource(State, "/state/<int:state_id>")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

