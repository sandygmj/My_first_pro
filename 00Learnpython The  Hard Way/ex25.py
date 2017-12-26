def break_words(stuff):   #将stuff按空格分成单独的单词，返回为一个列表。
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):   #按字母顺序进行重新排列。
	#sort the words.
	return sorted(words)

def print_first_word(words):
	#Print the first word after poping it.
    word = words.pop(0)
    print(word)

def print_last_word(words):
	#Printing the last word after poping it
	word = words.pop(-1)
	print(word)

def sort_sentence(sentence):
	#Take in a full sentence and returns the sorted words
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	#Print the first and last words of the sentence
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	#Sorted the sentence and print the first and the last one. 
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	