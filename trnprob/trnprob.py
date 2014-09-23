from Tkinter import *
import Tkinter as tk
import sys,random
from socket import gethostname
from psychopy import visual, event, core
from os import getcwd, listdir, path, system
from misc import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# --------- EXPERIMENT SETTINGS ------------
experimentname='transpro'
conditions=[1,2]
numscreens = 3
timer=core.Clock()

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
    print ''
    #win=visual.Window(fullscr=True,units='pix',color=windowcolor,screen=1)
else:
    #win=visual.Window(fullscr=True,units='pix',color=windowcolor)
    checkdirectory(getcwd() + '\\logfiles\\')
    logfile=getcwd()+ '\\logfiles\\' + str(subjectnumber)+ '-logfile.txt'
    while path.exists(logfile):
       logfile=logfile+'_dupe.txt'
    logfile=open(logfile,'w')
    sys.stdout=logfile
    sys.stderr=logfile

#set up data file
data=[['ID', subjectnumber],['condition', condition]]
data.append([])

from instructs import *

if condition == 1:
    transferprob = transferprobs[0] #virus
if condition == 2:
    transferprob = transferprobs[1] #tumor

#------------------------------------------------------------------------------
#end dialogue function
def close_window(event):
    root.quit()

#------------------------------------------------------------------------------
#proceed to final frame
def gotonextframe(event):
    screenadvance()

#------------------------------------------------------------------------------
#retrieve familiarity rating
def retfamrat():
    global familiarityrating
    familiarityrating = var.get()


#------------------------------------------------------------------------------
#remove guide text when entry begins
def eraseTxt(event):
    global clickcount
    if event.x >0 and event.x <=textentryX:
        if event.y>0 and event.y <= textentryY:
            clickcount=clickcount+1;
            if clickcount<3:
                textentry.delete("0.0",END)

#------------------------------------------------------------------------------
#creates display text
def createscrntext(displaytext, xloc, yloc, master):
    global textobj
    temptext = StringVar()
    temptext.set(displaytext)
    textobj = screentext=Label(master,textvariable=temptext,anchor="center",
        font=('Times 18'), wraplength=850)    
    textobjX = textobj.winfo_reqwidth()
    textobjY = textobj.winfo_reqheight()
    textobj.place(x=xloc-(textobjX/2), y=yloc-(textobjY/2))
    
#------------------------------------------------------------------------------        
#advance screen function    
def screenadvance():
    global currentscreen   
    global wrtmorecounter
    # # # #
    # # close program after final screen
    if currentscreen > numscreens:
        root.quit()
    # # # #
    # # transfer problem screen   
    elif currentscreen == 1:
        insobj.place_forget()
        next_button.place(x=(x*.75)-(buttonX/2),y=y*.75)
        transferproblem = transferprob[1]
        textentry.place(x=xcent-(textentryX/2),y=ycent-5)
        textentry.insert(END,"Enter answer here")
        createscrntext(transferproblem,xcent, ycent-200, root)
        timer.reset() #start timer
        currentscreen += 1
    # # # #
    # # familiarity survey screen
    elif currentscreen == 2:
        global partresponse
        global familiarityrating
        partresponse = textentry.get("0.0",END)
        textobj.place_forget()
        textentry.place_forget()
        createscrntext(famsurveytext,xcent, ycent-200, root)
        # # deploy radio buttons
        for i in range(0,len(radbuttlist)):
            radbuttlist[i].place(x=xcent - (bX/2), y=ycent + (i * 30))
        currentscreen += 1
        famliarityrating = var.get()
    # # # # 
    # # termination screen
    elif currentscreen == 3:
        global totaltime
        totaltime=timer.getTime()#get sort time
        next_button.place_forget()
        textobj.place_forget()
        for i in range(0,len(radbuttlist)):
            radbuttlist[i].place_forget()
        createscrntext(goodbyetext,xcent, ycent-200, root)
        currentscreen += 1
        root.bind("<Key>",gotonextframe)
            

#------------------------------------------------------------------------------
# # Set up display objects
# # # #

# # # #
#create tk window
root = tk.Tk()
currentscreen = 1
x, y = root.winfo_screenwidth(), root.winfo_screenheight()
xcent, ycent = x/2, y/2
root.attributes('-fullscreen', True)
root.geometry("%dx%d+0+0" % (x, y))
root.bind("<F12>", close_window)
root.bind("<Button-1>",eraseTxt)
familiarityrating = 0
clickcount = 0

# # # #
#create box for response entry
textentry=Text(root,height=10,width=60,wrap=WORD)  
textentryX = textentry.winfo_reqwidth()
textentryY = textentry.winfo_reqheight()

# # # #
#Screen advance button
next_button = Button(root,text="Next",width=10,
    height=3,font='Times 18',
    command=screenadvance)
buttonX = next_button.winfo_reqwidth()
buttonY = next_button.winfo_reqheight()
next_button.place(x=xcent-(buttonX/2),y=y*.75)

# # # # 
#Create instructions for first screen
initinstructs = (
"In this study, you will be given a question and asked to provide an answer." 
"  Please use the keyboard to type a thoughtful and thorough response to the"
" question.")
instext = StringVar()
instext.set(initinstructs)
insobj = screentext=Label(root,textvariable=instext,anchor="center",
    font='Times 18', wraplength=850)    
insobjX = insobj.winfo_reqwidth()
insobjY = insobj.winfo_reqheight()
insobj.place(x=xcent-(insobjX/2), y=ycent-(insobjY/2))

# # # #
#Create familiarity survey objects
famsurveytext = (
"We would like to know your level of prior familiarity"
" with the problem that you just solved. Please select"
" the option below that fits best:")
famoptions = [
("Not Familiar (I have not seen this problem before)", "1"),
("Possibly Familiar (I might have seen this problem before", "2"),
("Familiar (I already knew the problem, but could not remember the solution)", "3"),
("Highly Familiar (I already knew the problem and its solution)", "4")]
var = StringVar()
var.set(famoptions[0][0])
radbuttlist = []
bX = 0
for i in range(0,len(famoptions)):
    b = Radiobutton(root, text=famoptions[i][0],variable=var, 
        value=famoptions[i][1],font='Times 18',command=retfamrat)
    if b.winfo_reqwidth() > bX:
        bX = b.winfo_reqwidth()
    radbuttlist.append(b)

# # # #
#Create exit screen vars
goodbyetext = (
"Thank you very much for participating in our study "
"today! Please let the experimenter know that you "
"have finished this experiment.")

#------------------------------------------------------------------------------
# # Run program
# # # #
root.mainloop()

#------------------------------------------------------------------------------
# # Save Data
# # # #

print '\n ---- TASK INFORMATION: ----'
taskdata = (
['task time: ',totaltime],
['transfer problem: ', transferprob[0]],
['transfer response: ', partresponse],
['familiarity: ',familiarityrating])

for thing in taskdata:
    for titleordata in thing:
        print titleordata
        data.append([titleordata])

writefile(subjectfile,data,',')



#------------------------------------------------------------------------------
# # terminate exp
print '\nExperiment completed'
if gethostname() in ['klab1','klab2','klab3']:
    logfile.close()
    os.system("TASKKILL /F /IM pythonw.exe")
