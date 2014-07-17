TinyMk
======

TinyMk is a small but powerful make system written in Python and based on `Cake <http://coffeescript.org/#cake>`_. It consists of a single script that's about 200 lines long. Here's a somewhat complex example of using it:

.. code-block:: python
   
   from tinymk import * # import TinyMk
   import os
   
   add_category('build') # add a new category
   
   @task()
   def build():
       # invoke 2 other targets
       invoke('build:headers')
       invoke('build:app')
   
   @task('build:')
   def app():
       sources = ['a.c', 'b.c', 'c.c']
       objects = [os.path.splitext(src)[0]+'.o' for src in sources]
       # if we need to update the output file...
       if need_to_update('app', sources):
           # loop over the sources
           for obj, src in zip(objects, sources):
               # update the object file if the source has changed
               run_d(obj, src, 'gcc -c %s -o %s' % (src, obj))
           # update the output file
           run('gcc %s -o %s' % (' '.join(objects), 'app'))
   
   @task('build:')
   def headers():
       # regenerate gen.h if gen.py has changed
       run_d('gen.h', 'gen.py', 'python gen.py > gen.h')

Even better, TinyMk is licensed under the MIT Expat license, so you can distribute it with your application.

For more info, see the `docs` folder and the `examples` folder.
