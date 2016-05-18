#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import sys
from src.dictionary import Dictionary
from src.origin_file import Origin_file

class Controller:

    def __init__(self):
       self.dictionary_mnger = Dictionary()
       self.origin_mnger = Origin_file()

    def execute(self, args):

        # Read Dictionary file
        if args.dictionary:
            dictionary_filename = args.dictionary
            Dictionary.read_dict(self.dictionary_mnger, dictionary_filename)

        # Read Original file
        if args.file:
            origin_filename = args.file
            Origin_file.read_file(self.origin_mnger, origin_filename, self.dictionary_mnger)

        # Create output directory
        out_dir = "name_change_output"
        if args.out:
            out_dir = args.out
        os.system('mkdir -p ' + out_dir)

        # Write output file
        fo = open(out_dir + '/output.txt', 'w')
        for i, line in enumerate(self.origin_mnger.replaced_lines):
            fo.write(line)

            #progress output
	    sys.stdout.write('\r')
	    sys.stdout.write("[writing " + fo.name + ": " + str(((i+1)*100/len(allLines))) + "%]")
	    sys.stdout.flush()

        fo.close()
