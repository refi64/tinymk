Introduction/FAQ
================

Why another build tool?
***********************

There's no real reason; I just wanted to experiment. After using build systems like `Shake <http://shakebuild.com>`_ (very powerful but complex) and `Cake <http://coffeescript.org/#cake>`_ (simple and elegant but very rebuild-the-wheel type), I wanted a mix. I like Haskell, but I don't like it enough to work with it that much. TinyMk is written in Python, which is pre-installed on most Unix-like platforms, and is very portable. One thing I especially liked about Cake was the use of creative prefixes (task *build* calls *build:objects* and *build:library*). TinyMk implements this using categories.

Is TinyMk better than *x*?
**************************

No. Every build system has different goals/concepts. It's useless to ask if *x* is better than *y* when they have completely different end goals.

Of course, when comparing *x* to CMake/autotools, *x* always wins.

Why is the documentation so out-of-date?
****************************************

Work-in-progress. I hate writing API docs.

I have a question about using TinyMk. Where should I go?
********************************************************

Use the `mailing list <https://groups.google.com/forum/#!forum/tinymk>`_: tinymk@googlegroups.com.
