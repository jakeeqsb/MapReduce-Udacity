#!/usr/bin/env python3
import sys
import re

last_word = None
word_count = 0

for line in sys.stdin:

	data = line.split('\t')
	if len(data)!= 2:
		continue
	word, count = data
	word = word.lower()
	word = re.sub(r'[^\w\s]','',word)
	
	if last_word and last_word != word:
		print("{0}\t{1}".format(last_word, word_count))
		word_count = 0

	last_word = word
	word_count += int(count) 


if last_word:
	print("{0}\t{1}".format(last_word, word_count))


