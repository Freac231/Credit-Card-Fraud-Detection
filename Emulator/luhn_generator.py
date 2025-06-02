import random


def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_sum = sum(digits[-1::-2])
    even_sum = sum(sum(digits_of(d * 2)) for d in digits[-2::-2])
    return (odd_sum + even_sum) % 10


def is_luhn_valid(card_number):
    return luhn_check(card_number) == 0


def generate_card_number(prefix, length):
    number = prefix
    while len(number) < (length - 1):
        number += str(random.randint(0, 9))

    # Calculate check digit
    for check_digit in range(10):
        if is_luhn_valid(number + str(check_digit)):
            return number + str(check_digit)

