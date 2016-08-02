#!/usr/bin/env python
# -*- coding: utf-8 -*- #
__author__ = "huangy"
__copyright__ = "Copyright 2016, The metagenome Project"
__version__ = "1.0.0-dev"

import argparse
import sys

def read_params(args):
    parser = argparse.ArgumentParser(description='group file change')
    parser.add_argument('-i', '--input', dest='input', metavar='input', type=str, required=True,
                        help="input file")
    parser.add_argument('-o', '--outputdir', dest='outputdir', metavar='outputdir', type=str, required=True,
                        help="out put dir")
    args = parser.parse_args()
    params = vars(args)
    return params

if __name__ == '__main__':
    param = read_params(sys.argv)
    inputFile = param['input']
    outputDir = param["outputdir"]
    with open("%s"%outputDir,"w") as fqout:
        for temp in inputFile.split(","):
            fqout.write("PE\t%s\n"%temp)
