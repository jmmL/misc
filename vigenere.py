import unittest

def generate_grid(alphabet):
    grid = []
    for i in range(0, len(alphabet)):
        grid.append([])
    for i in range(0, len(alphabet)):
        grid[i] = alphabet[i:] + alphabet[:i]
    return grid

   
def encipher_text(plaintext, grid, key):
    ciphertext = ""
    for i in range(0, len(plaintext)):
        ciphertext += grid[ord(key[i % len(key)]) - 97][ord(plaintext[i]) - 97]
    return ciphertext


def decipher_text(ciphertext, grid, key):
    attempted_plaintext = ""
    for i in range(0, len(ciphertext)):
        attempted_plaintext += chr(grid[ord(key[i % len(key)]) - 97].index(ciphertext[i]) + 97)
    return attempted_plaintext


class MyGridTest(unittest.TestCase):
    def setUp(self):
        self.test_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.test_grid = generate_grid(self.test_alphabet)    

    def test_generate_grid(self):
        self.assertEqual(self.test_grid[7], "hijklmnopqrstuvwxyzabcdefg")
        self.assertEqual(len(self.test_grid), 26)
        self.assertEqual(len(self.test_grid[25]), 26)


class MyVigenereTests(unittest.TestCase):
    def setUp(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.test_grid = generate_grid(self.alphabet)
        self.test_plaintext = "helloworld"
        self.test_key = "test"


    def test_encipher_text(self):
        self.assertEqual(encipher_text(self.test_plaintext, self.test_grid, self.test_key), "aidehagkeh")
        self.assertNotEqual(encipher_text(self.test_plaintext, self.test_grid, self.test_key), self.test_plaintext)


    def test_decipher_text(self):
        self.assertEqual(decipher_text("ciprbhiwmyfdonofw", self.test_grid, "lemontree"), "reddoorsinbraavos")
   

def main():
    key = "lemon"
    plaintext = "itwasacolddarknight"
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    key = key.lower()
    plaintext = plaintext.lower()
    grid = generate_grid(alphabet)

    ciphertext = encipher_text(plaintext, grid, key)
    print(ciphertext)

    attempted_plaintext = decipher_text(ciphertext, grid, key)
    print(attempted_plaintext)


if __name__ == "__main__":
    unittest.main()
    main()
