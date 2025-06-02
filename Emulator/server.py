from flask import Flask, request, jsonify
from validation_functions import validate_data
from logger import logger
import db_connection

app = Flask(__name__)


def hide_card_number(number):
    return '************' + number[12:]


def process(data):
    validate_data(data)  ## first we need to validate the data to process it

    is_honey_token = db_connection.is_honey_token(data['card_number'], data['date'], data['cvv'],
                                                  data['card_holder_name'])

    if is_honey_token:
        logger.info('[SERVER] Honey Token Detected')


@app.route("/charge", methods=["POST"])
def charge():
    data = request.json
    try:
        process(data)
        data['card_number'] = hide_card_number(data['card_number'])
        logger.info(f"[SERVER] Received payment request: {data}")

        return jsonify({"status": "received",
                        "message": "Payment processed successfully"})
    except Exception as e:
        logger.error(f"[SERVER] Denied payment request: {e}")
        return jsonify({"status": "failed",
                        "message": str(e)})


if __name__ == "__main__":
    app.run(port=8080, debug=False)
