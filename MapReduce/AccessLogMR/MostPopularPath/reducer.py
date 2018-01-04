#!/usr/bin/env python3
import sys

mst_pop_pg = None
mst_hits = 0
curr_pg = None
curr_occ = 0 


for line in sys.stdin:

	data = line.strip().split("\t")

	if len(data) == 2:
		pg, count = data 

		count = int(count)

		if not curr_pg:
			curr_pg = pg
			mst_pop_pg = curr_pg
			curr_occ = count 
			mst_hits = count 

		elif curr_pg == pg:
			curr_occ += count 

		else:
			curr_pg = pg
			curr_occ = count

		if mst_hits < curr_occ:
			mst_pop_pg = curr_pg
			mst_hits = curr_occ



print("{0}\t{1}".format(mst_pop_pg, mst_hits))


