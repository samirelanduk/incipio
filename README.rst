incipio
=======

incipio is a Python package for creating Python packages.

Example
-------

  >>> import incipio
  >>> incipio.create_package("pyAwesome", ".", author="Guido")




Installing
----------

pip
~~~

incipio can be installed using pip:

``$ pip install incipio``

incipio is written for Python 3. If the above installation fails, it may be
that your system uses ``pip`` for the Python 2 version - if so, try:

``$ pip3 install incipio``

Requirements
~~~~~~~~~~~~

incipio currently has no dependencies.


Overview
--------

incipio is a Python package for automatically generating a lot of the
boilerplate that comes with starting a new Python package. The aim is for you
to be able to start Python, import incipio, execute one function, and have the
package be created to order.

Package Creation
~~~~~~~~~~~~~~~~

The ``create_package`` is used to create Python packages. The following
will create a Python package called 'pyAwesome' in the user's home directory:

    >>> import incipio
    >>> incipio.create_package("pyAwesome", "/home/guido")

The author's name needs to appear in a lot of places, and this can be provided
easily enough:

    >>> incipio.create_package("pyAwesome", "/home/guido", author="Guido R")


Changelog
---------

Release 0.1.0
~~~~~~~~~~~~~

`14 March 2017`

* Added basic package creation with virtual environments, git repositories, and tests.
