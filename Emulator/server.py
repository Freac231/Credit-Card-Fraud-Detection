from flask import Flask, request, jsonify

app = Flask(__name__)


def card_number_validation(card_number):
    if len(card_number) != 16:
        return False
    elif not card_number.isdigit():
        return False
    return True


def date_validation(date):
    if len(date) != 4 or not date.isdigit():    ## basic length check and that it consists of numbers
        return False

    month = int(date[0:2])
    year = int(date[2:4])

    if month not in range(1, 13):
        return False
    elif year < 25:
        return False
    return True


def cvv_validation(cvv):
    if not cvv.isdigit():
        return False

    cvv_int = int(cvv)

    if cvv_int not in range(1, 1000):
        return False
    return True


def name_validation(name):
    try:
        names = name.split(" ")
        if len(names) != 2:     ## only first and last names are allowed
            return False
    except ValueError:
        return False

    return True


def process(data):
    card_number, date, cvv, card_holder_name = data.values()

    if not card_number_validation(card_number):
        raise Exception("Invalid Card Number")
    elif not date_validation(date):
        raise Exception("Invalid Date")
    elif not cvv_validation(cvv):
        raise Exception("Invalid CVV")
    elif not name_validation(card_holder_name):
        raise Exception("Invalid Name")


@app.route("/charge", methods=["POST"])
def charge():
    data = request.json
    try:
        process(data)
        print(f"[SERVER] Received payment request:\n{data}")
        return jsonify({"status": "received",
                        "message": "Payment processed successfully"})
    except Exception as e:
        print(f"[SERVER] Denied payment request:\n  Error: {e}")
        return jsonify({"status": "failed",
                        "message": str(e)})


if __name__ == "__main__":
    app.run(port=8080, debug=False)
