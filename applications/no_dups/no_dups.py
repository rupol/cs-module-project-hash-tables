def no_dups(s):
    # split string at spaces into array of words
    words_list = s.split(" ")
    # output for storing non duplicate words (order matters - list)
    no_dups_list = []

    for word in words_list:
        if word not in no_dups_list:
            # add words not already in words_list (to end)
            no_dups_list.append(word)
    # join words_list back into a string
    separator = " "
    return separator.join(no_dups_list)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
