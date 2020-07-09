import string

def word_count(s):
    # Your code here
    s = s.translate(str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&'))
    word_array = s.split()
    num_words = {}
    for word in word_array:
        if word == "":
            continue
        word = word.lower()
        if word not in num_words.keys():
            num_words[word] = 0
        num_words[word] += 1
    return num_words

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))