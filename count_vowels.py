def main():
    vowel_string = input("Please enter a string:\n")
    count = 0
    vowels = ["a","e","i","o","u","A","E","I","O","U",]
    for letter in vowel_string:
        if letter in vowels:
            count += 1
    print(count)

main()
