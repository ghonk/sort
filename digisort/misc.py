from psychopy import visual, event, core, gui
import os, random, socket, numpy, shutil

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
# copies the data file to a series of dropbox folders
def copy2db(filename,experimentname):
    copyfolders=[ #add your own!
        'C:\\Users\\klab\\Dropbox\\PSYCHOPY DATA\\'+experimentname+'\\',
        'C:\\Users\\klab\\Dropbox\\garrett\\PSYCHOPY DATA\\'+experimentname+'\\']

    for i in copyfolders:
        checkdirectory(i)
        shutil.copy(filename,i)

#------------------------------------------------------------------------------------        
# do a dialog and return subject info 
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
        cardoutline = visual.Rect(win, width=380, height=250)
        cardoutline.setFillColor([1.0,1.0,1.0])
        cardoutline.setLineColor([-1,-1,-1])
        cardtext=visual.TextStim(win, text=i[1], height=14, font='Segoe UI',
            color=[-1,-1,-1], pos=[0,0], wrapWidth=375, name=targetcards.index(i)) 
        cardlabel = i[0]
        cardinfo = [cardoutline, cardtext, cardlabel]
        cardstims.append(cardinfo)
    return cardstims

#------------------------------------------------------------------------------------
# update widgets
def updatewidgets(widgets):
    for i in widgets:
        if isinstance(i, (list, tuple)):
            for j in i:
                j.update()
        else:
            i.update()

#------------------------------------------------------------------------------------
# forget widgets
def forgetwidgets(widgets):
    originalposition=[]
    for i in widgets:
        if isinstance(i, (list, tuple)):
            w=[] 
            for j in i:
                w.append(j.place_info())
                j.place_forget()
            originalposition.append(w)
        else:
            originalposition.append(i.place_info())
            i.place_forget()
    return originalposition
 
#------------------------------------------------------------------------------------
# remember widgets
def rememberwidgets(widgets,info):
    for i in widgets:
        n=widgets.index(i)
        if isinstance(i, (list, tuple)):
            for j in i:
                m=i.index(j)
                j.place(**info[n][m])
        else:
             
            i.place(**info[n])
