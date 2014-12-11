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
        # self.assertFalse(credit_card_check(0123456789024568))

    def test_true_cards(self):
        self.assertTrue(credit_card_check("9384 3495 3297 0121"))
        self.assertTrue(credit_card_check("0123 4567 8902 4568"))


def check_length(card_number):
    if len(card_number) != 19:
        return False
    else:
        return True


def check_digits(card_number):
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
    total = 0
    for i in range(0, len(card_number)):
        if card_number[i].isdigit():
            total += int(card_number[i])

    # If the sum of all 16 digits is evenly divisible by 10, then return True, else return False
    if total % 10 == 0:
        return True
    else:
        print("Sum was not evenly divisible by 10 (total: " + str(total) + ")")
        return False


def credit_card_check(card_number):
    """Validates card numbers to ensure they are of the form "#### #### #### ####" where each # is a digit and the
    sum of all digits is divisible evenly by 10
    """

    return check_length(card_number) and check_digits(card_number) and check_sum(card_number)


def main():
    print(credit_card_check("9384 3495 3297 0121"))


if __name__ == "__main__":
    main()