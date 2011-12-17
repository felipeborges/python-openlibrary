#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''A Python wrapper for the OpenLibrary API.'''

import urllib2
import simplejson

__author__ = "Felipe Borges <felipe10borges@gmail.com>"

class Publisher(object):
    '''A class represeting a Book Publisher.
    '''
    def __init__(self,
                 name = None):
        self.name = name

    def get_name(self):
        '''Get the Publisher name.
        
        Returns:
            The Publisher name.
        '''
        return self.name
		
    @staticmethod
    def get_publisher_from_json_dict(data):
        '''Creates a new Publisher instance based on a JSON dict.
		
        Args:
            data: a Json dictionary
        Returns:
            A Publisher instance
        '''
        return Publisher(data.get('name'))	
		
    def __str__(self):
        '''String representation of a Publisher.
        
        Returns:
            A string representation of a Publisher.
        '''
        return self.name

class Author(object):
    '''A class representing a Book Author.
    '''
    def __init__(self,
                name = None,
                url = None):
        self.name = name
        self.url = url
        
    def get_name(self):
        '''Get the author name.
        
        Returns:
            The author name.
        '''
        return self.name
      
    def get_url(self):
        '''Get the author url.
        
        Returns:
            The author URL.
		'''
        return self.url
        
    @staticmethod
    def get_author_from_json_dict(data):
        '''Creates a new Author instance based on a JSON dict.
		
        Args:
            data: a Json dictionary
        Returns:
            An Author instance
        '''
        return Author(data.get('name', None),
                      data.get('url', None))
	
    def __str__(self):
        return self.name

class Book(object):
    '''A class representing an OpenLibrary Book entry.
    '''
    def __init__(self,
                publishers = None,
                identifiers = None,
                classifications = None,
                links = None,
                weight = None,
                title = None,
                subtitle = None,
                url = None,
                number_of_pages = None,
                cover = None,
                subjects = None,
                publish_date = None,
                excerpts = None,
                authors = None,
                publish_places = None):

        self.publishers = publishers
        self.identifiers = identifiers
        self.classifications = classifications
        self.links = links
        self.weight = weight
        self.title = title
        self.subtitle = subtitle
        self.url = url
        self.number_of_pages = number_of_pages
        self.cover = cover
        self.subjects = subjects
        self.publish_date = publish_date
        self.excerpts = excerpts
        self.authors = authors
        self.publish_places = publish_places
		
    def get_title(self):
        '''Get the title of this Book.
		
        Returns:
            The Title of this Book.
        '''
        return self.title
		
    def get_authors(self):
        '''Get the list of authors of this book.
		
        Returns:
            The list of authors of this book
        '''
        return self.authors
		
    def get_publishers(self):
        '''Get a list of publishers of this book.
		
        Returns:
            A list of Publishers of this book.
		
        '''
        return self.publishers
        
    def get_number_of_pages(self):
        '''Get the number of pages of the Book.
        
        Returns:
            The number of pages of the Book.
        '''
        return self.number_of_pages
      
    def get_book_cover(self):
        '''Get the Book cover.
        
        Returns:
            The Book cover.
        '''
        return self.cover
        
    @staticmethod
    def get_book_from_json_dict(data):
        '''Creates a new Book instance based on a JSON dict.
		
        Args:
            data: a Json dictionary
        Returns:
            A Book instance
        '''
        publishers = [Publisher.get_publisher_from_json_dict(p) for p in data['publishers']]
        authors = [Author.get_author_from_json_dict(a) for a in data['authors']]
		
        return Book(publishers = publishers,
                    identifiers = data.get('identifiers', None),
                    classifications = data.get('classifications', None),
                    links = data.get('links', None),
                    weight = data.get('weight', None),
                    title = data.get('title', None),
                    subtitle = data.get('subtitle', None),
                    url = data.get('url', None),
                    number_of_pages = data.get('number_of_pages', None),
                    cover = data.get('cover', None),
                    subjects = data.get('subjects', None),
                    publish_date = data.get('publish_date', None),
                    excerpts = data.get('excerpts', None),
                    authors = authors,
                    publish_places = data.get('publish_places', None))
	
    def __str__(self):
        '''A string representation of this Book instance.
		
        Returns:
            A string representation of this Book instance.
        '''
        return self.title

class Api:
    def __init__(self):
        self.base_url = "http://openlibrary.org/api/books?bibkeys="
		
    def get_book(self, id, bibkey = "ISBN"):
        '''Get a Book by its ID: ISBN (default), LCCN, OCLC
        or OLID (Open Library ID).
        
        Returns:
            A Book instance.
        '''
        url = urllib2.urlopen(self.base_url+bibkey+":%s&jscmd=data&format=json" % id)
        data = simplejson.load(url)['%s:%s' % (bibkey, id)]
        return Book.get_book_from_json_dict(data)
