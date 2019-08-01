import telnetlib
import os
import sys
import math

#host = 'mpserver{:02d}.flightgear.org'
#max_server_number = 51

# https://github.com/pigeond/fgmap/blob/master/sg_perl/sgmath.cxx
# http://mpmap02.flightgear.org/v3/fg_server_xml.cgi?mpserver01.flightgear.org:5001

class SGVec3f:
	"""From Simgear Fgmap for SGVec3f"""
	def __init__(self):
		self.SGD_PI = math.pi
		self.SGD_DEGREES_TO_RADIANS = SGD_PI / 180.0
		self.SGMISC_PI = float('3.1415926535897932384626433832795029')
	def rad2deg(self, val):
		return val * 180 / self.SGMISC_PI

class SGQuatf:
	"""From Simgear Fgmap for SGQuatf"""
	def __init__(self):
		return self

class FGMap_PilotData:
	def __init__(self, line):
		start = line.split(': ')
		values = start[1].split(' ')
		server = start[0].split('@')
		self.callsign = server[0]
		self.server = server[1]
		self.world_X = float(values[0])
		self.world_Y = float(values[1])
		self.world_Z = float(values[2])
		self.lat = float(values[3])
		self.lon = float(values[4])
		self.alt = float(values[5])
		self.roll = float(values[6])
		self.pitch = float(values[7])
		self.heading = float(values[8])
		self.model = values[9]
		#AF2222@LOCAL: 4211743.703738 173479.991783 4770691.733736 48.727522 2.358656 291.600867 -2.492445 -1.092461 0.953486 Aircraft/777/Models/777-200ER.xml

class FGTelNetQuery:
	"""Class for FGTelNetQuery"""
	def __init__(self, server, port):
		self.server = server
		self.port = port
		self.pilots = []
	def connect(self):
		try:
			self.telnet_fg = telnetlib.Telnet(self.server, self.port) # conecting to the server
		except Exception as e:
			print("Could not connect. Check server and port. " + str(e))
			return False
		self.output = self.telnet_fg.read_all()
		return True
	def disconnect(self):
		self.telnet_fg.close()
	def showresults(self):
		lines = self.output.decode('utf-8').split('\n')
		for i in range(0, len(lines)-1):
			if('#' in lines[i][0] or ' ' in lines[i][0]): # if line begins with # or white space abort
				continue
			print("#"*50)
			print(" Line {} : ".format(i))
			print("#"*50)
			data = FGMap_PilotData(lines[i])
			self.pilots.append(data)
			print("Callsign: {} Server: {} Lat: {}  Lon: {}  Alt: {} Roll: {} Pitch: {} Heading: {} Model: {}".format(data.callsign, data.server, data.lat, data.lon, data.alt, data.roll, data.pitch, data.heading, data.model))
	def exportresults(self, filename):
		open(filename,'w').write(self.output.decode('utf-8'))
	def getpilots(self):
		return self.pilots
	def processpposition(self, lat, lon, ox, oy, oz):

		return 1

print('Starting... Python v{}'.format(sys.version))
query = FGTelNetQuery('mpserver01.flightgear.org', 5001)
if (query.connect()):
	query.exportresults('telnetresult.txt')
	query.showresults()
	query.disconnect()

	print("\nPilot List:")
	for pilot in query.getpilots():
		print("{} --#-- {}".format(pilot.callsign, pilot.model))
	print('\n')
	for pilot in query.getpilots():
		print("{} --#-- {}".format(pilot.callsign, pilot.heading))

os.system('PAUSE')