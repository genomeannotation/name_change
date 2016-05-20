#!/usr/bin/env python

import os
import sys
import re

class Origin_file:

	def __init__(self):
		self.replaced_lines = ""

	#read Origin file 
	def read_file(self, origin_filename, dictionary_mnger):

		# Verify and read origin file
		if not os.path.isfile(origin_filename):
		    sys.stderr.write("Failed to find " + origin_filename + ".\n")
		    sys.exit()
		sys.stderr.write("Reading Origin...\n")

		fi = open(origin_filename, 'r')
		allLines = fi.readlines()

		lines = ''.join(allLines)

		for i, name in enumerate(dictionary_mnger.dict_list_old):
			oldname = r"\b" + re.escape(name) + r"\b"
			newname = dictionary_mnger.dict_list_new[i]
			lines = re.sub(oldname, newname, lines)

			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + origin_filename + ": " + str(((i+1)*100/len(dictionary_mnger.dict_list_old))) + "%]")
			sys.stdout.flush()
		self.replaced_lines = lines

		sys.stdout.write('\n')
		fi.close()
