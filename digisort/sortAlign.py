from psychopy    import visual, event, core
from random      import shuffle
from socket      import gethostname
import sys
from os          import getcwd, listdir, path, system
from misc        import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
"""
                 _            _ _             
                | |     /\   | (_)            
  ___  ___  _ __| |_   /  \  | |_  __ _ _ __  
 / __|/ _ \| '__| __| / /\ \ | | |/ _` | '_ \ 
 \__ \ (_) | |  | |_ / ____ \| | | (_| | | | |
 |___/\___/|_|   \__/_/    \_\_|_|\__, |_| |_|
                                   __/ |      
                                  |___/       
    TODOS 
          - aligned instructions sticky
          - need to restrict group sizes in sort
          - capture edits after the OK screen

    Conditions = 
    1 - DisgAttack vs Unrelated
    2 - DisgAttack vs DisgProtect
    3 - Converge   vs Unrelated
    4 - Converge   vs Use More

"""
__author__ = "Garrett and Nolie"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# --------- EXPERIMENT SETTINGS ------------
# text properites
experimentname='sortAlign'
conditions=[1,2,3,4,5,6,7,8]
windowcolor=[.88235,.88235,.88235]
tcolor=[-1,-1,-1]
tfont='Arial'
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
    win=visual.Window([1440,900],units='pix',color=windowcolor,screen=1)
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
print wsize

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
    height=tsize,font=tfont,color=tcolor,pos=[0,100],wrapWidth=575)

#define the mouse and timer
cursor = event.Mouse(visible=True, newPos=None, win=win)
timer=core.Clock()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ----------LOAD STIMULI ------------
# load target sort cards into list 'cards'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # PROBLEM SITUATIONS
# # # DISGUISE
if condition==1:
# Non-Aligned; Disguise; Problems
    targetcards = baseprobcardset[0] + contprobcardset[0]
elif condition==2:
# Aligned; Disguise; Problems
    targetcards = baseprobcardset[0] + contprobcardset[1]
# # # CONVERGENCE
elif condition==3:
# Non-aligned; Convergence; Problems
    targetcards = baseprobcardset[1] + contprobcardset[0]
elif condition==4:
# Aligned; Convergence; Problems
    targetcards = baseprobcardset[1] + contprobcardset[2]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # SOLUTION SITUATIONS
# # # DISGUISE
elif condition==5:
# Non-Aligned; Disguise; Solutions
    targetcards = basesolcardset[0] + contsolcardset[0]
elif condition==6:
# Aligned; Disguise; Solutions
    targetcards = basesolcardset[0] + contsolcardset[1]
# # # CONVERGENCE
elif condition==7:
# Non-aligned; Convergence; Solutions
    targetcards = basesolcardset[1] + contsolcardset[0]
elif condition==8:
# Aligned; Convergence; Solutions
    targetcards = basesolcardset[1] + contsolcardset[2]

if condition%2 == 0:
    categorynames=['share solution one', 'share solution two']
    extradescr=["passages share a solution","passages share a solution"]
    instructions.setText(alignedinstructions)
else:
    categorynames=['shared solutions', 'different solutions']
    extradescr=["passages share a solution",
                "passages do not share solutions"]
    instructions.setText(nonalignedinstructions)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# specify start position of each image
positions = [[-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0]]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ----------RUN TASK PHASES------------
instructions.setPos([0,0])
#execute sort task
execfile('sort.py')
#execute principle query
execfile('getprinciple.py')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ----------GRAB DATA------------

print '\n----final data listing -------'
for i in data:
    print i

writefile(subjectfile,data,',')


print '\nExperiment completed'
if gethostname() in ['klab1','klab2','klab3']:
   logfile.close()
   os.system("TASKKILL /F /IM pythonw.exe")

	
	

