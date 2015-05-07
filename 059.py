"""
Project Euler Problem 59
========================

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key. The
advantage with the XOR function is that using the same encryption key on
the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher1.txt, a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain common
English words, decrypt the message and find the sum of the ASCII values
in the original text.
"""

file = open('resources/cipher1.txt', 'r')
asciis = map(int, file.read().split(','))

length = 3
valid = [chr(i) for i in xrange(ord('a'), ord('z') + 1)]
common_words = [' and ', ' or ',  ' are ', ' is ', ' the ', ' of ', ' was ', ' were ']

def find_message(max_length, key = ''):
    if len(key) < max_length:
        for c in valid:
            find_message(max_length, key+c)
    else:
        xored_chars = []
        for i in xrange(len(asciis)):
            xored_chars.append(chr(asciis[i] ^ ord(key[i % 3])))
        xored_file = ''.join(xored_chars)
        count = sum([1 if cword in xored_file else 0 for cword in common_words])
        if count > 5: 
            print sum([ord(c) for c in xored_chars])
            return

find_message(3)