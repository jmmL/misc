def get_nyx(words, vowels):
    """ Returns a list of words that lack vowels and have at least one letter "x" or "y"
    """
    nyx_list = ""
    for word in words:
        word = word.lower()
        if not bool(vowels.intersection(word)) and ("x" in word or "y" in word) and "'" not in word:
            nyx_list += word.strip() + ", "
    return nyx_list


def main():
    dictionary_path = "/usr/share/dict/british-englsh-insane"
    vowels = set(["a", "e", "i", "o", "u"])

    try:
        words = open(dictionary_path, "r")
    except OSError as e:
        raise(e)

    print(get_nyx(words, vowels))


if __name__ == "__main__":
    main()
