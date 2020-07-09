import random
import sys

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
cache = {}
words = words.split()
for word in range(len(words) - 1):
    if words[word] in cache.keys():
        cache[words[word]].append(words[word + 1])
    else:
        cache[words[word]] = [words[word + 1]]

# TODO: construct 5 random sentences
# Your code here
keys = list(cache.keys())
start_words = []
stop_words = []
for key in keys:
    if key[0].isupper() or (key[0] in ['"', '('] and key[1].isupper()):
        start_words.append(key)
    if key[-1] in ['.', '?', '!', '."', '.)']:
        stop_words.append(key)
    elif key[-1] in ['"', ')'] and key[-2] in ['.', '?', '!']:
        stop_words.append(key)

word = random.choice(start_words)
print(word, end = " ")
if word in stop_words:
    print()
    sys.exit()
while True:
    array = cache[word]
    s = random.choice(array)
    print(s, end = " ")
    word = s
    if s in stop_words:
        print()
        break
