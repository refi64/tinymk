#!/usr/bin/env python

import sys, os
sys.path.insert(0, os.path.abspath('../..'))

from tinymk import *

def coffee(x):
    # run the CoffeeScript compiler
    run('coffee -c %s' % x)

@task()
def build():
    invoke('build:a')
    invoke('build:b')

@task('build:')
def a():
    # if a.coffee has changed and we need to update a.js...
    if need_to_update('a.js', 'a.coffee'):
        # call the coffee function
        coffee('a.coffee')

@task('build:')
def b():
    # see above function
    if need_to_update('b.js', 'b.coffee'):
        coffee('b.coffee')

main()
