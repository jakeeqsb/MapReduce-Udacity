#!/usr/bin/env python3
import sys

last_ip = None
ip_count = 0

for line in sys.stdin:
	data = line.split("\t")

	if len(data) == 2:
		ip, count = data

		if last_ip and last_ip != ip:
			print("{0}\t{1}".format(last_ip, ip_count))

			ip_count = 0

		last_ip = ip
		ip_count += int(count)


if last_ip != None:
	print("{0}\t{1}".format(last_ip, ip_count))