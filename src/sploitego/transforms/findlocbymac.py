#!/usr/bin/env python

from sploitego.maltego.message import IPv4Address, UIMessage
from sploitego.framework import configure
from common.reversegeo import getlocbymac


__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
    'onterminate'
]


@configure(
    label='To Locations [Google Maps]',
    description='Gets device locations based on MAC address.',
    uuids=[ 'sploitego.v2.IPv4AddressToLocation_GoogleMaps' ],
    inputs=[ ( None, IPv4Address ) ]
)
def dotransform(request, response):
    if 'ethernet.hwaddr' not in request.fields or not request.fields['ethernet.hwaddr']:
        response += UIMessage('You must provide an Ethernet Hardware Address (ethernet.hwaddr) property.')
    else:
        response += getlocbymac(request.fields['ethernet.hwaddr'])
    return response