TinyMk
======

TinyMk is a small but powerful make system written in Python and based on `Cake <http://coffeescript.org/#cake>`_ and `Shake <http://http://shakebuild.com/>`. It consists of a single script that's about 300 lines long. Here's a somewhat complex example of using it:

.. code-block:: python
   
   from tinymk import * # import TinyMk
   import os, glob
   
   add_category('build') # add a new category
   
   sources = ['a.c', 'b.c', 'c.c']
   objects = [os.path.splitext(src)[0]+'.o' for src in sources]
   
   @task()
   def build():
       # invoke 2 other targets
       invoke('build:headers')
       invoke('build:app')
   
   # create a task for each element in sources inside of the category objects
   # ptask is like GNU make's pattern rules
   # for each element in the sources list, call the function
   @ptask('%.c', '%.o', sources, 'objects')
   def objects(outs, src):
       # outs is a list; since there is only one output, get it
       out = outs[0]
       # object the object file in the source has changed
       run_d(out, dep, 'gcc -c %s -o %s' % (src, out))
   
   # create a task named 'app' in the category 'build'
   @task('build:')
   def app():
       # if we need to update the output file...
       if need_to_update('app', sources):
           cinvoke('objects')
           # update the output file
           run('gcc %s -o %s' % (' '.join(objects), 'app'))
   
   # create a task named 'headers' in the category 'build'
   @task('build:')
   def headers():
       # regenerate gen.h if gen.py has changed
       run_d('gen.h', 'gen.py', 'python gen.py > gen.h')
   
   main()

Even better, TinyMk is licensed under the MIT Expat license, so you can distribute it with your application.

For more info, see the `docs` folder and the `examples` folder.

Prebuild docs are available on `ReadTheDocs <https://tinymk.readthedocs.org/en/latest>`_.

Links
*****

- `GitHub <https://github.com/kirbyfan64/tinymk>`_
- `Documentation on ReadTheDocs <tinymk.readthedocs.org>`_
- `Mailing list <tinymk@googlegroups.com>`_
- `Mailing list web interface <https://groups.google.com/forum/#!forum/tinymk>`_
