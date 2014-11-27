API reference
=============

.. py:module:: tinymk

.. py:data:: lock
   
   An instance of `multiprocessing.Lock`. Use this when dealing with `stdout` and `stderr`.

.. py:function:: add_category(name)
   
   Add a new category. You can create multiple categories at once by separating the name with colons(`:`):
   
   .. code-block:: python
      
      add_category('a') # add a category named a
      add_category('a:b:c') # add a category named c inside a new category in b inside a

.. py:function:: task(tname=None)
   
   A decorator to create a new task with the name `tname`.
   
   :param tname: If `None`, the task will carry the name of the function. In addition, if `tname` ends with a colon, `tname` will be used as the category, and the function's name will be the task name. For example:
   
   .. code-block:: python
      
      @task('a:b:') # task name will be a:b:c
      def c(): pass
      
      @task('a:b:d') # task name will be a:b:d
      def abc(): pass
      
      @task() # task name will be abc
      def xyz(): pass

.. py:function:: ptask(pattern, outs, deps, category=None)
   
   A decorator to create a set of pattern tasks. Pattern tasks are the TinyMk equivalent of GNU Make's `pattern rules`. Here's an example:
   
   .. code-block:: python
      
      @ptask('%.in', '%.out', glob.glob('*.in'))
      def copy_files(outs, dep):
          run_d(outs, dep, 'cp %s %s' % (dep, outs[0]))
   
   That's roughly equivalent to this GNU make rule:
   
   .. code-block:: make
      
      %.out : %.in
          cp $< $@
   
   :param pattern: The pattern that `deps` will be matched against.
   :param outs: The output file patterns.
   :param deps: The input files.

.. py:function:: need_to_update(outs, deps)
   
   Returns `True` if the oldest file in `outs` is newer than the newest file in `deps`. If either `outs` or `deps` is a string, it will be converted to a list using `shlex.split`.

.. py:function:: digest_update(outs, deps)
   
   Returns `True` if any of the files in `deps` have been modified since the last time the function was called. The SHA1 hashes are stored in an SQLite3 database.
   
   :param outs: Ignored. Only here so it can be used with :py:func:`run_d`.
   :param deps: The dependencies.

.. py:function:: invoke(name, *args, **kw)
   
   Calls the task named `name`.
   
   :param name: The task to call.
   :param \*args: The positional arguments passed to the task.
   :param \*\*kwargs: The keyword arguments passed to the task.

.. py:function:: qinvoke(name, *args, **kw)
   
   The same thing as :py:func:`invoke`, but doesn't print the task that is executing.

.. py:function:: pinvoke(*args, **kw)
   
   The same thing as `invoke`, but, instead of running the task, launches it in a seperate process and returns a `multiprocessing.Process` object. See :py:func:`invoke`.

.. py:function:: pqinvoke(*args, **kw)
   
   The same thing as `pinvoke`, but doesn't print the task that is executing.

.. py:function:: cinvoke(category, invoker=invoke)
   
   Call `invoker` for every task contained within `category`. Note that, if the category itself is a task, it will not be called.

.. py:function:: run(cmd, write=True, shell=False, get_output=False)
   
   Run `cmd`.
   
   :param cmd: The command to run. If it is a string and `shell` is False, it will first be converted to a list.
   :param write: If `True`, the command will be printed to the screen before it's run.
   :param shell: If `True`, the command will be run in the shell.
   :param get_output: If `True`, a tuple consisting of `(stdout, stderr)` containing the command's output will be returned.

.. py:function:: run_d(outs, deps, cmd, func=need_to_update, **kw)
   
   Call `run` with `cmd` if `func`, when called with `outs` and `deps`, returns `True`. Doing:
   
   .. code-block:: python
      
      run_d('x.out', 'x.in', 'cp x.in x.out', func)
   
   Is equivalent to:
   
   .. code-block:: python
      
      if func('x.out', 'x.in'):
          run('cp x.in x.out')
   
   :param outs: The output files.
   :param deps: The dependencies.
   :param cmd: The command to run. See :py:func:`run`.
   :param \*\*kw: Keyword arguments passed to `run`. See :py:func:`run`.

.. py:function:: main(no_warn=False, default=None)
   
   Run the main driver. If `no_warn` is `True`, then no warnings about deprecated stuff will be displayed. If `default` is not `None`, it is assumed to be a string holding a task to run if no tasks were given on the command line.
