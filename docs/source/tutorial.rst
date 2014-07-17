Tutorial
========

TinyMk may be small, but it isn't any short of powerful.

The basics
**********

Here's a basic example:

.. code-block:: python
   
   from tinymk import *
   
   @task()
   def test():
       print('Hello, TinyMk!')

This simple code defines a task named `test`. Save this into a file named `build.py` and run it::
   
   $ python build.py
   invalid number of args
   usage: build.py [-h|--help] [--task-help] <task> [<args>]
   $

To list the tasks, use `?` as the task name::
   
   $ python build.py ?
   Tasks:
   
   test
   $

Let's run our task::
   
   $ python build.py test
   Hello, TinkMk!
   $

Running commands
****************

Often, in a build script, you don't want to just print stuff. You want to be able to run programs. Look at this example:

.. code-block:: python
   
   from tinkmk import *
   
   @task()
   def test():
       run('cp x.in x.out')

Now create a file named `x.in`::
   
   $ echo 'Hi!' > x.in
   $

Next, run the build script and check our new file `x.out`::
      
   $ python build.py test
   cp x.in x.out
   $ cat x.out
   Hi!
   $ 

Dependencies
************

Let's say we have a big project, consisting of millions of files. It's likely that you don't want to rebuild everything when you modify one file. Build systems like make let you mention a command's dependencies:

.. code-block:: make
   
   x.out : x.in
       cp x.in x.out

TinyMk can do this, too, albeit slightly differently. You manually check if you need to update the files using `need_to_update`:

.. code-block:: python
   
   from tinymk import *
   
   @task()
   def test():
       if need_to_update('x.out', 'x.in'):
           run('cp x.in x.out')

Typing all of that is a pain, though. That's what the `run_d` function is for:

.. code-block:: python
   
   from tinymk import *
   
   @task()
   def test():
       run_d('x.out', 'x.in', 'cp x.in x.out')

That's easier, isn't it?

Categories
**********

In a large project, you might want to apply some method of organization. TinyMk lets you group tasks into `categories`. Here's an example:

.. code-block:: python
   
   from tinymk import *
   
   add_categories('a')
   
   @task('a:')
   def b():
       print('Running task a:b...')

Now you can use it like this::
   
   $ python build.py a:b
   Running task a:b...
   $ 

Conclusion
**********

That concludes this breif tutorial on TinyMk. There's much more that hasn't been discussed, however; you'll want to read the :doc:`API reference </apiref>`. In addition, you should read the :doc:`command line interface reference </cmdref>`.
