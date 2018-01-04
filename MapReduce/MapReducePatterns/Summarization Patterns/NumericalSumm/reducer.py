#!/usr/bin/env python3
import sys
from collections import defaultdict

res = defaultdict(list)
each_total = 0

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) !=2:
		continue 

	wk_day, sales = data

	res[wk_day].append(float(sales))



for ky, itm in res.items():
	each_total = sum(itm)
	print('{0}\t{1}'.format(ky, each_total / len(itm)))
