#! /usr/bin/env python3
import sys
import unittest


def naive_calculator(operator, number_list):
    if operator == "+":
        calculated_output = sum(number_list)

    elif operator == "*":
        calculated_output = 1
        for i in number_list:
            calculated_output *= i

    elif operator == "^":
        calculated_output = number_list[0]
        for i in number_list[1:]:
            calculated_output = calculated_output ** i
    else:
        sys.exit("Error: operator not recognised")

    return calculated_output


def string_to_list_of_floats(string):
    number_list = string.split()
    try:
        number_list = [float(i) for i in number_list]
    except ValueError:
        print("Complex numbers are not currently supported")
        raise
    return number_list


def get_input():
    initial_input = input("Please input an expression:\n")
    if "q" in initial_input.lower():
        sys.exit("Quiting...")
    return initial_input


def find_most_nested_expression(string):
    index_2 = string.index(")")
    index_1 = string.rindex("(", 0, index_2)
    return string[index_1 + 1:index_2]


def chew_through_nests(string):
    #print(string)

    if ")" in string:
        most_nested = find_most_nested_expression(string)
        operator = most_nested[0]
        number_list = string_to_list_of_floats(most_nested[1:])
        string = string.replace("(" + most_nested + ")", str(naive_calculator(operator, number_list)))
        return chew_through_nests(string)
    else:
        return float(string)


def check_input(initial_input):
    if initial_input.count("(") == initial_input.count(")") and initial_input.count("(") > 0:
        return True
    else:
        sys.exit("Malformed input. Check your brackets.")


class MyCalculatorTests(unittest.TestCase):
    def test_find_most_nested_expression(self):
        test_expression = "(+ 3 (^ 2 4)"
        self.assertEqual(find_most_nested_expression(test_expression), "^ 2 4")

    def test_string_to_list_of_floats(self):
        test_string = "3 2 4 5"
        test_complex_string = "3+4j 1 2-1j"
        self.assertEqual(string_to_list_of_floats(test_string), [3, 2, 4, 5])
        self.assertRaises(ValueError, string_to_list_of_floats, test_complex_string)

    def test_naive_calculator(self):
        test_number_list = [1, 3, 4, 5]
        test_floats_and_negatives = [-2, 1, 0.5, 7.6]
        test_complex_number_list = [-1, 0.5]
        self.assertEqual(naive_calculator("*", test_number_list), 60)
        self.assertEqual(naive_calculator("+", test_number_list), 13)
        self.assertEqual(naive_calculator("^", test_number_list), 1)
        self.assertEqual(naive_calculator("+", test_floats_and_negatives), 7.1)
        self.assertEqual(naive_calculator("*", test_floats_and_negatives), -7.6)
        self.assertAlmostEqual(naive_calculator("^", test_complex_number_list), 0+1j)

    def test_chew_through_nests(self):
        test_nest = "(+ 2 (^ 3 3) (* 3 2))"
        test_complex_nest = "(+ (^ -1 0.5) 2)"
        test_lots_of_nests = "(* (+ 3 4 5 (^ 2 6) (* 3 4 0) (* 1 2 8) (+ (+ 2 3) (+ 9 0 (* 2 7) (* 14 0.5)))) 2)"
        self.assertEqual(chew_through_nests(test_nest), 35.0)
        self.assertRaises(ValueError, chew_through_nests, test_complex_nest)
        self.assertEqual(chew_through_nests(test_lots_of_nests), 254.0)


def main():
    """ This is a prefix calculator """
    print("This is a prefix calculator. The first 3 goes are free!\nType \"q\" to quit.")
    goes = 0
    while goes < 3:
        initial_input = get_input()
        #initial_input = "(+ 2 (^ 3 3) (* 3 2))"

        check_input(initial_input)
        answer = chew_through_nests(initial_input)

        print("= " + str(answer))
        goes += 1

if __name__ == "__main__":
    main()