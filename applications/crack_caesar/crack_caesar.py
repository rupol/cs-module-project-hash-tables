# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
def build_decode_table(cipher_text):
    # build letter frequency hash table
    # key: letter
    # value: frequency
    char_frequency = {}
    for char in cipher_text:
        if char.isalpha():
            if char not in char_frequency:
                char_frequency[char] = 1
            else:
                char_frequency[char] += 1
    # sort frequency table most frequent char -> least frequent char
    char_frequency = sorted(char_frequency.items(),
                            key=lambda x: x[1], reverse=True)
    # discard the frequencies - list of chars sorted most -> least
    c = [i[0] for i in char_frequency]
    # match cipher frequency with expected english char frequency
    decode_table = {
        c[0]: 'E', c[1]: 'T', c[2]: 'A', c[3]: 'O', c[4]: 'H', c[5]: 'N', c[6]: 'R', c[7]: 'I', c[8]: 'S', c[9]: 'D', c[10]: 'L', c[11]: 'W', c[12]: 'U', c[13]: 'G', c[14]: 'F', c[15]: 'B', c[16]: 'M', c[17]: 'Y', c[18]: 'C', c[19]: 'P', c[20]: 'K', c[21]: 'V', c[22]: 'Q', c[23]: 'J', c[24]: 'X', c[25]: 'Z'
    }
    return decode_table


def decode(decode_table, cipher_text):
    plain_text = ""

    for char in cipher_text:
        if char.isalpha():
            plain_text += decode_table[char]
        else:
            plain_text += char

    return plain_text


# test with ciphertext
with open("applications\\crack_caesar\\ciphertext.txt") as f:
    plain_text = f.read()

decode_table = build_decode_table(plain_text)

# print(decode_table)
print(decode(decode_table, plain_text))
