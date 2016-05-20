#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
import argparse
from src.controller import Controller

def main():
    parser = argparse.ArgumentParser(
    epilog="""
    Name changing tool for replacing scaffold names.
    Latest version At:
    https://github.com/genomeannotation/name_change
    """,
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-d', '--dictionary', required=True, help='two column file with [new names]\\t[old names]')
    parser.add_argument('-f', '--file', required=True, help='file with names to be changed')
    parser.add_argument('-o', '--out', help='output folder name')
    args = parser.parse_args()
    controller = Controller()
    controller.execute(args)

if __name__ == '__main__':
    main()
