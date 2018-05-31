.. Visi Debugger documentation master file, created by
   sphinx-quickstart on Sun Nov 18 18:18:58 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the VDB documentation!
=================================

About
-----

.. warning::

    The documentation for VDB is still very much under development! If you want to contribute (or have ideas for better documentation), feel free to `send me a pull request`_ or `email me`_.

.. _send me a pull request: https://github.com/Fitblip/vdb-fork
.. _email me: https://github.com/Fitblip

VDB is a (mostly) python-based multi-debugging platform written by `@invisig0th`_ from the `Kenshoto`_ team. 

It's more of a layer of abstraction written around native debugging platforms and techniques (e.g. ptrace, and Windows native API debugging), which allows you to have a same basic process for debugging executables on Windows/*nix/OSX platforms.

`@invisig0th`_ has done an amazing job, and written this project pretty much by himself. I (`@fitblip`_) have taken it upon myself to start documentation for this project in my spare time, because this project needs it!

I've also added a few of `my own`_ changes to `@invisig0th`_'s code, and fixed a couple bugs. Eventually (hopefully) they'll be merged into the next release!

Another excellent resource is `the VDB wiki itself`_, which just got redone and is now much more responsive. 

.. _@invisig0th: https://twitter.com/invisig0th
.. _@fitblip: https://twitter.com/fitblip
.. _Kenshoto: http://kenshoto.com/
.. _my own: https://github.com/Fitblip/vdb-fork#major-differences
.. _the VDB wiki itself: http://visi.kenshoto.com/

Installation
------------
Either download the `most recent snapshot`_ from visi's page, or `clone my repo`_.

Extract it to a directory you like, then do something like this in your code::

	# Import standard modules
	import os
	import sys

	# Setup our VDB path
	vdb_path = "C:\\PathToVDB\\vdb_20120806"
	
	# Insert VDB directory in search path
	if vdb_path: sys.path.insert(1,vdb_path)
	
	# Import PE and vtrace
	import PE, vtrace

There isn't a setup.py for this project, nor will there probably be, as it changes so quickly. If you really have gripes with that, send me a pull request :-P. 

If you want to use the PyQt interface, obviously you need that as well!

.. _most recent snapshot: http://visi.kenshoto.com/static/releases/
.. _clone my repo: https://github.com/Fitblip/vdb-fork


Tutorials/Examples
------------------
`At my blog`_ you can find a few examples and tutorials (more to come), but watch this space, as the tutorials page is coming!

.. _At my blog: http://www.talesofacoldadmin.com

API Refrence
------------
You can find the API reference 

Contributing
------------

1. `My github repo`_ will take and manage any pull request you can throw at it!
2. Email visi himself
3. `Create me an issue`_ for a feature you want/bug you've found, and I'll see what I can do with

.. _My github repo: https://github.com/Fitblip/vdb-fork
.. _Create me an issue: https://github.com/Fitblip/vdb-fork/issues

State of Project
----------------
Visi is a busy man, but he's no doubt working on the next release. `You can checkout his ReleaseNotes`_ which gives you a good update on the progress he's making. You can also check out `my commit history`_ to see the commits I've made myself.

.. _You can checkout his ReleaseNotes: http://visi.kenshoto.com/viki/ReleaseNotes
.. _my commit history: https://github.com/Fitblip/vdb-fork/commits/master

Credit
------
This is `@invisig0th`_'s project in it's entirety. He's the only author, although there have been some outside contributions in the past, mostly from within the Kenshoto team. 

.. _@invisig0th: https://twitter.com/invisig0th


License
-------
Visi has a license somewhere, but I need to poke him, as it doesn't specify anywhere in the code, and the LICENSE file is missing in newer releases. 