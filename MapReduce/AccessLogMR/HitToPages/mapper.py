#!/usr/bin/env python3
import sys

for line in sys.stdin:

	data = line.strip().split()
	
	if len(data) == 10:
		page = data[6]
	
		print("{0}\t{1}".format(page, "1"))



