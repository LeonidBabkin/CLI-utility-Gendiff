#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import argparse
from gendiff.gendiff import generate_diff


def parse_command_line():
    parser = argparse.ArgumentParser(description='Makes files discerned')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f',
                        '--format',
                        action='store',
                        help='set format of output',
                        )
    args = parser.parse_args()


def main():
    args = parse_command_line()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    return print(diff)


if __name__ == '__main__':
    main()
