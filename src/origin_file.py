#!/usr/bin/env python

import os
import sys

class Origin_file:

	def __init__(self):
		self.replaced_lines = []
		self.delim = ','

	#read Origin file 
	def read_file(self, origin_filename, dictionary_mnger):

		# Verify and read origin file
		if not os.path.isfile(origin_filename):
		    sys.stderr.write("Failed to find " + origin_filename + ".\n")
		    sys.exit()
		sys.stderr.write("Reading Origin...\n")

		fi = open(origin_filename, 'r')
		allLines = fi.readlines()
	
		for i, line in enumerate(allLines):
			words = line.strip('\n')
			splits = words.split(self.delim)
			g = [0, 0, 0]
			for j, item in enumerate(splits[:]):

				try:
					location = dictionary_mnger.dict_list.index(item)
				except ValueError:
					location = -1	

				#change the line
				if (location >= 0):
					g[0]=1 #line needs replaced word
					g[1]=j #position of word to be replaced
					g[2]=location-1 #location - 1 to access new version of word from dictionary

			newline = ""
			if g[0]==1:
				for k, word in enumerate(splits[:]):
					if k == g[1]:
						newline += dictionary_mnger.dict_list[g[2]] + self.delim
					else:
						newline += word + self.delim
				self.replaced_lines.append(newline[:-1])
			else:
				self.replaced_lines.append(line)

			#progress output
			sys.stdout.write('\r')
			sys.stdout.write("[reading " + origin_filename + ": " + str(((i+1)*100/len(allLines))) + "%]")
			sys.stdout.flush()

		sys.stdout.write('\n')
		fi.close()
