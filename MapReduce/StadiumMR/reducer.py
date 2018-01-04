#!/usr/bin/env python3
import sys

last_roof = None
roof_count = 0

for line in sys.stdin:

	line = line.strip()
	
	data =  line.split("\t")

	if len(data) != 2:
		continue;
	roof, count = data 

	count = int(count)

	if not last_roof:
		last_roof = roof

	if roof == last_roof:
		roof_count += count

	else:
		#result = [last_roof, roof_count]
		print("{0}\t{1}".format(last_roof, roof_count))

		last_roof = roof
		roof_count = 1



print("\t".join(str(v) for v in [last_roof, roof_count]))
