import random
from urllib.request import urlopen #python2.7 使用 from urllib import url open,此为python3用法
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
	"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef _init_ (self,***)":
	"class %%% has-a _init_ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self,@@@)":
	"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	"Set *** to an instance of class %%%.",
	"***.***(@@@)":
	"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***":
	"From *** get the *** attribute and set it to '***'."
}

#do they want to drill ptrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

#load up the words from the website
for word  in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet,phrase):
	class_names = [w.capitalize() for w in 
					random.sample(WORDS,snippet.count("%%%"))]
	other_names = random.sample(WORDS,snippet.count("***"))
	results = []
	param_names = []

	for i in range(0,snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS,param_count)))

	for sentence in snippet,phrase:
		result = sentence[:]

		for word in class_names:
			result = result.replace("%%%",word,1)

		for word in other_names:
			result = result.replace("***",word,1)

		for word in param_names:
			result = result.replace("@@@",word,1)

		results.append(result)

	return results

#keeping going until they hit CTRL-D
try:
	while True:
		snippets = list(PHRASES.keys())    #python3中dict.keys()返回值不支持索引，所以要加list转化为列表。
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question,answer = convert(snippet,phrase)
			if PHRASE_FIRST:
				question,answer = answer , question

			print (question)

			input("> ")
			print("ANSWER:  %s\n\n" % answer)
except EOFError:
	print("\nBye")