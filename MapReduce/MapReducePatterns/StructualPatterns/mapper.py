#!/usr/bin/env python3 


import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:

        # YOUR CODE HERE
        if line[0] == 'id' or line[0] == 'user_ptr_id':
        	continue
       	if len(line) == 19:
       		
       		id, title, tagnames, author_id, body, node_type, \
       		parent_id, abs_parent_id, added_at, score, \
       		state_string, last_edited_id, last_activity_by_id, last_activity_at, \
       		active_revision_id, extra, extra_ref_id, extra_count, marked = line

       		#print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}".format(id,"B",title, tagnames,
       		#	author_id, body, node_type, parent_id, abs_parent_id, added_at,score))

       		writer.writerow([id,"B",title, tagnames,
       			author_id, body, node_type, parent_id, abs_parent_id, added_at,score])
       	elif len(line) == 5:
       		user_ref_id, reputation, gold, silver, bronze = line 
       		#print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(user_ref_id,'A',\
       		#	reputation, gold, silver, bronze))
       		writer.writerow([user_ref_id,'A',
       			reputation, gold, silver, bronze])
            
     
mapper()