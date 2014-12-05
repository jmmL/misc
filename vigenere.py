def generate_grid():
    grid = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
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


def main():
    key = "lemon"
    plaintext = "itwasacolddarknight"

    key = key.lower()
    plaintext = plaintext.lower()
    grid = generate_grid()

    ciphertext = encipher_text(plaintext, grid, key)
    print(ciphertext)

    attempted_plaintext = decipher_text(ciphertext, grid, key)
    print(attempted_plaintext)

if __name__ == "__main__":
    main()
