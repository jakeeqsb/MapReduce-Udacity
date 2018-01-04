#!/usr/bin/env python3
import sys

import sys

for line in sys.stdin:
	line = line.strip()

	data = line.split("\t")

	if len(data) == 6:
		store = data[2]
		cost = data[4]

		print("{0}\t{1}".format(store, cost))