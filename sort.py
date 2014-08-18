print '\n --------RUNNING SORT TASK ---------'

categorynames=['Shared Solutions', 'Different Solutions']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# specify position of each image
positions = [[-50, 50], [-40, 40], [-30, 30], [-20, 20], [-10, 10], [0, 0]]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# ----------LOAD STIMULI ------------
# load target sort cards into list 'cards'
if condition==1:
    targetcards = alignedcardset
elif condition==2:
    targetcards = unrelatedcardset

cards = makecards(targetcards,win)
shuffle(cards)
print '\n -------Stimulus List --------'
for i in cards:
    print i
print '\n Starting Sort Locations:'
for i in positions:
    print i

# set position of each image
for i in cards:
    i[0].setPos(positions[cards.index(i)])
    i[1].setPos(positions[cards.index(i)])

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#create two image bins
bins=[]
binlabel=[]

bins.append(visual.Rect(win, width=400, height=760))
bins.append(visual.Rect(win, width=400, height=760))

for i in bins:
    binID=bins.index(i)
    
    #set position
    i.setPos([(-wsize[0]/2)+(i.width/1.9),0])
    if binID==1:
        i.setPos([(wsize[0]/2)-(i.width/1.9),0])
    
    # set fill and border    
    i.setFillColor([0.5,0.5,0.5])
    i.setLineColor(tcolor)
    
    #create a text label
    binlabel.append(visual.TextStim(win,
        text=categorynames[binID],height=tsize,font=tfont,
        color=tcolor,pos=i.pos))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   RUNNING THE SORT TASK
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# handle instructions
for i in bins:
    i.draw(win)
for i in binlabel:
    i.draw(win)
instructions.draw(win)
win.flip()
core.wait(2)
if 'q' in event.waitKeys(keyList=['space','q']):
    core.quit()

## reset instructions
instructions.setText('Use the mouse to move examples. Press the return key when you are finished.')
instructions.setPos([0,(wsize[1]/2)-tsize])

#set auto draw for cards and bins
for i in bins:
    i.draw(win)
for i in binlabel:
    i.draw(win)
for i in cards:
    i[0].draw(win)
    i[1].draw(win)
instructions.draw(win)

#present stimuli and reset mouse
win.flip()
cursor.clickReset()

# - - - - - - - - - - - - - - - - - - - - - - - - - -
# -----BEGIN SORTING
timer.reset() #start timer
sortinfo=findobjects(cards,bins)
while ('return' not in event.getKeys(keyList='return')) or (-1 in sortinfo):
    sortinfo=findobjects(cards,bins)
    if 'q' in event.getKeys(keyList='q'):
        core.quit()
    if cursor.isPressedIn(win)        
        for i in list(cards[::-1]):
            #what about creating a wait event that stops the movement through the for loop
            if cursor.isPressedIn(i[0]):

                #sort image list so selection is on top
                cards.pop(cards.index(i))
                cards.insert(len(cards),i)
                
                #adjust mouse click to center on card
                centerpos = i[0].pos - cursor.getPos() 
                
                #relocate selection
                while True in cursor.getPressed():
                    i[0].setPos(cursor.getPos() + centerpos)
                    i[1].setPos(cursor.getPos() + centerpos)
                    
                    # draw objects in depth order
                    instructions.draw(win)
                    for j in bins:
                        j.draw()
                    for j in binlabel:
                        j.draw()
                    for j in cards:
                        j[0].draw()
                        j[1].draw()
                    win.flip()
                    
# - - - - - - - - - - - - - - - - - - - - - - - - - -
# -----ANALYZE AND STORE DATA            
totaltime=timer.getTime()#get sort time

#re-sort the image list
sortedcards=list(cards)
for i in cards:
    sortedcards[int(i[1].name)]=i
cards=sortedcards

## determine which bin each image is in
sortinfo=findobjects(cards,bins)
    
print '\n ---- SORT TASK INFORMATION: ----'
print ['Sort Time:',totaltime]
data.append(['Sort Time:',totaltime])

print '\n FINAL IMAGE LOCATIONS:'
for i in cards:
    imageid=int(i[1].name)

    # get file name
    cardname=i[2]

    # determine XY coordinates
    startposition=positions[imageid]
    finalposition=i[1].pos.tolist()
    
    # determine string category name
    category=sortinfo[imageid]
    if category!=-1:
        category=categorynames[category]
    else:
        category='NA'
        
    print [cardname + ': ', finalposition, category]
    # # # SHOULD CHANGE 'SORT' TO CONDITION SPECIFIC LABEL
    data.append(['sort',cardname,startposition,finalposition,category])

writefile(subjectfile,data,',')

print '\n----final data listing -------'
for i in data:
    print i
