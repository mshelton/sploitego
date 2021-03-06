#!/usr/bin/env python

from pkg_resources import resource_filename
from os import path

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = [ 'Nadeem Douba' ]

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'

images = 'sploitego.resources.images'
etc = 'sploitego.resources.etc'

def imageicon(cat, name):
    return 'file://%s' % resource_filename('.'.join([ images, cat ]), name)

def imagepath(cat, name):
    return '%s' % resource_filename('.'.join([ images, cat ]), name)

# networking
unavailableport = imageicon('networking', 'unavailableport.gif')
openport = imageicon('networking', 'openport.gif')
timedoutport = imageicon('networking', 'timedoutport.gif')
closedport = imageicon('networking', 'closed_port.gif')

# severity
critical = imageicon('severity', 'critical.gif')
high = imageicon('severity', 'high.gif')
medium = imageicon('severity', 'medium.gif')
low = imageicon('severity', 'low.gif')
info = imageicon('severity', 'info.gif')

# logos
nmap = imagepath('logos', 'nmap.gif')
metasploit = imagepath('logos', 'metasploit.png')
nessus = imagepath('logos', 'nessus.png')

# etc
conf = resource_filename(etc, 'sploitego.conf')

# flags
def flag(c):
    f = imageicon('flags', '%s.png' % c.lower())
    if path.exists(f[7:]):
        return f
    return None