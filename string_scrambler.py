import random
import unittest


def randomise_letters(letters):
    letters_list = list(letters)
    random.shuffle(letters_list)
    return "".join(letters_list)


def scramble_word(word):
    if not word[-1].isalpha():
        return scramble_word(word[0:-1]) + word[-1]
    if len(word) < 4:
        return word
    else:
        return word[0] + randomise_letters(word[1:-1]) + word[-1]


def scramble_phrase(phrase):
    phrase = phrase.strip()
    shuffled_phrase = []
    word_list = phrase.split(" ")
    for word in word_list:
        shuffled_phrase.append(scramble_word(word))
    return " ".join(shuffled_phrase)


def main():
    input_phrase = "The chancellor said that from midnight the current system, where the" \
                   " amount owed jumps at certain price levels, would be replaced by a " \
                   "graduated rate, working in a similar way to income tax."

    print(scramble_phrase(input_phrase))


class MyScrambleTests(unittest.TestCase):
    def test_randomise_letters(self):
        self.assertEqual(randomise_letters("a"), "a")

    def test_scramble_word(self):
        self.assertEqual(scramble_word("dog"), "dog")
        self.assertEqual(scramble_word("on"), "on")
        self.assertEqual(scramble_word("on..!"), "on..!")

    def test_scramble_phrase(self):
        phrase = "The lazy dog jumped over the blue moon"
        self.assertEqual(scramble_phrase("on dog"), "on dog")
        self.assertEqual(scramble_phrase("On dog.!."), "On dog.!.")
        self.assertCountEqual(scramble_phrase(phrase), phrase)


if __name__ == '__main__':
    main()
    unittest.main()