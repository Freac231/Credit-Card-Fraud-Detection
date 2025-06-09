import mysql.connector
from luhn_generator import generate_card_number

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database='credit_card_fraud'
)

cursor = db.cursor()


## Now we can execute queries on the database

def add_honey_token(card_number, date, cvv, card_holder_name):
    cursor.execute("INSERT INTO honey_tokens (card_number, date, cvv, card_holder_name) VALUES (%s, %s, %s, %s)",
                   (card_number, date, cvv, card_holder_name))
    db.commit()


def delete_honey_token(token_id):
    cursor.execute("DELETE FROM honey_tokens WHERE id=%s",
                   (token_id,))
    db.commit()


def is_honey_token(card_number, date, cvv, card_holder_name):
    cursor.execute("SELECT * FROM honey_tokens WHERE card_number=%s AND date=%s AND cvv=%s AND card_holder_name=%s",
                   (card_number, date, cvv, card_holder_name))
    result = cursor.fetchone()

    if result:      ## Token match to the card info
        return True
    return False


def get_honey_token_id(card_number, date, cvv, card_holder_name):
    cursor.execute("SELECT * FROM honey_tokens WHERE card_number=%s AND date=%s AND cvv=%s AND card_holder_name=%s",
                   (card_number, date, cvv, card_holder_name))

    result = cursor.fetchone()
    if result:
        return result[0], result[1]
    return None
