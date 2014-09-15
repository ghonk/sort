print '\n --------RUNNING SORT TASK ---------'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# make cards
cards = makecards(targetcards,win)
shuffle(cards)

print '\n -------Stimulus List --------'
# set position of each image
for i in cards:
    print i
    i[0].setPos(positions[cards.index(i)])
    i[1].setPos(positions[cards.index(i)])
    i.append([positions[cards.index(i)]])
    print ["starting position: ",positions[cards.index(i)]]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#create two image bins
bins=[]
binlabel=[]
otrlabel=[]
otrdescr=[]
extralabel=["BIN ONE", "BIN TWO"]

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
    binlabelpos = i.pos + [0, -395]
    binlabel.append(visual.TextStim(win,text=extradescr[binID],
        height=tsize,font=tfont,color=tcolor,pos=binlabelpos))
    
    #create extra text label
    otrlabelpos = i.pos + [0, 395]
    otrlabel.append(visual.TextStim(win,text=extralabel[binID],
        height=tsize,font=tfont,color=tcolor,pos=otrlabelpos))

    #create extra description label
    otrdescrpos = i.pos + [0, 365]
    otrdescr.append(visual.TextStim(win,text=extradescr[binID],
        height=tsize,font=tfont,color=tcolor,pos=otrdescrpos))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   RUNNING THE SORT TASK
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#print interface
for i in bins:
    i.draw(win)
for i in binlabel:
    i.draw(win)
for i in otrlabel:
    i.draw(win)
for i in otrdescr:
    i.draw(win)

# handle instructions    
instructions.draw(win)
win.flip()
core.wait(2)
if 'q' in event.waitKeys(keyList=['space','q']):
    core.quit()

## reset instructions
instructions.setText(sortinstructions2)
instructions.setPos([0,(wsize[1]/2)-200])

#set auto draw for cards and bins
for i in bins:
    i.draw(win)
for i in binlabel:
    i.draw(win)
for i in otrlabel:
    i.draw(win)
for i in otrdescr:
    i.draw(win)
for i in cards:
    i[0].draw(win)
    i[1].draw(win)
instructions.draw(win)

#present stimuli and reset mouse
win.flip()
cursor.clickReset()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# -----BEGIN SORTING
timer.reset() #start timer
sortinfo=findobjects(cards,bins)
while ('return' not in event.getKeys(keyList='return')) or (-1 in sortinfo):
    sortinfo=findobjects(cards,bins)
    if 'q' in event.getKeys(keyList='q'):
        core.quit()     
        
    while True in cursor.getPressed():    
        for i in list(cards[::-1]):
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
                    for j in otrlabel:
                        j.draw()
                    for j in otrdescr:
                        j.draw()
                    for j in cards:
                        j[0].draw()
                        j[1].draw()
                    win.flip()
                
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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
    startposition=i[-1]
    finalposition=i[1].pos.tolist()
    
    # determine string category name
    category=sortinfo[imageid]
    i.append(category)
    if category!=-1:
        category=categorynames[category]
    else:
        category='NA'
    
    # # # SHOULD CHANGE 'SORT' TO CONDITION SPECIFIC LABEL
    print [cardname + ': ', finalposition, category]
    data.append([condition,cardname,startposition,finalposition,category])

instructions.setText(princtext)
instructions.setPos([0,0])
instructions.draw(win)
win.flip()
event.waitKeys()

win.flip()

print '\n----final data listing -------'
for i in data:
    print i
