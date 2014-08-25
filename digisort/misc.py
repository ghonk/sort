from psychopy import visual, event, core, gui
import os, random, socket, numpy

#------------------------------------------------------------------------------------
# creates folder if it doesnt exist
def checkdirectory(dir): 
    if not os.path.exists(dir):
        os.makedirs(dir)

#------------------------------------------------------------------------------------    
# writes list to file
def writefile(filename,data,delim):
    datafile=open(filename,'w')
    for line in data: #iterate over litems in data list
        currentline='\n' #start each line with a newline
        for j in line: #add each item onto the current line

            if isinstance(j, (list, tuple)): #check if item is a list
                for k in j:
                    currentline=currentline+str(k)+delim
            else:
                currentline=currentline+str(j)+delim
                
##        write current line
        datafile.write(currentline)
    datafile.close()  

#------------------------------------------------------------------------------------        
# do a dialouge and return subject info 
def getsubjectinfo(experimentname,conditions,datalocation):
    ss_info=[]
    pc=socket.gethostname()
    myDlg = gui.Dlg(title=experimentname)
    myDlg.addText('Subject Info')
    myDlg.addField('ID:', tip='or subject code')
    myDlg.addField('Condition:', random.choice(conditions),choices=conditions)
    myDlg.show()
    if not myDlg.OK:
        core.quit()
        
    subjectinfo = [str(i) for i in myDlg.data]
    
    if subjectinfo[0]=='':
        core.quit()
    else: 
        id=subjectinfo[0]
        condition=subjectinfo[1]
        subjectfile=datalocation+pc+'-'+experimentname+'-'+condition+'-'+id+'.csv'
        while os.path.exists(subjectfile) == True:
            subject_file=datalocation+pc+'-'+experimentname+'-'+condition+'-'+id+'.csv' + '_dupe'
        return [int(id),int(condition),subjectfile]
            
#------------------------------------------------------------------------------------
# determines which bin each object is in
def findobjects(stim,bins): 
    sort=[]
    for i in stim:
        sort.append(-1) #default
        for j in bins:
            if i[0].overlaps(j):
                sort[stim.index(i)]=bins.index(j)
    return sort
    
#------------------------------------------------------------------------------------
# creates cards for sort task      
def makecards(targetcards,win):
    cardstims = []    
    for i in targetcards:
        cardoutline = visual.Rect(win, width=380, height=225)
        cardoutline.setFillColor([1.0,1.0,1.0])
        cardoutline.setLineColor([-1,-1,-1])
        cardtext=visual.TextStim(win, text=i[1], height=16, font='Microsoft Sans Serif Regular',
            color=[-1,-1,-1], pos=[0,0], wrapWidth=375, name=targetcards.index(i)) 
        cardlabel = i[0]
        cardinfo = [cardoutline, cardtext, cardlabel]
        cardstims.append(cardinfo)
    return cardstims
