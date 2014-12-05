
grid = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, len(alphabet)):
    grid.append([])
for i in range(0, len(alphabet)):
    grid[i] = alphabet[i:] + alphabet[:i]

    
key = "lemon"
plaintext = "itwasacolddarknight"
ciphertext = ""

key = key.lower()
plaintext = plaintext.lower()

for i in range(0, len(plaintext)):
    ciphertext += grid[ord(key[i % len(key)]) - 97][ord(plaintext[i]) - 97]
    
print(ciphertext)

attempted_plaintext = ""

for i in range(0, len(ciphertext)):
    attempted_plaintext += chr(grid[ord(key[i % len(key)]) - 97].index(ciphertext[i]) + 97)
    
print(attempted_plaintext)
