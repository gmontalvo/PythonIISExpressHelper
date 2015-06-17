import os
import signal
import subprocess
import xml.dom.minidom

PROJECT = 'C:\\Users\gmontalv\Documents\GitHub\RegistrationDemo\RegistrationDemo\RegistrationDemo.csproj'
IIS = 'C:\Program Files (x86)\IIS Express\iisexpress.exe'
PID = 'pid.txt'

if os.path.isfile(PID):
    file = open(PID, 'r')
    pid = file.readline()

    try:
       os.kill(int(pid), signal.SIGTERM)
    except:
        print('Error killing process')

    file.close()
    os.remove(PID)

docoument = xml.dom.minidom.parse(PROJECT)
element = docoument.getElementsByTagName('DevelopmentServerPort')[0]

args = [
    IIS,
   '/systray:false',
   '/path:{0}'.format(os.path.dirname(PROJECT)),
   '/port:{0}'.format(element.firstChild.nodeValue),
]

process = subprocess.Popen(args)

file = open(PID, 'w')
file.write(str(process.pid));
file.close()
