#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
            description='Compares two config files and shows a difference',
            )
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
            '-f',
            '--format',
            action='store',
            help='set format of output',
            )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    return print(diff)


if __name__ == '__main__':
    main()
