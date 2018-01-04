#!/usr/bin/env python3
import sys 

for line in sys.stdin:
	data = line.strip().split(" ")

	if len(data) == 10:
		page = data[6]

		if page.find("http://www.the-associates.co.uk") != -1:
			page = page[len("http://www.the-associates.co.uk"):]
			
		print("{0}\t{1}".format(page,"1"))
