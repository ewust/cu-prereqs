#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    res = re.search("^([0-9/]{4,6})\s.+\s([A-Z]{4} [0-9]{4})", line)
    if res is not None:
        class_num = res.group(0)
        print class_num
        prereq = res.group(1)
        #print '%s -> ECEN %s' % (prereq, class_num)
