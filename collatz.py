def collatz_count(number):
    step_count = 1
    number_history = ""

    while number > 1:
        number_history += str(int(number)) + "->"
        if number % 2:
            number = 3 * number + 1
        else:
            number /=  2
        step_count += 1

    number_history += "1"
    return number_history, step_count

if __name__ == "__main__":
    collatz_number = 499999999999999999999999999999999999999999999999999999999
    collatz_information = collatz_count(collatz_number)
    print(str(collatz_information[1]) + " steps\nTimeline: " + str(collatz_information[0]))
