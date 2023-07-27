###################################################################################
#                                                                                 #
#           This is HTML and DIJ files generator.                                 #
#                                                                                 #
#           This script was created by Dawid Kolodziej for Tech Support use only  #
#                                                                                 #
###################################################################################
import os
import configparser

path = ["dijfolder", "htmlfolder"]

for z in path:
    doesExist = os.path.exists(z)
    if not doesExist:
        os.mkdir(z)
config = configparser.ConfigParser()
config.read('test.txt')


DIJ = config.get('numbers', 'DIJ')
files = config.get('numbers', 'files')
prefix = config.get('numbers', 'prefix')


for x in range(1,int(DIJ)+1):
    ID = f"{prefix}{x:04d}XXXXXXXXXXXXXXXXXX"
    for i in range(1,int(files)+1):
        filename = f".\\htmlfolder\\file{x}_000{i:04d}.html"
        print(filename)
        with open(filename, "w") as file:
            file.write('''"<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- EngageOne Generate Build=6.6.11.4072 Date=23-05-2023 Time=15:00:29 Platform=LINUX -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<!-- '''+str(ID) + f"{i:04d}" ''' -->
<title>dummy html</title>
<style type="text/css">a:link {color:#FFFFFF} a:visited {color:#FFFFFF} a:active {color:#FFFFFF}
.ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td {line-height: 100%}
.ExternalClass {width: 100%;}
</style>
</head>
<body bgcolor="#FFFFFF"
style="background-color:#FFFFFF; margin-top:0; margin-left:0; margin-bottom:0; margin-right:0; padding-top:0; padding-left:0; padding-bottom:0; padding-right:0;">
<table align="center" cellspacing="0" cellpadding="0" width="794" style="border-collapse:collapse;background-color:#FFFFFF;">
<tr style="vertical-align:top;line-height:38px;font-size:38px"><td width="38" height="38"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td><td width="718" height="38"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td><td width="38" height="38"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td></tr>
<tr style="vertical-align:top;">
<td width="38"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td><td width="718"><div style="line-height:17px;"><span style="color:#000000;font-family:Arial;font-size:15px;">Dear Customer&#44; </span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;text-align:justify;"><span style="color:#000000;font-family:Arial;font-size:15px;">This very important email was sent by EODeliver </span><span style="color:#000000;font-family:Arial;font-size:15px;text-decoration:underline;">Customer's Corner</span><span style="color:#000000;font-family:Arial;font-size:15px;">&#44; to the Section &#8220;Periodic communications&#8221; of each product. </span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;text-align:justify;"><span style="color:#000000;font-family:Arial;font-size:15px;">We invite you to read it and we thank you for choosing our online services&#44;  reminding you of the possibility of requesting a change in the method of sending communications at any time by contacting us at Customer Service&#47;by entering the &#8220;Communications Management Section&#8221;. </span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;"><span style="color:#000000;font-family:Arial;font-size:15px;">Customer Service </span></div>
<div style="line-height:17px;"><span style="color:#000000;font-family:Arial;font-size:15px;">Precisely Software</span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;text-align:justify;"><span style="color:#000000;font-family:Arial;font-size:11px;">This e-mail is sent automatically and replies cannot be read. For each information request, do not use the &#34;reply&#34;&#44; but contact us through the dedicated form available in the Contact section of the Precisely website.</span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;"><span style="color:#000000;font-family:Arial;font-size:15px;">&nbsp;</span></div>
</td>
<td width="38"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td></tr>
<tr style="vertical-align:top;line-height:65px;font-size:65px"><td width="794" colspan="3" height="65"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td></tr>
</table>
</body>
</html>"''')





    filename = f".\\dijfolder\\file{x}.DIJ"
    print(filename)

    with open(filename, "w") as file:
        file.write('''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE eGAD SYSTEM "eGAD.Dtd">
<eGAD pakUID="8c7b000b9373479dbd57afccba860b00">
<jobdata>
<datetime>20230523030029</datetime>
<platform>EngageOne</platform>
<Version major="4" minor="3"/>
</jobdata>''')
        for i in range(1,int(files)+1):
            file.write('''<document docID="''' +str(i)+ f'''" docInstanceID="'''+ str(ID) + f"{i:04d}" + '''">
<DDSDocValue name="Email" type="text" len="14">user1@test.com</DDSDocValue>
<DDSDocValue name="From" type="text" len="16">NOREPLY@TEST.NET</DDSDocValue>
<DDSDocValue name="Subject" type="text" len="64">Important communication relating to the Precisely product report</DDSDocValue>
<AccNo>PRE;0037057626</AccNo>
<StmtDate>2023-07-25</StmtDate>
<CustData>
</CustData>
<DDSDocValue name="ARCHIVE_INDEX" type="text" len="121">|dummy|68272764|0|20876632|NAME|SURNAME|2023-02-01|ACCXXX97B04F839E|AMBP|23/05/2023|03:00:28 |||user2@test.com|</DDSDocValue>
</document>''')
        file.write('''</eGAD>''')





