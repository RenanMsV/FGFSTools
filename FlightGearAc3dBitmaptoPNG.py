sourcePath = "Models/"
outputPath = "OutModels\\"
deleteBMPFiles = False
from PIL import Image
import glob
import os
import re

logFile = open("log.txt", 'w')
fileout = open('fileout.txt', 'w')

print("Source Path : {} . Output Path : {} . Delete BMP Files : {} .\nContinue? Y | N".format(sourcePath,outputPath,deleteBMPFiles))
if not input() == 'Y':
	die()

def reportFilesByType(fileType):
	file = open("reportOutput.txt", "w")
	items = findFilesByType(fileType)
	for item in items:
		file.write(item+"\n")

def findFilesByType(fileType):
	return glob.iglob("{}**/*{}".format(sourcePath,fileType), recursive=True)

def convertImage (imagePath, imgOutPath, imgOutFormat = 'png'):
	debug("Opening Image: {}".format(imagePath))
	#logFile.write("Opening Image: " + imagePath+"\n")
	img = Image.open(imagePath)
	splited = imagePath.split('.')[:-1][0].split("\\")
	index = 0
	for x in range(0, len(splited)):
		string = outputPath
		for y in range(0, index):
			string += "\\" + splited[y]
		index += 1
		os.makedirs(string, exist_ok=True)
	localOutPath = "{}{}".format(imgOutPath, imagePath.split('.')[:-1][0])
	debug("Saving new Image at : {}.{}".format(localOutPath, imgOutFormat))
	#logFile.write("Saving new Image at : " + localOutPath+"\n")
	img.save( "{}.{}".format(localOutPath, imgOutFormat ))

def playAlertSound():
	import winsound
	winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

def debug(line, log=False, out = False):
	print(line.strip())
	if(log): logFile.write(line)
	if(out): fileout.write(line)

def deleteFile(path):
	try:
		os.remove(path)
	except:
		pass

def ac3dmodeltexturechange(path, tfrom, tto):
	lines = open(path).readlines()
	for lineindex, line in enumerate(lines): # for with line index so we can change it later
		if re.search(tfrom, line, re.IGNORECASE): # line contains the file extension
			debug("Found texture line at model: {}".format(line), out = True)
			if "/" not in line or re.search("C:/", line, re.IGNORECASE): # line not contains / meaning the image is in the same path
				if re.search("C:/", line, re.IGNORECASE):
					line = 'texture "{}"\n'.format(line.strip().split('"')[1].split("/")[-1])
				try:
					convertImage("{}\\{}".format("\\".join(path.split("\\")[:-1]), line.strip().split('"')[1]), outputPath)
					line = re.sub("(?i)" + tfrom, tto, line)
					lines[lineindex] = line
				except:
					debug("Image not found: {}\n".format("{}\\{}".format("\\".join(path.split("\\")[:-1]), line.strip().split('"')[1])), log = True)
	# code to change .ac model texture names correctly
	splited = path.split('.')[:-1][0].split("\\")
	index = 0
	for x in range(0, len(splited)):
		string = outputPath
		for y in range(0, index):
			string += "\\" + splited[y]
		index += 1
		os.makedirs(string, exist_ok=True)
	localOutPath = "{}{}".format(outputPath, path)
	debug("Opening Model: " + path)
	acmodel_out = open(localOutPath, 'w')
	debug("Saving new Model at: " + localOutPath)
	for line in lines:
		acmodel_out.write(line)
	debug("\n")

def newac3dtexturechange():
	for item in findFilesByType('.ac'):
		ac3dmodeltexturechange(item, ".bmp", ".png")
	if deleteBMPFiles:
		for item in findFilesByType('.bmp'):
			deleteFile(item)


newac3dtexturechange()
playAlertSound()
input("\n\nEnter to close")

# ainda precisa :
	