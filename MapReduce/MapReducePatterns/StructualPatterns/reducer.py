#!/usr/bin/env python3


import sys
import csv
from collections import defaultdict
def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    nodes = defaultdict(list)
    users = defaultdict()


    for line in reader:

        # YOUR CODE HERE

        if len(line) < 2:
            continue

        print(line)
        key = line[0]
        marker = line[1]	

        if marker == 'A':
        	users[key] = line[2:]
        elif marker == 'B':
        	nodes[key].append(line[2:])

    for ky in users:
        id,title,tag,auth_id,node_type, parent_id, abs_parent_id, added_at, score = nodes[ky]
        for elem in users[ky]:
            rep, gold, silver, bronze = elem
            writer.writerow([id,title,tag,auth_id,node_type, parent_id, abs_parent_id, added_at, score,
                rep, gold, silver, bronze])

reducer()