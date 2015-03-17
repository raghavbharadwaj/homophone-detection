import sys
import os
dataset = sys.argv[1]

#corpus = open(dataset, 'r')
#c = open(sys.argv[2], 'w')

#labels=["to","too","you_re","your","lose","loose","their","they_re","its","it_s"]
labels = ["too","to"]
contents=open(sys.argv[1],'r')
for line in contents:
	words = line.split()
	for i in range(0,len(words)):
		if words[i].split('/')[0].lower() in labels:
			if i!=len(words)-1:
				features = words[i].split('/')[0].lower()+" "+"prevword:"+words[i-1].split('/')[0]+" prevpos:"+words[i-1].split('/')[1]+" nexword:"+words[i+1].split('/')[0]+" nexpos:"+words[i+1].split('/')[1]
			else:
				features = words[i].split('/')[0].lower()+" "+"prevword:"+words[i-1].split('/')[0]+" prevpos:"+words[i-1].split('/')[1]+" nexword:EOS nexpos:EOSPOS"

			print(features)
contents.close()
				
