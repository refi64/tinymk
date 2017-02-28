Command-line reference
======================

Usage::

   build_script [-h|--help] [--task-help] <task> [<args>]

.. option:: -h, --help

  Show the help screen.

.. option:: --task-help

  Print information on specifying task names. See :ref:`task_info`.

.. option:: task

  The task to call. See :ref:`task_info`.

.. option:: args

  Arguments passed to the task.

.. _task_info:

Specifying task names
*********************

Tasks are organized into groups called categories. For example, this task name::

  a:b:c

is referring to the task `c` inside the category `b` inside the category `a`.

If you do this::

  a:b:?

the tasks belonging to the category `b` inside the category `a` will be printed.

If you do this::

  a:b:c?

it will print information about the task `c` inside `b` inside `a`.
