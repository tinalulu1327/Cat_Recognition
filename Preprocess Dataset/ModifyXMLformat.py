"""
 AUTHOR : Xiaolu Zhang
 PURPOSE : Dataset preprocess
"""

# coding=utf-8
import os
import os.path
import xml.dom.minidom

path = "./xmls/"
files = os.listdir (path)
s = []
for xmlFile in files:
    if not os.path.isdir (xmlFile):
        print (xmlFile)
    try:
        dom = xml.dom.minidom.parse (os.path.join (path, xmlFile))
        root = dom.documentElement

        folder = root.getElementsByTagName ('folder')
        folder[0].firstChild.data = 'image'

        with open(os.path.join(path,xmlFile),'w') as fh:
            root.writexml(fh)
        print('OK!')
    except:
        print('Error')

print ("Finish")
