#mark joseph
"""
spytools.py
=====

4 of the functions defined below are missing an implementation! Finish
the following functions:

1. gen_consecutive_chars()
2. gen_key(password)
3. sub_decrypt(password, ciphertext)
4. vig_decrypt(key, message)

"""
# 1. Implement gen_consecutive_chars()
def gen_consecutive_chars(*args):
   if(len(args) == 0):
        output = ""
        for i in range (97, 123):
            newChr = chr(i)
            output = output + newChr

        return output
   elif(len(args) == 2):
        output = ""
        for i in range (args[0], args[1]+1):
            newChr = chr(i)
            output = output + newChr

        return output
   else:
       print("Wrong number of command line arguments, either 0 args or 2")


def remove_letters(letters, s):
    """Removes every character in letters from string, s.
    :param letters: string of characters to be removed
    :type letters: str
    :param s: string that characters will be removed from
    :type s: str
    :return: a new string with all characters in letters removed from s
    :rtype: str
    """
    new_s = ''
    for ch in s:
        if ch not in letters:
            new_s += ch
    return new_s

def remove_duplicates(s):
    """Removes all duplicate characters in string, s
    :param s: string to remove duplicates from
    :type s: str
    :return: new string without duplicates
    :rtype: str
    """
    new_s = ''
    for ch in s:
        if ch not in new_s:
            new_s += ch
    return new_s


# 2. Implement gen_key(password)
def gen_key(password):

    newpwd = remove_duplicates(password)

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    index = newpwd[-1:]
    startThing = alphabet.find(index)

    fullstring = newpwd

    while(len(fullstring)!= 26):
        startThing = startThing + 1
        if(startThing == 26):
            startThing = 0
        fullstring = fullstring + alphabet[startThing]

    return fullstring


def sub_encrypt(password, message):
    """Encrypt a message using the substitution cipher. If a
    character is not in the key, the character remains unchanged.
    :param password: the password used to generate a key
    :type password: str
    :param message: the message to be encrypted
    :type message: str
    :return: the resulting ciphertext as a string
    :rtype: str
    """
    key = gen_key(password)
    alpha = gen_consecutive_chars()
    ciphertext = ''
    for ch in message:
        try:
            ciphertext = ciphertext+  key[alpha.index(ch)]
        except ValueError:
            ciphertext = ciphertext + ch
    return ciphertext

# 3. Implement sub_decrypt(password)
def sub_decrypt(password, ciphertext):
    key = gen_key(password)
    alpha = gen_consecutive_chars()
    message = ''
    for ch in ciphertext:
        try:
            message = message + alpha[key.index(ch)]
        except ValueError:
            message = message + ch

    return message

def vig_encrypt(key, message):

    cypher_text = ''
    alphabet = gen_consecutive_chars()
    key_len, alphabet_len = len(key), len(alphabet)


    # or replace next two lines with...
    # for i, ch in enumerate(message):
    for i in range(len(message)):
        ch = message[i]

        # based on key... what row (labeled by letters) in table will we
        # use? the example in the book shows a mapping of the key to a
        # message:
        # DAVINCIDAVINCIDAVINC
        # the eagle has landed
        # consequently, the row in we use for the first letter, t is D
        # (row_letter is D for first letter, t)
        row_letter = key[i % key_len].lower()

        # calculate offset to simulate shifting letters for each row:
        # again, using the first letter t, and D as the row letter...
        # D is at position 3 of the alphabet, which means that the key
        # (the alphabet) is shifted by 3: defghijklmnopqrstuvwxyzabcd
        # ... let's save this shift in a variable called offset
        offset = alphabet.index(row_letter.lower())

        try:
            # so now, we can translate our original character, ch, by
            # finding out where it is in the offset row represented by D.
            # simply add the offset to what ch's position would be in the
            # alphabet (so if ch is t and the key specifies that the
            # offset is 3, then the index of the character that t is
            # translated to 19 + 3)...
            other_index = (alphabet.index(ch) + offset) % alphabet_len

            # if working with the letter and key mentioned above, t is
            # translated to the letter at index 22 of the alphabet: w
            cypher_text += alphabet[other_index]

        except ValueError:
            cypher_text += ch

    return cypher_text

# 4. Implement vig_decrypt(key, message)
def vig_decrypt(key, message):
    """Decrypt a message that was encrypted using the vigenère cipher.
    Punctuation is preserved. The ciphertext should be normalized to
    all lowercase letters.

    s = 'whz rcooe pnu oailrf'
    vig_decrypt(s) # --> 'the eagle has landed'

    :param key: the key originally used to encrypt the message
    :type key: str
    :param message: the message to be decrypted (the ciphertext)
    :type message: str
    :return: the plain text produced by decrypting the ciphertext
    :rtype: str
    """

    cypher_text = ''
    alphabet = gen_consecutive_chars()
    key_len, alphabet_len = len(key), len(alphabet)


    # or replace next two lines with...
    # for i, ch in enumerate(message):
    for i in range(len(message)):
        ch = alphabet[i]

        # based on key... what row (labeled by letters) in table will we
        # use? the example in the book shows a mapping of the key to a
        # message:
        # DAVINCIDAVINCIDAVINC
        # the eagle has landed
        # consequently, the row in we use for the first letter, t is D
        # (row_letter is D for first letter, t)
        row_letter = key[i % key_len].lower()

        # calculate offset to simulate shifting letters for each row:
        # again, using the first letter t, and D as the row letter...
        # D is at position 3 of the alphabet, which means that the key
        # (the alphabet) is shifted by 3: defghijklmnopqrstuvwxyzabcd
        # ... let's save this shift in a variable called offset
        offset = alphabet.index(row_letter.lower())

        try:
            # so now, we can translate our original character, ch, by
            # finding out where it is in the offset row represented by D.
            # simply add the offset to what ch's position would be in the
            # alphabet (so if ch is t and the key specifies that the
            # offset is 3, then the index of the character that t is
            # translated to 19 + 3)...
            other_index = (message.index(ch) + offset) % key_len

            # if working with the letter and key mentioned above, t is
            # translated to the letter at index 22 of the alphabet: w
            cypher_text += message[other_index]

        except ValueError:
            cypher_text += ch

    return cypher_text

if __name__ == '__main__':

    print(vig_encrypt("h", "hello world"))
    print(vig_decrypt("h", "olssv dvysk"))
