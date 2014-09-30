def main():
    """ A very naive word-counter"""
    wordy_string = input("Please enter a string:\n")
    alphabet = ["q","w","e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
     "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m",]
    word_count = 0
    for i in range(len(alphabet)):
        if alphabet[i] in wordy_string:
            word_count = 1
    for i in wordy_string:
        if i == " ":
            word_count += 1
    print(word_count)
main()
