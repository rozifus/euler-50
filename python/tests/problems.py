#!/usr/bin/env python

import os, sys
import imp
import doctest
import re

def testall():
    # setup path and regex for problems
    prob_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
    prob_file_format = re.compile('^\d\d\d\d\.py$')
    problems = []

    # get list of problems
    for (path, folders, files) in os.walk(prob_dir):
        if path == prob_dir:
            for f in files:
                if prob_file_format.match(f):
                    problems.append(f)

    # test each problem
    for p in problems:
        problem_module = imp.load_source(p, os.path.join(prob_dir, p))
        doctest.testmod(problem_module)

if __name__ == "__main__":
    testall()
