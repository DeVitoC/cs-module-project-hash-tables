def no_dups(s):
    # Your code here
    words_array = s.split()
    words_dict = {}
    for word in words_array:
        words_dict[word] = 1
    words_array = list(words_dict.keys())
    s = " "
    s = s.join(words_array)
    return s

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))