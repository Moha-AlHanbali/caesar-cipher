import nltk
from nltk.corpus import words, names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


def encrypt(text, k):
    """
    Encrypts a text with numeric shift based on inputs.

    Arguments:
    text: String
    k: Int

    Return: Encrypted String
    
    """
    encrypt_text = ""
    multi_word = False
    words = text.split(" ")

    for word in words:

        if multi_word == True:
            encrypt_text += " "

        multi_word = True

        for char in word:


            char_order = ord(char)

            if char_order >= 65 and char_order <= 90:
                shift = 65
            elif char_order >= 97 and char_order <= 122:
                shift = 97
            else:
                encrypt_text += char
                continue


            shifted_order = char_order + k - shift

            reshifted_order = shifted_order % 26 + shift

            encrypt_text += chr(reshifted_order)

    return encrypt_text





encrypt, 

def decrypt(encrypted_text, k):
    """
    Decrypts a text with numeric shift based on inputs.

    Arguments:
    encrypted_text: Encrypted String
    k: Int key for decryption

    Return: Decrypted String
    
    """
    return encrypt(encrypted_text, -k)



def crack(encrypted_text):
    """
    Decodes a ciphered text without access to the key.

    Arguments:
    encrypted_text: Encrypted String

    Return: Decrypted String
    """
    words_list = words.words()
    names_list = names.words()

    candidates = []
    for i in range(26):
        candidates.append(decrypt(encrypted_text, i))

    for candidate in candidates:
        phrase = candidate.split(" ")
        word_count = 0

        for word in phrase:
            if word.lower() in words_list or word.lower() in names_list:
                word_count += 1
            
        total_words = len(candidate.split(" "))
        ratio = (word_count / total_words) *100

        if ratio > 50:
            print((" ").join(phrase), ratio)
            return (" ").join(phrase)

    return ""
