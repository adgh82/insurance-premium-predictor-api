from flask import Flask, request
from modelapplication import scale_input, get_prediction


app = Flask(__name__)


@app.route('/respond')
def respond_call():
    return 'I am Alive'


@app.route('/get-premium', methods=['POST'])
def predict_premium():

    request_data = request.get_json()

    req_dict = request_data
    scaled_input = scale_input(req_dict['age'], req_dict['height'], req_dict['weight'],
                               req_dict['diabetic'] == 1, req_dict['bp'] == 1,
                               req_dict['transplant'] == 1, req_dict['chronic'] == 1,
                               req_dict['allergy'] == 1, req_dict['cancer'] == 1, req_dict['surgery'])

    premium = get_prediction(scaled_input)

    return {'premium': round(premium[0], 2)}


if __name__ == '__main__':
    app.run(debug=True)
