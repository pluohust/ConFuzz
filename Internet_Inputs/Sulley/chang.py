readhandle=open('./1','r')
writehandle=open('./2','w')
while True:
	oneline=readhandle.readline()
	if oneline:
		oneline=oneline.strip()
		if len(oneline)>1:
			writehandle.write('	sess.connect(s_get(\"'+oneline+'\"))\n')
	else:
		break
readhandle.close()
writehandle.close()