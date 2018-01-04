#!/usr/bin/env python3

import sys
import re
import csv


reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:


	if len(line) == 19:
		node_id = line[0]
		bdy = line[4]

		bdy_list = re.findall(r'[a-zA-Z]+', bdy)

		for word in bdy_list:

			print("{0}\t{1}".format(word.lower(), node_id))

