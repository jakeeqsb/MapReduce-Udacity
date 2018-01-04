#!/usr/bin/env python3
import sys

last_cat = None
total_cost = 0

for line in sys.stdin:
	line = line.strip()

	data = line.split("\t")

	if len(data) != 2:
		continue

	cat = data[0]
	cost = float(data[1])

	if last_cat and last_cat != cat:
		print("{0}\t{1}".format(last_cat, total_cost))
		total_cost = 0

	last_cat = cat
	total_cost += cost


if last_cat != None:
	print("{0}\t{1}".format(last_cat, total_cost))