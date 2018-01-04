#!/usr/bin/env python3
import sys

for line in sys.stdin:
	line = line.strip().split(' ')

	for word in line:
		print("{0}\t{1}".format(word.strip(), "1"))
		
