#!/usr/bin/env python3
import sys

last_store = None
hst_cost = 0

for line in sys.stdin:
	data = line.split("\t")

	if len(data) != 2:
		continue

	store, cost = data

	cost = float(cost)

	if last_store and last_store != store:
		print("{0}\t{1}".format(last_store,hst_cost))
		hst_cost = 0

	last_store = store
	if cost >= hst_cost:
		hst_cost = cost

if last_store:
	print("{0}\t{1}".format(last_store,hst_cost))
