###################################################################################
#                                                                                 #
#           This is HTML and DIJ files generator.                                 #
#                                                                                 #
#           This script was created by Dawid Kolodziej for Tech Support use only  #
#                                                                                 #
###################################################################################
import os
import configparser
from ast import literal_eval


# Creating folder for DIJ and HTML files
path = ["dijfolder", "htmlfolder"]

for z in path:
    doesExist = os.path.exists(z)
    if not doesExist:
        os.mkdir(z)


# import user settings and prefix from the config.txt file
config = configparser.ConfigParser()
config.read('config.txt')

DIJ = config.get('numbers', 'DIJ')
files = config.get('numbers', 'files')
prefix = config.get('prefix', 'prefix')


# import HTML code from html_body.txt file and creating HTML files
htmlconfig = configparser.RawConfigParser()
htmlconfig.read('html_body.txt')

for x in range(1, int(DIJ) + 1):
    ID = f"{prefix}{x:04d}XXXXXXXXXXXXXXXXXX"

    for i in range(1, int(files) + 1):
        html_head = htmlconfig.get('htmlbody', 'html_head')
        link = '''<!-- ''' + str(ID) + f"{i:04d}" ''' -->'''
        html_body = htmlconfig.get('htmlbody', 'html_body')
        filename = f".\\htmlfolder\\file{x}_000{i:04d}.html"
        html = html_head + "\n" + link + "\n" + html_body

        with open(filename, "w") as file:
            file.write(html)


# import a code from the DIJ.txt file and creating required DIJ files
    filename = f".\\dijfolder\\file{x}.DIJ"

    dijconfig = configparser.RawConfigParser()
    dijconfig.read("dij.txt")

    documentID = '''<document docID="''' + str(i) + f'''" docInstanceID="''' + str(ID) + f"{i:04d}" + '''">'''

    with open(filename, "w") as file:
        text = dijconfig.get('DIJ', 'text')
        file.write(text)
        for i in range(1, int(files) + 1):
            document = dijconfig.get('DIJ', 'document')
            DIJdoc = documentID + "\n" + document
            file.write(DIJdoc)
        file.write('''</eGAD>''')


# creating a new prefix and writing it to the config.txt file
hval = '0x' + prefix
convert_hval = literal_eval(hval) + 1
hex_convert_hval = hex(convert_hval)
a = hex_convert_hval.replace('0x', '')

config.set('prefix', 'prefix', a)
with open('config.txt', 'w') as configfile:
    config.write(configfile)
