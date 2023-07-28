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

path = ["dijfolder", "htmlfolder"]

for z in path:
    doesExist = os.path.exists(z)
    if not doesExist:
        os.mkdir(z)

config = configparser.ConfigParser()
config.read('config.txt')

DIJ = config.get('numbers', 'DIJ')
files = config.get('numbers', 'files')
prefix = config.get('prefix', 'prefix')



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


hval = '0x' + prefix
convert_hval = literal_eval(hval)+1
hex_convert_hval = hex(convert_hval)
to_file = hex_convert_hval.replace('0x', '')
a = to_file


config.set('prefix', 'prefix', a)
with open('config.txt', 'w') as configfile:
    config.write(configfile)
