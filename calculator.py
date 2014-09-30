def main():
    """ This is a rudimentary prefix calculator """
    list_of_operators = ["+", "*", "^", ]
#    print(inputted_operands[0] + 1)
#    print(type(inputted_operands))
#    print(inputted_operands[0] + inputted_operands[1])
    
    def naive_calculator(operator,operands):
        if operator == "+":
            calculated_output = 0
            for i in range(len(operands)):
                calculated_output += operands[i]
                
        elif operator == "*":
            calculated_output = 1
            for i in range(len(inputted_operands)):
                calculated_output *= operands[i]
                
        elif operator == "^":
            calculated_output = operands[0]
            for i in range(len(operands) - 1):
                calculated_output = calculated_output ** operands[i+1]
                
        return(calculated_output)
        
    def string_to_ints(string):
        string = string.split()
        string = [int(i) for i in string]
        return(string)
    
    print("This is a rudimentary prefix calculator. The first 3 goes are free!\nType \"q\" to quit.")
    i = 0
    
    while i < 3:
        initial_input = input("Please input an expression:\n")
        if "q" in initial_input or "Q" in initial_input:
            print("Quiting...")
            break
        
        inputted_operator = initial_input[0]
        inputted_operands = initial_input[1:]
        
        if inputted_operator not in list_of_operators:
            print("Error: operator not recognised")
            break
        
        inputted_operands = string_to_ints(inputted_operands)
  
        print("= " + str(naive_calculator(inputted_operator,inputted_operands)))
        i += 1
main()
