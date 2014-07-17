#!/usr/bin/env python
import sys, os
sys.path.insert(0, '../..')

from tinymk import *

@task()
def build():
    # update x.out if x.in has changed
    run_d('x.out', 'x.in', 'cp x.in x.out')

main()
