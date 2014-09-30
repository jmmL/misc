def main():
    """ This returns a string in Pig Latin format"""
    string_to_mangle = input("Enter a string:\n")
    def piggy(pig_string):
        if pig_string[0] == "a" or "e" or "i" or "o" or "u":
            pig_string += "way"
            return pig_string
        else:
            pig_string += "-" + pig_string[0] + "ay"
            return pig_string[1:]
        
    print(piggy(string_to_mangle))

main()
