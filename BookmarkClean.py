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

clean_links = {}
pre_text = "<DT><A "
post_text = "</A>"

for element in root.iter("a"):
    # print("%s - %s - %s" % (element.tag, element.attrib, element.text))
    clean_links[element.text] = element.attrib
    # if (len(clean_links) > 10) :
    # break

for link in sorted(clean_links.keys()):
    line = pre_text
    for attrib_key in clean_links[link].keys():
        line += " "
        line += str(attrib_key).upper() + "=" + '"'
        line += clean_links[link][attrib_key]
        line += '"'
    line += ">" + link + post_text
    print(line)






