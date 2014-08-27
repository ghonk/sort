"""

sortAlign

TODOS - COMPARE Conditions
      - PRINCIPLE QUERY

Conditions
1 - DisgAttack vs Unrelated
2 - DisgAttack vs DisgProtect
3 - Converge   vs Unrelated
4 - Converge   vs Converge Serially 
"""

from psychopy import visual, event, core
from random import shuffle
from socket import gethostname
import sys
from os import getcwd, listdir, path, system
from misc import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# --------- EXPERIMENT SETTINGS ------------
# text properites
experimentname='sortAlign'
conditions=[1,2,3,4]
windowcolor=[0,0,0]
tcolor=[-1,-1,-1]
tfont='Microsoft Sans Serif Regular'
tsize=22

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ----------SET UP INTERFACE------------
## load files
if sys.platform=='darwin':
    checkdirectory(getcwd() + '/subjects/')

    # get subject information
    [subjectnumber,condition,subjectfile]= getsubjectinfo(
        experimentname,conditions,getcwd() + '/subjects/')
else:
    checkdirectory(getcwd() + '\\subjects\\')

    # get subject information
    [subjectnumber,condition,subjectfile]= getsubjectinfo(
        experimentname,conditions,getcwd() + '\\subjects\\')

    
#create window and set logging option
if gethostname() not in ['klab1','klab2','klab3']:
    win=visual.Window(fullscr=True,units='pix',color=windowcolor,screen=1)
else:
    win=visual.Window(fullscr=True,units='pix',color=windowcolor)
    checkdirectory(getcwd() + '\\logfiles\\')
    logfile=getcwd()+ '\\logfiles\\' + str(subjectnumber)+ '-logfile.txt'
    while path.exists(logfile):
       logfile=logfile+'_dupe.txt'
    logfile=open(logfile,'w')
    sys.stdout=logfile
    sys.stderr=logfile

## what screen to use

wsize=win.size

#seed data file
data=[['ID', subjectnumber],['condition', condition]]
data.append([])

print '\n SUBJECT INFORMATION:'
print ['ID: ', subjectnumber]
print ['condition: ', condition]
print ['Data file: ', subjectfile]

# create instruction stimulus
from instructs import *
instructions=visual.TextStim(win,text='press the spacebar to continue',
    height=tsize,font=tfont,color=tcolor,pos=[0,100],wrapWidth=2000)

#define the mouse and timer
cursor = event.Mouse(visible=True, newPos=None, win=win)
timer=core.Clock()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ----------RUN TASK PHASES------------

instructions.setText(sortinstructions1)
instructions.setPos([0,0])
execfile('sort.py')


instructions.setText(exittext)
instructions.setPos([0,0])
instructions.draw(win)
win.flip()
event.waitKeys()

print '\nExperiment completed'
if gethostname() in ['klab1','klab2','klab3']:
	logfile.close()
	os.system("TASKKILL /F /IM pythonw.exe")

	
	

