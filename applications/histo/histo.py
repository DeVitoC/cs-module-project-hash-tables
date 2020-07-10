# Your code here
def histogram(filename):
	with open(filename) as f:
		words = f.read()

	cache = {}
	reference = {}
	high_value = 0
	longest_word = 0
	words = words.translate(str.maketrans('', '', '":;,.-+=/\|[]{}()*^&!?'))
	words = words.split()
	for word in words:
		word = word.lower()
		if len(word) > longest_word:
			longest_word = len(word)
		if word in cache.keys():
			cache[word] += 1
		else:
			cache[word] = 1

	sorted(cache.items(), key = lambda x: x[1], reverse = True)

	for word in cache:
		if cache[word] in reference.keys():
			reference[cache[word]].append(word)
		else:
			reference[cache[word]] = [word]
		if cache[word] > high_value: high_value = cache[word]

	# for word in cache:
	# 	print(f"{word}: {cache[word]}")

	for num in range(0, high_value):
		if (high_value - num) not in reference.keys():
			continue
		hashmarks = '#' * (high_value - num)
		sorted_words = reference[high_value - num]
		sorted_words.sort()
		# print(f"{high_value - num}: {sorted_words}")
		for word in sorted_words:
			justify = longest_word - len(word) + 2
			print(f"{word}:{' ' * justify}{hashmarks}")


histogram("robin.txt")