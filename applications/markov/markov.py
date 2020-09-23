import random

# Read in all the words in one go
with open("applications\\markov\\input.txt") as f:
    words = f.read().split(" ")

# analyze which words can follow other words
# create word_analysis dict to store:
# key: each unique word
# value: an array of words that are seen following that word (include duplicates)
word_analysis = {}
for (index, word) in enumerate(words):
    next_word = words[(index + 1) % len(words)]
    if word not in word_analysis:
        word_analysis[word] = [next_word]
    else:
        word_analysis[word].append(next_word)

# eg_dict = {
#     "I": ["another", "word", "and", "another"],
#     "word": ["another", "word", "and", "another"],
#     "Startword": ["another", "word", "and", "another"],
#     "endword!": ["another", "word", "and", "another"],
#     "endword?\"": ["another", "word", "and", "another"],
# }


# get start words
# words that begin with a capital, or a `"` followed by a capital
start_words = {
    word: next_words for word, next_words in word_analysis.items() if word[0].isupper() or word[0] == '"'}

# get stop words
# words that end in any of the punctuation `.?!`, or that punctuation followed by a `"`.
punctuation = ('.', '?', '!')
stop_words = {}
for word, next_words in word_analysis.items():
    if word[-1] in punctuation:
        stop_words[word] = next_words
    if len(word) > 1:
        if word[-2] in punctuation and word[-1] == '"':
            stop_words[word] = next_words

# construct 5 random sentences


def random_sentence():
    sentence = []
    is_complete = False
    # loop through
    current_word, next_words = random.choice(list(start_words.items()))
    sentence.append(current_word)
    while is_complete is not True:
        # select a new word from our word analysis list of next words
        current_word = random.choice(next_words)
        # print the word
        sentence.append(current_word)
        # If it's a "stop word", stop.
        if current_word in stop_words:
            is_complete = True
        # Else randomly choose a word that can follow this one.
        else:
            next_words = word_analysis[current_word]
    separator = " "
    return separator.join(sentence)


print(random_sentence())
print("")
print(random_sentence())
print("")
print(random_sentence())
print("")
print(random_sentence())
print("")
print(random_sentence())
