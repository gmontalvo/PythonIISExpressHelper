###############################################################################
#
# script for starting IIS process, so that smoke testing can be completed
#
###############################################################################

import os
import signal
import subprocess
import xml.dom.minidom

# set-up some contants
IIS = 'C:\Program Files (x86)\IIS Express\iisexpress.exe'
PID = 'pid.txt'

# look for PID file, which contains the IIS process ID
if os.path.isfile(PID):
    file = open(PID, 'r')
    pid = file.readline()

    # kill the process - should only be running in error conditions
    try:
       os.kill(int(pid), signal.SIGTERM)
    except:
        print('Error killing process')

    # close and delete the file
    file.close()
    os.remove(PID)

# project file is passed to script (argv[1])
if len(argv) > 1:

    # parse the csproj file, which is xml formatted
    docoument = xml.dom.minidom.parse(argv[1])
    element = docoument.getElementsByTagName('DevelopmentServerPort')[0]

    # create array of process arguments
    args = [
        IIS,
       '/systray:false',
       '/path:{0}'.format(os.path.dirname(PROJECT)),
       '/port:{0}'.format(element.firstChild.nodeValue),
    ]

    # spawn the IIS process
    process = subprocess.Popen(args)

    # write the process ID to a file, so we can kill it later
    file = open(PID, 'w')
    file.write(str(process.pid));
    file.close()
