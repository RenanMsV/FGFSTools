import glob
import os
import time
from shutil import copyfile

#input('Select your Language/Selecione sua Linguagem. : 0 English | 1 Português ')

root = os.getcwd().replace('\\', '/')
xmls = glob.glob('*.xml')
if not xmls:
    print('Error: No ICAO.xml files found')
else:
    print('Converting ' + str(xmls.__len__()) + ' procedures files...')
    time.sleep(5)
for xml in xmls : 
    path = list(xml)
    tree = root + '/Airports/' + path[0] + '/' + path[1] + '/' + path[2] + '/'
    path = tree + xml.split('.')[0] + '.procedures.xml'
    os.makedirs(tree, exist_ok=True)
    copyfile(xml, path)
    print(xml.split('.')[0] + ' file converted.')
input('Done. ENTER to exit.')
