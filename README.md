#Python OpenLibrary#

__A Python wrapper for the OpenLibrary API.__

This library provides a pure [Python](http://python.org) interface for the [OpenLibrary API](http://openlibrary.org/developers/api).
[OpenLibrary](http://openlibrary.org) is an online project of the non-profit [Internet Archive](http://www.archive.org)
which intends to create _"one web page for every book ever publised"_.

[OpenLibrary.org](http://openlibrary.org)

___

##Building##

###Dependencies###

* **simplejson**: http://cheeseshop.python.org/pypi/simplejson

###From Source:###

Download the latest **python-openlibrary**:

https://github.com/felipeborges/python-openlibrary

Unpack it and run:

    $ sudo python setup.py build
    $ sudo python setup.py install

___

##Using##

###Documentation###

    $ pydoc openlibrary.Publisher
    $ pydoc openlibrary.Author
    $ pydoc openlibrary.Book

###Example###

To create an instance of the openlibrary.Api class:

    >>> import openlibrary
    >>> api = openlibrary.Api()

To get a Book by its ISBN number:

    >>> book = api.get_book("0451526538")
    'The adventures of Tom Sawyer'

To get a Book by its OLID (Open Library ID):

    >>> book = api.get_book("OL123M", "OLID")
    'Stories of Indian life.'

To get the Authors of this given Book:

    >>> authors = book.get_authors()
    >>> print [author.get_name() for author in authors]

___

## License ##

        Copyright 2011 Felipe Borges <felipe10borges@gmail.com>
  
        This program is free software; you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation; either version 2 of the License, or
        (at your option) any later version.
  
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program; if not, write to the Free Software
        Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
        MA 02110-1301, USA.
