DIJ = 5 # enter number of DIJ files you would like to process in EODeliver
files = 5 # enter number of file per DIJ file you would like to process in EODeliver



for x in range(1,DIJ+1):
    ID = f"25AKKX{x:04d}XXXXXXXXXXXXXXXXXX"  # Enter some custom string of characters. This will be part of unique docInstanceID number.
    for i in range(1,files+1):
        filename = f"u:\\kopiowanie\\htmlfolder\\file{x}_000{i:04d}.html"
        print(filename)
        with open(filename, "w") as file:
            file.write('''"<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- EngageOne Generate Build=6.6.11.4072 Date=23-05-2023 Time=15:00:29 Platform=LINUX -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<!-- '''+str(ID) + f"{i:04d}" ''' -->
<title>11-na-print</title>
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
<td width="38"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td><td width="718"><div style="line-height:17px;"><span style="color:#000000;font-family:Arial;font-size:15px;">Gentile cliente&#44; </span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;text-align:justify;"><span style="color:#000000;font-family:Arial;font-size:15px;">desideriamo informarti che una comunicazione &#232; disponibile on line nella tua </span><span style="color:#000000;font-family:Arial;font-size:15px;text-decoration:underline;">Area Clienti Agos</span><span style="color:#000000;font-family:Arial;font-size:15px;">&#44; alla Sezione &#8220;Comunicazioni Periodiche&#8221; di ciascun prodotto. </span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;text-align:justify;"><span style="color:#000000;font-family:Arial;font-size:15px;">Ti invitiamo a prenderne visione e ti ringraziamo per aver scelto i nostri servizi on line&#44; ricordandoti la possibilit&#224; di richiedere in qualsiasi momento la modifica della modalit&#224; di invio delle comunicazioni contattandoci al Servizio Clienti&#47;entrando nella Sezione &#8220;Gestione delle Comunicazioni&#8221;. </span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;"><span style="color:#000000;font-family:Arial;font-size:15px;">Servizio Clienti </span></div>
<div style="line-height:17px;"><span style="color:#000000;font-family:Arial;font-size:15px;">Agos Ducato S.p.A.</span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;text-align:justify;"><span style="color:#000000;font-family:Arial;font-size:11px;">---- 1 ---- mail viene inviata automaticamente e le risposte non potranno essere lette. Per ogni richiesta di informazioni non utilizzare il tasto &#34;Rispondi&#34;&#44; ma contattaci attraverso il form dedicato disponibile alla sezione Contatti del sito di Agos Ducato.</span></div>
<div style="font-size:12px;line-height:12px;">&nbsp;</div>
<div style="line-height:17px;"><span style="color:#000000;font-family:Arial;font-size:15px;">&nbsp;</span></div>
</td>
<td width="38"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td></tr>
<tr style="vertical-align:top;line-height:65px;font-size:65px"><td width="794" colspan="3" height="65"><span style="font-size:1px;line-height:1px;">&nbsp;</span></td></tr>
</table>
</body>
</html>"''')





    filename = f"u:\\kopiowanie\\dijfolder\\file{x}.DIJ"
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
        for i in range(1,files+1):
            file.write('''<document docID="''' +str(i)+ f'''" docInstanceID="'''+ str(ID) + f"{i:04d}" + '''">
<DDSDocValue name="Email" type="text" len="22">user1@test.com</DDSDocValue>
<DDSDocValue name="From" type="text" len="22">NOREPLY@AGOSDUCATO.NET</DDSDocValue>
<DDSDocValue name="Subject" type="text" len="80">Comunicazione importante relativa al rapporto di finanziamento Agos n. 068272764</DDSDocValue>
<AccNo>AMB;0037057626</AccNo>
<StmtDate>2023-05-23</StmtDate>
<CustData>
</CustData>
<DDSDocValue name="ARCHIVE_INDEX" type="text" len="121">|dummy|68272764|0|20876632|NAME|SURNAME|2023-02-01|ATTXXX97B04F839E|AMBP|23/05/2023|03:00:28 |||user2@test.com|</DDSDocValue>
</document>''')
        file.write('''</eGAD>''')





