Overview
--------

incipio is a Python package for automatically generating a lot of the
boilerplate that comes with starting a new Python package. The aim is for you
to be able to start Python, import incipio, execute one function, and have the
package be created to order.

Package Creation
~~~~~~~~~~~~~~~~

The :py:func:`.create_package` is used to create Python packages. The following
will create a Python package called 'pyAwesome' in the user's home directory:

    >>> import incipio
    >>> incipio.create_package("pyAwesome", "/home/guido")

The author's name needs to appear in a lot of places, and this can be provided
easily enough:

    >>> incipio.create_package("pyAwesome", "/home/guido", author="Guido R")
