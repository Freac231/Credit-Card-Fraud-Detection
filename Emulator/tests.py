from validation_functions import card_number_validation, date_validation, cvv_validation, name_validation
from server import hide_card_number

card_numbers = {'0123456789012345': True, '1233': False, 'abc21231': False, '01234567b90123456': False,
                '4580728519274658': True, '45807285192746581321': False}

dates = {'1126': True, '0832': True, '12312': False, '-112': False, '3229': False, '0021': False,
         '1asd': False}

cvvs = {'123': True, 'ahs': False, '12341': False, '000': False, '0': False, '+12': False, '1a2': False}

names = {'Jon Doe': True, 'acasc': False, 'Jon': False, 'Doe': False, 'Jane Doe': True, 'Jane doe Jane': False}


def test_card_number_validation(card_number):
    test = card_number_validation(card_number)

    if test is card_numbers[card_number]:
        return "Passed"
    return "Failed"


def test_date_validation(date):
    test = date_validation(date)

    if test is dates[date]:
        return "Passed"
    return "Failed"


def test_cvv_validation(cvv):
    test = cvv_validation(cvv)

    if test is cvvs[cvv]:
        return "Passed"
    return "Failed"


def test_name_validation(name):
    test = name_validation(name)

    if test is names[name]:
        return "Passed"
    return "Failed"


if __name__ == '__main__':

    print("Testing Card Number Validation Function")
    for i, card_number in enumerate(card_numbers):
        test = test_card_number_validation(card_number)
        print(f"\tTest {i+1}: {test}")

    ##
    print("########################\nTesting Date Validation Function")
    for i, date in enumerate(dates):
        test = test_date_validation(date)
        print(f"\tTest {i+1}: {test}")

    ##
    print("########################\nTesting CVV Validation Function")
    for i, cvv in enumerate(cvvs):
        test = test_cvv_validation(cvv)
        print(f"\tTest {i+1}: {test}")

    print("########################\nTesting Name Validation Function")
    for i, name in enumerate(names):
        test = test_name_validation(name)
        print(f"\tTest {i+1}: {test}")

    ## Testing:
    ## hide_credit_card_number()
    number = '4580409022433922'
    hidden_number = hide_card_number(number)

    print(f"########################\nTesting hide_credit_card_number({number}) --> {hidden_number}")

