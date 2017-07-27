#
import os.path
import re
import gzip
import shutil
#import time
if not os.path.isfile('WPNAVFIX.txt'):
    input('File WPNAVFIX.txt not found. ENTER to exit.')
    exit()
file = open('fix.dat','w')
content = open('WPNAVFIX.txt').readlines()
output = ["; Cicle 1705. by RenanMsV"]
i = 0
for line in content: # pegando a versão do airac
    if line.startswith(';AIRAC Cycle : '): 
        output = ["; Cicle {}. by RenanMsV\n;".format(line.split(';AIRAC Cycle : ')[1][:4])]
    if line.startswith(';'):
        content.remove(content[i])
        i = i+1
        continue
    print('Converting line ' + str(i) + ': ' + line)
    coord = line[29:]
    coord1 = coord[:10].rstrip()
    coord2 = coord[10:].rstrip()
    coord11 = coord1.split('.')[0].replace(' ', '')
    coord12 = coord1.split('.')[1].replace(' ', '')
    coord1 = coord11.zfill(3) + '.' + coord12.zfill(6)
    coord21 = coord2.split('.')[0].replace(' ', '')
    coord22 = coord2.split('.')[1].replace(' ', '')
    coord2 = coord21.zfill(3) + '.' + coord22.zfill(6)
    out = coord1 + ' ' + coord2 + ' ' + line.split(' ')[0]
    output.append(out)
    i = i+1
for x in output:
    file.write(x + '\n')
file.close()
with open('fix.dat', 'rb') as f_in, gzip.open('fix.dat.gz', 'wb') as f_out: # zipando em gzip
    shutil.copyfileobj(f_in, f_out)
os.remove('fix.dat')
input('Done. ENTER to exit.')
