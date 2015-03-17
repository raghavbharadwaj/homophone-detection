import sys
import os
import subprocess

testfile = open(sys.argv[1],'r')

for line in testfile:
	f=open('training_file','w')
	f.write(line)
	f.close()
	label = line.split()[0]
	if label == "their" or label=="they_re":
		subprocess.call(["megam", "-nc", "-predict", "weights_their", "multitron",'training_file'])
	
	if label == "your" or label=="you_re":
		subprocess.call(["megam", "-nc", "-predict", "weights_your", "multitron",'training_file'])

	
	if label == "its" or label=="it_s":
		subprocess.call(["megam", "-nc", "-predict", "weights_its", "multitron",'training_file'])

	
	if label == "to" or label=="too":
		subprocess.call(["megam", "-nc", "-predict", "weights_to", "multitron",'training_file'])

	
	if label == "lose" or label=="loose":
		subprocess.call(["megam", "-nc", "-predict", "weights_loose", "multitron",'training_file'])


testfile.close()
