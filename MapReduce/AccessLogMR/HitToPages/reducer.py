#!/usr/bin/env python3
import sys

last_pg = None
pg_count = 0

for line in sys.stdin:
	data = line.split("\t")

	if len(data) == 2:
		pg,count = data

		
		if last_pg and last_pg != pg:
			print("{0}\t{1}".format(last_pg, pg_count))
			pg_count = 0

		last_pg = pg 
		pg_count += int(count) 

if last_pg:
	print("{0}\t{1}".format(last_pg, pg_count))
