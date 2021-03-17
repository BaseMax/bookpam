# Max Base
# 2020-12-13, 2020-12-14, 2020-12-15, 2021-03-17
# https://github.com/BaseMax/bookpam

import re
import sys

class BookPam:
    def __init__(self, bookname, filename):
        self.__NAME_BOOK = bookname
        self.__filename = filename
        try:
            self.__inputFile = open(sys.path[0]+"\\"+self.__filename, 'r')
            self.__data = self.__inputFile.read().strip()
        except Exception as err:
            print(err)
            sys.exit()
        self.__cover = ""
        self.__fehrest = ""
        self.__output = ""
        self.__functions_papers = ""
        self.__functions = []
        self.__start_book_pages = 0  # detect it's fehrest or not!
        self.__lines = self.__data.split("\n")
        self.__headers = []
        self.__status = 0
        self.__countLines = len(self.__lines)
        try:
            self.__layoutFile = open(sys.path[0]+"\\"+'layout.html', 'r')
            self.__layoutData = self.__layoutFile.read()
        except Exception as err:
            print(err)
            sys.exit()
        try:
            self.__styleFile = open(sys.path[0]+"\\"+'style.css', 'r')
            self.__styleData = self.__styleFile.read()
        except Exception as err:
            print(err)
            sys.exit()
        try:
            self.__scriptFile = open(sys.path[0]+"\\"+'script.js', 'r')
            self.__scriptData = self.__scriptFile.read()
        except Exception as err:
            print(err)
            sys.exit()

    def __appending(self, s):
        if self.__start_book_pages == 0:
            self.__cover += s
        else:
            self.__output += s

    def __rep_func(self, gp):
        if gp[1] not in self.__functions:
            self.__functions.append(gp[1])
        # print(gp[1])
        return '<kbd class="function">' + gp[1] + '</kbd>'

    def bookpam(self, outputname):

        i = 0
        while i < self.__countLines:
            self.__lines[i] = self.__lines[i].strip()
            if self.__lines[i].startswith('```'):
                if self.__status == 0:
                    self.__appending('<pre><code>\n')
                    self.__status = 1
                elif self.__status == 1:
                    self.__appending('</code></pre>')
                    self.__status = 0
                i = i + 1
                continue
            if self.__status == 1:
                self.__appending(self.__lines[i] + "\n")
                i = i + 1
                continue
            self.__lines[i] = re.sub(
                r'\{([^\}])\}', r'<img src="\1">', self.__lines[i])
            if self.__lines[i].startswith('######'):
                value = self.__lines[i][6:].strip()
                self.__lines[i] = '<h6>' + value + '</h6>'
                if self.__start_book_pages == 1:
                    self.__headers.append((6, value))
            if self.__lines[i].startswith('#####'):
                value = self.__lines[i][5:].strip()
                self.__lines[i] = '<h5>' + value + '</h5>'
                if self.__start_book_pages == 1:
                    self.__headers.append((5, value))
            if self.__lines[i].startswith('####'):
                value = self.__lines[i][4:].strip()
                self.__lines[i] = '<h4>' + value + '</h4>'
                if self.__start_book_pages == 1:
                    self.__headers.append((4, value))
            if self.__lines[i].startswith('###'):
                value = self.__lines[i][3:].strip()
                self.__lines[i] = '<h3>' + value + '</h3>'
                if self.__start_book_pages == 1:
                    self.__headers.append((3, value))
            if self.__lines[i].startswith('##'):
                value = self.__lines[i][2:].strip()
                self.__lines[i] = '<h2>' + value + '</h2>'
                if self.__start_book_pages == 1:
                    self.__headers.append((2, value))
            if self.__lines[i].startswith('#'):
                value = self.__lines[i][1:].strip()
                self.__lines[i] = '<h1>' + value + '</h1>'
                if self.__start_book_pages == 1:
                    self.__headers.append((1, value))
            self.__lines[i] = self.__lines[i].replace('[center]', '<center>')
            self.__lines[i] = self.__lines[i].replace('[/center]', '</center>')
            if self.__start_book_pages == 0 and '[page]' in self.__lines[i]:
                self.__start_book_pages = 1
            self.__lines[i] = self.__lines[i].replace('[page]', '<section>')
            self.__lines[i] = self.__lines[i].replace('[/page]', '</section>')
            self.__lines[i] = self.__lines[i].replace('[cover]', '<section>')
            self.__lines[i] = self.__lines[i].replace('[/cover]', '</section>')
            self.__lines[i] = re.sub(
                r'\{([^\}]+)\}', r'<img src="\1">', self.__lines[i])
            self.__lines[i] = re.sub(
                r'\<\<([^\>]+)\>\>', self.__rep_func, self.__lines[i])
            self.__lines[i] = re.sub(
                r'\`([^\`]+)\`', r'<kbd class="variable">\1</kbd>', self.__lines[i])
            if self.__lines[i] == "":
                try:
                    if self.__lines[i + 1].strip() == "":
                        i += 1
                except:
                    pass
                self.__appending("<br>\n")
            else:
                self.__appending(self.__lines[i])
            i += 1
        self.__fehrest = '<section class="fehrest"><h1>Contents</h1><ul>'
        for header in self.__headers:
            self.__fehrest += '<li class="sub-' + \
                str(header[0]) + '">' + header[1] + '</li>'
        self.__fehrest += "</ul></section>"

        # if you want to write a programming language or somethings similar...
        functions_papers = '<section class="functions"><h1>List of functions</h1><ul>'
        for function in self.__functions:
            functions_papers += '<li>' + function + '</li>'
        functions_papers += "</ul></section>"

        self.__output = self.__cover + self.__fehrest + self.__output + functions_papers

        self.__layoutData = self.__layoutData.replace(
            '{{title}}', self.__NAME_BOOK)
        self.__layoutData = self.__layoutData.replace(
            '{{style}}', self.__styleData)
        self.__layoutData = self.__layoutData.replace(
            '{{script}}', self.__scriptData)
        self.__layoutData = self.__layoutData.replace(
            '{{content}}', self.__output)

        outputFile = open(outputname + ".html", 'w')
        outputFile.write(self.__layoutData)
