#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
import argparse
from src.controller import Controller

def main():
    parser = argparse.ArgumentParser(
    epilog="""
    Name changing tool for replacing scaffold names.
    """,
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-d', '--dictionary', required=True, help='path to two column file with [old names] \\t [new names]')
    parser.add_argument('-f', '--file', required=True, help='path to file with names to be changed')
    parser.add_argument('-o', '--out', help='output folder name')
    args = parser.parse_args()
    controller = Controller()
    controller.execute(args)

if __name__ == '__main__':
    main()
