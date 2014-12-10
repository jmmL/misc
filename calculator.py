import sys


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


def string_to_list_of_ints(string):
    number_list = string.split()
    number_list = [int(i) for i in number_list]
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
        number_list = string_to_list_of_ints(most_nested[1:])
        string = string.replace("(" + most_nested + ")", str(naive_calculator(operator, number_list)))
        return chew_through_nests(string)
    else:
        return string


def check_input(initial_input):
    if initial_input.count("(") == initial_input.count(")") and initial_input.count("(") > 0:
        return True
    else:
        sys.exit("Malformed input. Check your brackets.")


def main():
    """ This is a rudimentary prefix calculator """
    print("This is a rudimentary prefix calculator. The first 3 goes are free!\nType \"q\" to quit.")
    goes = 0
    while goes < 3:
        initial_input = get_input()
        #initial_input = "(+ 2 (^ 3 3) (* 3 2))"

        check_input(initial_input)
        answer = chew_through_nests(initial_input)

        print("= " + answer)
        goes += 1

if __name__ == "__main__":
    main()