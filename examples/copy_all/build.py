#!/usr/bin/env python

import sys, os, glob
sys.path.insert(0, os.path.abspath('../..'))

from tinymk import *

@ptask('%.in', '%.out', glob.glob('*.in'))
def copy_files(out, dep):
    out = out[0]
    run_d(out, dep, 'cp %s %s' % (dep, out))

main()
