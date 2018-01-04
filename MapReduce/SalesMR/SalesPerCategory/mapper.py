#!/usr/bin/env python3
import sys

for line in sys.stdin:
	line = line.strip()

	data = line.split("\t")

	if len(data) == 6:
		cat = data[3]
		cost = data[4]

		print("{0}\t{1}".format(cat, cost))