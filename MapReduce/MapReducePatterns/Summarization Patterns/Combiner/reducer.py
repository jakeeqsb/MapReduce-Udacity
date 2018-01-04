#!/usr/bin/env python3

import sys

last_wk = None
etot_sales = 0
count = 0


for line in sys.stdin:

	data = line.strip().split("\t")

	if len(data) != 2:
		continue 

	wk, sales = data 

	if last_wk and last_wk != wk:
		print("{0}\t{1}".format(last_wk, etot_sales/count))
		etot_sales = 0
		count = 0 

	last_wk = wk
	etot_sales += float(sales)
	count += 1


if last_wk:
	print("{0}\t{1}".format(last_wk, etot_sales/count))
