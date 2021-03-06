#!/usr/bin/env python

from sploitego.cmdtools.nmap import NmapScanner, NmapReportParser
from common.nmap import addreport, addports, addsystems
from sploitego.framework import configure, superuser
from sploitego.maltego.message import IPv4Address
from sploitego.maltego.utils import debug

__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = ['Nadeem Douba']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'


__all__ = [
    'dotransform'
]


@superuser
@configure(
    label='To Ports [Nmap -A]',
    description='This transform performs an active Nmap scan.',
    uuids=[ 'sploitego.v2.IPv4AddressToPort_NmapA' ],
    inputs=[ ( 'Reconnaissance', IPv4Address ) ],
)
def dotransform(request, response):
    target = request.value
    s = NmapScanner()
    debug('Starting scan on host: %s' % target)
    r = s.scan(['-n', '-A', target] + list(request.params), NmapReportParser)
    addports(r, response)
    addsystems(r, response)
    addreport(r, response, '-A')
    return response
