__author__ = 'mike'

import lxml.html

from lxml.html import etree
# from lxml.html.soupparser import etree

print("hello world")

parser = lxml.html.HTMLParser()
tree = etree.parse('e:\\users\\mike\\documents\\bookmarks_12_5_14_small.html', parser)
root = tree.getroot()




for element in root.iter('a'):
    print("%s - %s - %s" % (element.tag, element.text, element.attrib))

print("hello world")







