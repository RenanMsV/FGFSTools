import os
from sys import platform as _platform

icao = input('Enter Airport ID: ')
scenery = input('Any custom scenery location? ')
default = '--aircraft=ORCAM --callsign=_ --airport=' + icao + ' --telnet=,,100,,5010, --multiplay=in,100,,5010 --multiplay=out,100,localhost,5010 '

if _platform == "linux" or _platform == "linux2":
    # linux
    print()
elif _platform == "darwin":
    # MAC OS X
    print()
    final = './fgfs ' + default
    print('Trying to run : ' + final)
elif _platform == "win32":
    # Windows
    print()
    final = 'fgfs ' + default
if scenery:
    final = (final + '--fg-scenery="' + scenery + '"')
os.system(final)