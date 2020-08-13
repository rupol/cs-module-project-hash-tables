def word_histo(filename):
    # open file
    with open(filename) as f:
        # create array of lowercase words, filtering out special characters
        words = [''.join(char.lower() for char in word if char.isalpha() or char == "'")
                 for word in f.read().split()]
    word_histo = {}
    longest_word = 0
    # loop through words to get a count of each word, and find the longest word
    # save word count in word_histo
    for word in words:
        if word not in word_histo:
            word_histo[word] = 1
            if len(word) > longest_word:
                longest_word = len(word)
        else:
            word_histo[word] += 1

    # sort our word_histo dict by descending word count, then alphabetically
    sorted_histo = sorted(word_histo.items(), key=lambda x: (-x[1], x[0]))

    # print each word, left justifying two spaces after the longest word
    for word in sorted_histo:
        hashes = word[1]*"#"
        print(f'{word[0]:{longest_word + 2}}{hashes}')


word_histo("applications\\histo\\robin.txt")
