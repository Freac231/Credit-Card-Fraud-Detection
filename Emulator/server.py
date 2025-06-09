from flask import Flask, request, jsonify
from pywin.dialogs import status

from validation_functions import validate_data
from logger import logger
import db_connection

app = Flask(__name__)


def hide_card_number(number):
    return '************' + number[12:]


def process(data, req=None):
    validate_data(data)  ## first we need to validate the data to process it

    is_honey_token = db_connection.is_honey_token(data['card_number'], data['date'], data['cvv'],
                                                  data['card_holder_name'])

    if is_honey_token:
        token_id, card_number = db_connection.get_honey_token_id(data['card_number'], data['date'], data['cvv'],
                                                    data['card_holder_name'])

        logger.info(f"[SERVER] Honey Token Detected\n"
                    f"\t HONEY TOKEN ID: {token_id}\n"
                    f"\t CARD NUMBER: {card_number}\n"
                    f"\t REQUEST IP: {req.remote_addr}\n"
                    f"\t USER: {req.remote_user}")


@app.route("/charge", methods=["POST"])
def charge():
    data = request.json
    try:
        process(data, req=request)
        data['card_number'] = hide_card_number(data['card_number'])
        logger.info(f"[SERVER] Received payment request: {data}")

        return jsonify({"status": "received",
                        "message": "Payment processed successfully"})
    except Exception as e:
        logger.error(f"[SERVER] Denied payment request: {e}\n\tData: {data}")
        return jsonify({"status": "failed",
                        "message": str(e)})


if __name__ == "__main__":
    app.run(port=8080, debug=False)
