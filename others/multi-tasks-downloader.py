#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Multi-tasking automatic downloader
Before downloading, make sure the urls are all accessable!
Because the script is only repsonsible for dispatching the tasks.
'''

__author__ = 'Engine'

import os
import argparse
import subprocess


# set argument parser
arg_parser = argparse.ArgumentParser(description="kissg's axel downloader.")
app_group = arg_parser.add_mutually_exclusive_group()
app_group.add_argument("-w", "--wget", action="store_true",
                       help="Use wget to download.")
app_group.add_argument("-a", "--axel", action="store_true",
                       help="Use axel to download.")
arg_parser.add_argument("-n", "--num", type=int, default=8,
                        choices=list(range(1, 17, 1)),
                        help="Specify an alternative number of connections.")
arg_parser.add_argument("-q", "--quiet", action="store_true",
                        help="No output to stdout.")
arg_parser.add_argument("urls", nargs=argparse.REMAINDER, help="The urls.")

args = arg_parser.parse_args()


def download(cmd):
    if not args.wget:
        cmd.append("-n %s" % args.num)  # specify number of connections
    if args.quiet:  # quiet?
        cmd.append("-q")
    urls = args.urls
    for item in urls:  # the remain arguments are all regarded as urls, so
        if os.path.isfile(item):  # it shoul be the last option
            urls.remove(item)  # if the argument refers to a file, extract it
            with open(item, 'r') as f:
                for url in f.readlines():
                    urls.append(url)
    for i in urls:
        cmd.append(i.strip())  # create axel subprocess to download
        subprocess.Popen(cmd)
        cmd.pop()


def main():
    if args.wget:  # if -w option is specified, download with wget
        download(["wget"])
    else:          # if no downloader is specified, use axel
        download(["axel"])


if __name__ == "__main__":
    main()
