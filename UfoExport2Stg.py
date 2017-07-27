# by jam007 some changes by BR-RVD

from os.path import isfile

if not isfile('ufo-model-export.xml'):
	input('UFO File not Found. Enter to exit')
	exit() 

import lxml.etree as etree

file = open('object-line.stg','w') 
tree = etree.parse('ufo-model-export.xml')

root = tree.getroot()
l=[]
for amodel in root.iter('model'):
    l.append((amodel.find('stg-path').text, amodel.find('object-line').text) )
l.sort()
stg=''
for obj in l:
    if obj[0] != stg :
        file.write(obj[0]+'\n')
        print(obj[0])
        stg=obj[0]
    file.write(obj[1]+'\n')
    print(obj[1])
file.close();
input('\n\nOutput File Saved')