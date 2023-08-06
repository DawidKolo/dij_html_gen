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
import string


# import user settings and prefix from the config.txt file
config = configparser.ConfigParser()
config.read('config.txt')

DIJ = config.get('numbers', 'DIJ')
files = config.get('numbers', 'files')
prefix = config.get('prefix', 'prefix')
ballast = config.get('numbers', 'html_size')


# checking if required values are correct
if not DIJ.isnumeric():
    print("The given value is not a number")
    quit(1)
if not files.isnumeric() or int(files) > 9998:
    print("The given value is not a number or the given number is greater than 9998")
    quit(1)
if not ballast.isnumeric():
    print("The given value is not a number")
    quit(1)
if not all(c in prefix.hexdigits for c in prefix):
    print("Prefix is incorrect. Please ensure that all characters from prefix string represent hexadecimal digits (0-9, a-f)")
    quit(1)

# Creating folders for DIJ and HTML files
path = ["dijfolder-"+str(prefix), "htmlfolder-"+str(prefix)]

for z in path:
    doesExist = os.path.exists(z)
    if not doesExist:
        os.mkdir(z)


# import HTML code from html_body.txt file and creating HTML files
htmlconfig = configparser.RawConfigParser()
htmlconfig.read('html_body.txt')

# import commenting html code that increases the size of the HTML file
html_ballast = []
for s in range(1, int(ballast)-3):
    html_ballast.append(htmlconfig.get('htmlbody', 'ballast'))
new_ballast = ''.join(html_ballast)


for x in range(1, int(DIJ) + 1):
    ID = f"{prefix}{x:04d}XXXXXXXXXXXXXXXXXX"

    for i in range(1, int(files) + 1):
        html_head = htmlconfig.get('htmlbody', 'html_head')
        link = '''<!-- ''' + str(ID) + f"{i:04d}" ''' -->'''
        html_body = htmlconfig.get('htmlbody', 'html_body')
        filename = f".\\htmlfolder-{prefix}\\file{prefix}{x}_000{i:04d}.html"
        html = html_head + "\n" + link + "\n" + html_body + "\n" + new_ballast

        with open(filename, "w") as file:
            file.write(html)


# import a code from the DIJ.txt file and creating required DIJ files
    filename = f".\\dijfolder-{prefix}\\file{prefix}{x}.DIJ"

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
