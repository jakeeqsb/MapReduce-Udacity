#!/usr/bin/env python3
import sys

delim = ","

for line in sys.stdin:
	line = line.strip()

	data = line.split(delim)
	if len(data) == 11:

		stadium, capacity, expanded, location, surface, turf, team, opened, weather, roof, elevation = data
		print("{0}\t{1}".format(roof,"1"))



