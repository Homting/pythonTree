import os,sys

fileCount = 0
lineCount = 0
extision = ["c","cpp","java","html","js","css","py","pl","h","m"]
extision = ["py"]
def function(dirName):
	global fileCount,lineCount,extision
	for dirname,dirfiles,filename in os.walk(dirName):
		for f in filename:
			fame = os.path.join(dirname,f)
			try:
				ext = f.split('.')[-1]
				if (ext in extision):
					fileCount +=1
					l_count = len(open(fame).readlines())
					print fame,": ",l_count
					lineCount += l_count
			except:
				print fame,"error occur!"
				pass

function(".")

print "~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "total"
print "fileCount: ",fileCount
print "lineCount: ",lineCount

