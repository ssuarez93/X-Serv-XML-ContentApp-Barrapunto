#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Simple XML parser for the RSS channel from BarraPunto
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#
# Just prints the news (and urls) in BarraPunto.com,
#  after reading the corresponding RSS channel.

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import urllib

def normalize_whitespace(text):
    "Remove redundant whitespace from a string"
    return string.join(string.split(text), ' ')

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.response = "<h3>Titulares de Barrapunto.com:</h3>"

    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.response += "Title: " + self.theContent + "." + "</br>"
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                self.response += " Link: " + "<a href='" + self.theContent + \
                                "'>" + self.theContent + "</a>" + "." + "</br>"
                self.inContent = False
                self.theContent = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

# --- Main prog

# Load parser and driver
def parse():
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
# Ready, set, go!
    xmlURL = "http://barrapunto.com/index.rss"
    theParser.parse(xmlURL)
    return theHandler.response
