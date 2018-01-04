#!/usr/bin/env python3
import sys
from collections import defaultdict

res = defaultdict(list)

for line in sys.stdin:
	data = line.split("\t")

	if len(data) == 2:
		word, id = data
		res[word].append(id)


#for k, i in res.items():
#	print("{0}\t{1}".format(k, i))

print(sorted(res["fantastically"]))
print(len(res["fantastic"]))