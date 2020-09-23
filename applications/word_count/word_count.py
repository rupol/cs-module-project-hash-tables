def word_count(s):
    # split string into lowercase words, excluding special characters
    words_list = [''.join(char.lower() for char in word if char.isalpha() or char == "'")
                  for word in s.split()]
    # store {key: word, value: word's count} in this dict
    count = {}
    for word in words_list:
        # if string is just special characters
        if word == '':
            continue
        # if word isn't in dictionary, add {word: 1} to count
        if word not in count:
            count[word] = 1
        #  otherwise, add one to word's count
        else:
            count[word] += 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
