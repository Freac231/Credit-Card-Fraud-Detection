import requests


def get_credit_card_info():
    print("Enter payment information:\n", flush=True)

    card_number = input("Card number: ")
    date = input("Date: ")
    cvv = input("CVV: ")
    card_holder_name = input("Card holder name: ")

    return {
        "card_number": card_number,
        "date": date,
        "cvv": cvv,
        "card_holder_name": card_holder_name,
    }


def send_payment(data):
    url = "http://localhost:8080/charge"
    try:
        response = requests.post(url, json=data)

        print(f"[CLIENT] Response from server:\t{response.text}")

    except Exception as e:
        print("[CLIENT] Request failed", str(e))


if __name__ == "__main__":
    cc_data = get_credit_card_info()
    send_payment(cc_data)
