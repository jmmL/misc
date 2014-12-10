#    print(inputted_operands[0] + 1)
#    print(type(inputted_operands))
#    print(inputted_operands[0] + inputted_operands[1])


def naive_calculator(operator, number_list):
    calculated_output = 0
    if operator == "+":
        calculated_output = sum(number_list)


    elif operator == "*":
        calculated_output = 1
        #reduce(lambda x, y: x * y, number_list)
        for i in number_list:
            calculated_output *= i

    elif operator == "^":
        calculated_output = number_list[0]
        for i in number_list[1:]:
            calculated_output = calculated_output ** i
    else:
        print("Error: operator not recognised")

    return calculated_output


def string_to_list_of_ints(string):
    number_list = string.split()
    number_list = [int(i) for i in number_list]
    return number_list


def main():
    """ This is a rudimentary prefix calculator """
    list_of_operators = ["+", "*", "^", ]
    print("This is a rudimentary prefix calculator. The first 3 goes are free!\nType \"q\" to quit.")
    i = 0
    while i < 3:
        initial_input = input("Please input an expression:\n")
        if "q" in initial_input.lower():
            print("Quiting...")
            break
        
        operator = initial_input[0]

        if operator not in list_of_operators:
            print("Error: operator not recognised")
            break
        
        number_list = string_to_list_of_ints(initial_input[1:])

        print("= " + str(naive_calculator(operator, number_list)))
        i += 1

if __name__ == "__main__":
    main()
