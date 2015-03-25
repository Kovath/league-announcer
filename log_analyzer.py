#!/usr/bin/env python
# LOG ANALYZER
# by Kevin Yang
#
# Assumes VERY MUCH THIS FORMAT:
# [<time>] <event> -> <data>

import sys, re 
import numpy as np

def find_outliers(array, mean = None, std = None, m = 6):
	if mean == None:
		mean = np.mean(array)
	if std == None:
		std = np.std(array)

	return array[abs(array - mean) >= m * std]




if __name__ == "__main__":
	log_file = open(sys.argv[1])
	regex = re.compile(r"\[(?P<time>\d+)\] (?P<event>\w*) -> (?P<data>.*)")

	events = []
	for line in log_file:
		match = re.search(regex, line)
		if match == None:
			print("error parsing line: " + line)
			continue

		event = {
			"time" : match.group("time"),
			"event" : match.group("event"),
			"data" : eval(match.group("data")),
		}
		events.append(event)
	if len(events) <= 0:
		exit()



	data_query = dict([(key, []) for key in events[0]["data"].keys()])
	for event in events:
		for key in data_query.keys():
			data_query[key].append(event["data"][key])
	for query, data in data_query.items():
		data_query[query] = { "data" : np.array(data) }

	# calculations
	for query, stats in data_query.items():
		data = stats["data"]

		stats["median"] = np.median(data)
		stats["mean"] = np.mean(data)
		stats["min"] = np.min(data)
		stats["max"] = np.max(data)
		stats["std"] = np.std(data)
		stats["outliers"] = find_outliers(data, stats["mean"], stats["std"])

	# output
	for query, stats in data_query.items():
		print(query + ":")

		for stat, value in stats.items():
			print("\t%s: %s" % (stat, str(value)))
		print("")