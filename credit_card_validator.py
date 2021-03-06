import unittest


class MyCreditCardTests(unittest.TestCase):
    def test_bad_sum(self):
        self.assertFalse(credit_card_check("2768 3424 2345 2358"))

    def test_invalid_format(self):
        self.assertFalse(credit_card_check("0000000000000000"))
        self.assertFalse(credit_card_check("1876 0954 325009182"))
        self.assertFalse(credit_card_check(" 5555 5555 5555 5555"))
        self.assertFalse(credit_card_check("0000 0000 0000 000"))
        self.assertFalse(credit_card_check(""))
        self.assertFalse(credit_card_check("0000 0000"))
        self.assertFalse(credit_card_check("0123 4567 89AB EFGH"))
        self.assertFalse(credit_card_check("0000 000000000000"))
        self.assertFalse(credit_card_check(9384349532970121))

    def test_true_cards(self):
        self.assertTrue(credit_card_check("9384 3495 3297 0121"))
        self.assertTrue(credit_card_check("0123 4567 8902 4568"))


def check_length(card_number):
    """ Checks that the length of the str card_number is 19 exactly
    :param card_number: str
    :return: bool
    """
    if len(card_number) == 19:
        return True
    else:
        return False


def check_digits(card_number):
    """ Checks that the first 4 chars of the str card_number are digits followed by the 5th char being a space,
    and so on. Returns True if these conditions are met, and otherwise returns False
    :param card_number: str
    :return: bool
    """
    for i in range(0, len(card_number)):
        # The first 4 chars must be digits (and so on)
        if (i + 1) % 5 > 0 and not card_number[i].isdigit():
            print("Char wasn't a digit")
            return False

        # Every 5th char must be a space
        elif (i + 1) % 5 == 0 and not card_number[i].isspace():
            print("Char wasn't a space")
            return False
    else:
        return True


def check_sum(card_number):
    """ This function will return true if the sum of all digits in the string card_number is evenly divisible by
    a magic_number, 10
    :param card_number: str
    :return: bool
    """
    total = 0
    magic_number = 10

    for i in range(0, len(card_number)):
        if card_number[i].isdigit():
            total += int(card_number[i])

    # If the sum of all digits is evenly divisible by 10 (the magic number), then return True, else return False
    if total % magic_number == 0:
        return True
    else:
        print("Sum was not evenly divisible by %i (total: %s)" % (magic_number, total))
        return False


def credit_card_check(card_number):
    """ Validates card numbers to ensure they are of the form "#### #### #### ####" where each # is a digit and the
    sum of all digits is divisible evenly by 10
    :param card_number: str
    :return: bool
    """

    # Check that we've been given a card number in the right type (a string)
    if type(card_number) is not str:
        return False
    else:
        return check_length(card_number) and check_digits(card_number) and check_sum(card_number)


def main():
    print(credit_card_check("9384 3495 3297 0121"))


if __name__ == "__main__":
    main()