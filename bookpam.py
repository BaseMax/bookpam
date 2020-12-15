# Max Base
# 2020-12-13, 2020-12-14, 2020-12-15
# https://github.com/BaseMax/bookpam

import re

filename = 'test.md'
inputFile = open(filename, 'r')
data = inputFile.read().strip()

cover = ""
fehrest = ""
output = ""
functions_papers = ""
functions = []

def appending(s):
	global cover
	global output
	if start_book_pages == 0:
		cover += s
	else:
		output += s

def rep_func(gp):
	if gp[1] not in functions:
		functions.append(gp[1])		
	# print(gp[1])
	return '<kbd class="function">' + gp[1] + '</kbd>'
	

lines = data.split("\n")

start_book_pages = 0 # detect it's fehrest or not!
headers = []
status = 0
countLines = len(lines)
i = 0
while i < countLines:
	lines[i] = lines[i].strip()
	if lines[i].startswith('```'):
		if status == 0:
			appending('<pre><code>\n')
			status = 1
		elif status == 1:
			appending('</code></pre>')
			status = 0
		i = i+1
		continue
	if status == 1:
		appending(lines[i]+"\n")
		i = i+1
		continue
	lines[i] = re.sub(r'\{([^\}])\}', r'<img src="\1">', lines[i])
	if lines[i].startswith('######'):
		value = lines[i][6:].strip()
		lines[i] = '<h6>' + value + '</h6>'
		if start_book_pages == 1:
			headers.append((6, value))
	if lines[i].startswith('#####'):
		value = lines[i][5:].strip()
		lines[i] = '<h5>' + value + '</h5>'
		if start_book_pages == 1:
			headers.append((5, value))
	if lines[i].startswith('####'):
		value = lines[i][4:].strip()
		lines[i] = '<h4>' + value + '</h4>'
		if start_book_pages == 1:
			headers.append((4, value))
	if lines[i].startswith('###'):
		value = lines[i][3:].strip()
		lines[i] = '<h3>' + value + '</h3>'
		if start_book_pages == 1:
			headers.append((3, value))
	if lines[i].startswith('##'):
		value = lines[i][2:].strip()
		lines[i] = '<h2>' + value + '</h2>'
		if start_book_pages == 1:
			headers.append((2, value))
	if lines[i].startswith('#'):
		value = lines[i][1:].strip()
		lines[i] = '<h1>' + value + '</h1>'
		if start_book_pages == 1:
			headers.append((1, value))
	lines[i] = lines[i].replace('[center]', '<center>')
	lines[i] = lines[i].replace('[/center]', '</center>')
	if start_book_pages == 0 and '[page]' in lines[i]:
		start_book_pages = 1
	lines[i] = lines[i].replace('[page]', '<section>')
	lines[i] = lines[i].replace('[/page]', '</section>')
	lines[i] = lines[i].replace('[cover]', '<section>')
	lines[i] = lines[i].replace('[/cover]', '</section>')
	lines[i] = re.sub(r'\{([^\}]+)\}', r'<img src="\1">', lines[i])
	lines[i] = re.sub(r'\<\<([^\>]+)\>\>', rep_func, lines[i])
	lines[i] = re.sub(r'\`([^\`]+)\`', r'<kbd class="variable">\1</kbd>', lines[i])
	# print("==>'"+ lines[i] +"'")
	if lines[i] == "":
		try:
			if lines[i+1].strip() == "":
				i+=1
		except:
			pass
		appending("<br>\n")
	else:
		appending(lines[i])
	i += 1
# print(data)

layoutFile = open('layout.html', 'r')
layoutData = layoutFile.read()

styleFile = open('style.css', 'r')
styleData = styleFile.read()

scriptFile = open('script.js', 'r')
scriptData = scriptFile.read()

# for
# print(headers)
fehrest = '<section class="fehrest"><h1>فهرست</h1><ul>'
for header in headers:
	fehrest += '<li class="sub-' + str(header[0]) + '">' + header[1] + '</li>'
fehrest += "</ul></section>"

functions_papers = '<section class="functions"><h1>توابع</h1><ul>'
for function in functions:
	functions_papers += '<li>' + function + '</li>'
functions_papers += "</ul></section>"

output = cover + fehrest + output + functions_papers

layoutData = layoutData.replace('{{title}}', 'گپ: از نظریه گروه تا برنامه نویسی')
layoutData = layoutData.replace('{{style}}', styleData)
layoutData = layoutData.replace('{{script}}', scriptData)
layoutData = layoutData.replace('{{content}}', output)

outputFile = open('output.html', 'w')
outputFile.write(layoutData)
