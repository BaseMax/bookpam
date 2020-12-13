# Max Base
# 2020-12-13
# https://github.com/BaseMax/bookpam

import re

filename = 'book.md'
filename = 'test.md'
inputFile = open(filename, 'r')
data = inputFile.read().strip()

output = ""

lines = data.split("\n")

status = 0
countLines = len(lines)
i = 0
while i < countLines:
	lines[i] = lines[i].strip()
	if lines[i].startswith('```'):
		if status == 0:
			output += '<pre><code>\n';
			status = 1
		elif status == 1:
			output += '</code></pre>';
			status = 0
		i = i+1
		continue
	if status == 1:
		output += lines[i]+"\n"
		i = i+1
		continue
	lines[i] = re.sub(r'\{([^\}])\}', r'<img src="\1">', lines[i])
	if lines[i].startswith('######'):
		lines[i] = '<h6>' + lines[i][6:].strip() + '</h6>'
	if lines[i].startswith('#####'):
		lines[i] = '<h5>' + lines[i][5:].strip() + '</h5>'
	if lines[i].startswith('####'):
		lines[i] = '<h4>' + lines[i][4:].strip() + '</h4>'
	if lines[i].startswith('###'):
		lines[i] = '<h3>' + lines[i][3:].strip() + '</h3>'
	if lines[i].startswith('##'):
		lines[i] = '<h2>' + lines[i][2:].strip() + '</h2>'
	if lines[i].startswith('#'):
		lines[i] = '<h1>' + lines[i][1:].strip() + '</h1>'
	lines[i] = lines[i].replace('[center]', '<center>')
	lines[i] = lines[i].replace('[/center]', '</center>')
	lines[i] = lines[i].replace('[page]', '<section>')
	lines[i] = lines[i].replace('[/page]', '</section>')
	lines[i] = re.sub(r'\{([^\}]+)\}', r'<img src="\1">', lines[i])
	lines[i] = re.sub(r'\`([^\`]+)\`', r'<kbd>\1</kbd>', lines[i])
	# print("==>'"+ lines[i] +"'")
	if lines[i] == "":
		try:
			if lines[i+1].strip() == "":
				i+=1
		except:
			pass
		output += "<br>\n"
	else:
		output += lines[i]
	i += 1
# print(data)

layoutFile = open('layout.html', 'r')
layoutData = layoutFile.read()
layoutData = layoutData.replace('{{title}}', 'گپ: از نظریه گروه تا برنامه نویسی')
layoutData = layoutData.replace('{{content}}', output)

outputFile = open('output.html', 'w')
outputFile.write(layoutData)
