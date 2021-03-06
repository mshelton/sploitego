#!/usr/bin/env python

from os import path

from sploitego.utils.fs import fsemaphore, age, cookie
from sploitego.utils.wordlist import wordlist


__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'

__all__ = [
    'topsites'
]


def updatelist(filename):
    topsites = wordlist('http://www.google.com/adplanner/static/top1000/', '<a href="http://(.*?)/"target')
    f = fsemaphore(filename, 'wb')
    f.lockex()
    f.write('\n'.join(topsites))
    f.close()
    return topsites


def readlist(filename):
    f = fsemaphore(filename)
    f.locksh()
    data = wordlist('file://%s' % filename)
    f.close()
    return data


topsites = None
tmpfile = cookie('sploitego.adplanner.tmp')


if not path.exists(tmpfile) or age(tmpfile) >= 86400:
    topsites = updatelist(tmpfile)
else:
    topsites = readlist(tmpfile)





