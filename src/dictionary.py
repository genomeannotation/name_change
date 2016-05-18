#!/usr/bin/env python

import os
import sys

class Dictionary:

	def __init__(self):
		self.dict_list = []

	#read dictionary file 
	def read_dict(self, dictionary_filename):
		
		# Verify and read dictionary file
		if not os.path.isfile(dictionary_filename):
		    sys.stderr.write("Failed to find " + dictionary_filename + ".\n")
		    sys.exit()
		sys.stderr.write("Reading Dictionary...\n")

		fi = open(dictionary_filename, 'r')
		allLines = fi.readlines()

		for i, line in enumerate(allLines):
			words = line.strip('\n')
			splits = words.split("\t")
			self.dict_list.append(splits[0])
			self.dict_list.append(splits[1])
			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + dictionary_filename + ": " + str(((i+1)*100/len(allLines))) + "%]")
			sys.stdout.flush()

		sys.stdout.write('\n')
		fi.close()
