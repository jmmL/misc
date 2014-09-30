def main():
    """ A program for checking whether a string is a palindrome or not"""
    palindrome_string = input("Please enter a string:\n")
    # print(len(palindrome_string))
    
    def is_palindrome(string):
        for i in range(len(string)//2):
           if string[i] != string[len(string)-i-1]:
                return False
                break
            # print(str(i) + " index checked")
        return True
    
    print(is_palindrome(palindrome_string))

main()
