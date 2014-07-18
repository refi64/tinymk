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
   
   main()

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
   Running task test...
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
   
   main()

Now create a file named `x.in`::
   
   $ echo 'Hi!' > x.in
   $

Next, run the build script and check our new file `x.out`::
      
   $ python build.py test
   Running task test...
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
   
   main()

Typing all of that is a pain, though. That's what the `run_d` function is for:

.. code-block:: python
   
   from tinymk import *
   
   @task()
   def test():
       run_d('x.out', 'x.in', 'cp x.in x.out')
   
   main()

That's easier, isn't it?

Categories
**********

In a large project, you might want to apply some method of organization. TinyMk lets you group tasks into `categories`. Here's an example:

.. code-block:: python
   
   from tinymk import *
   
   add_categories('a')
   
   @task('a:')
   def b():
       print('Inside task a:b')
   
   main()

Now you can use it like this::
   
   $ python build.py a:b
   Running task a:b...
   Inside task a:b
   $ 

Parallel execution
******************

Sometimes you can run different tasks at the same time. For instance:

.. code-block:: python
   
   from tinymk import *
   
   @task()
   def build_object1():
       run_d('a.o', 'a.c', 'gcc -c a.c -o a.o')
   
   @task()
   def build_object2():
       run_d('b.o', 'b.c', 'gcc -c b.c -o b.o')
   
   @task()
   def build():
       if need_to_update('app', ['a.o', 'b.o']):
           qinvoke('build_object1')
           qinvoke('build_object2')
           run('gcc a.o b.o -o app')
   
   main()

Notice the use of `qinvoke`. It's like invoke, but it doesn't print the name of the currently running task.

Now, `a.o` and `b.o` don't directly depend on each other. We can technically build those two at the same time. Look at this slightly modified code:

.. code-block:: python
   
   from tinymk import *
   
   @task()
   def build_object1():
       run_d('a.o', 'a.c', 'gcc -c a.c -o a.o')
   
   @task()
   def build_object2():
       run_d('b.o', 'b.c', 'gcc -c b.c -o b.o')
   
   @task()
   def build():
       if need_to_update('app', ['a.o', 'b.o']):
           p1 = pqinvoke('build_object1')
           p2 = pqinvoke('build_object2')
           p1.join()
           p2.join()
           run('gcc a.o b.o -o app')
   
   main()

This time, we're using `pqinvoke`. `pqinvoke` is just like `qinvoke`, except that it return an object of type `multiprocessing.Process`(see the Python `multiprocessing module <https://docs.python.org/library/multiprocessing.html>`_). The next line does the same thing. The neat thing is that `pqinvoke` doesn't wait for the task to finish. It simply starts the task in a seperate process. That way, you can run multiple tasks at once.

However, there is a major issue: how do we know when `p1` and `p2` are done so we can finish building? Well, the `join` method simply pauses the current task until it's own task finishes running.

Also note that, just like `qinvoke` has it's counterpart `pqinvoke`, `invoke` has its own multiprocessing counterpart: `pinvoke`.

One more thing: you need to be careful when printing text to the screen when multiple tasks are running at once, or else their output will get all jumbled together. To fix the issue, simply enclose the code with a `with lock:` block:

.. code-block:: python
   
   with lock:
       print('Hello!')
   # continue doing other stuff...

Conclusion
**********

That concludes this breif tutorial on TinyMk. There's much more that hasn't been discussed, however; you'll want to read the :doc:`API reference </apiref>`. In addition, you should read the :doc:`command line interface reference </cmdref>`.
