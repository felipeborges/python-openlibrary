#Python OpenLibrary

It's a Python wrapper for the OpenLibrary API.

##Example

To create an instance of the openlibrary.Api class:

    >>> import openlibrary
    >>> api = openlibrary.Api()

To get a book:

    >>> book = api.GetBook("0451526538")
    'The adventures of Tom Sawyer'
