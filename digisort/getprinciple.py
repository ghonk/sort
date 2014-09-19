from Tkinter import *
import Tkinter as tk


print '\n --------RUNNING PRINCIPLE QUERY ---------'

#------------------------------------------------------------------------------
# # Set up tk functions
#------------------------------------------------------------------------------
# # # #
#end dialogue function
def close_window(event):
    root.destroy()

#------------------------------------------------------------------------------
#remove guide text when entry begins
def eraseTxt(event):
    global clickcount
    if event.x >0 and event.x <=textentryX:
        if event.y>0 and event.y <= textentryY:
            clickcount=clickcount+1;
            if clickcount<3:
                textentry.delete("0.0",END)
                clickcount = 4

#------------------------------------------------------------------------------
#proceed to final frame
def endexp(event):
    root.destroy()

#------------------------------------------------------------------------------
# # # #
#screen advance manager
def screenadvance():
	global group1resp
	global group2resp
	global firstview
	if currentscreen == 1:
		firstprinciplescreen()
		group1resp = textentry.get("0.0",END)
	elif currentscreen == 2:
		if condition % 2 == 0:
			if firstview == 1:
				group1resp = textentry.get("0.0",END)
			secondprinciplescreen()
			group2resp = textentry.get("0.0",END)	
		else:
			forgetwidgets([textentry,topobj,topobj2,botobj,botobj2,
			objlst2,objlst,lastobj,next_button])
			finaltext.place(x=xcent-(finaltextX/2), y=400-(finaltextY/2))
			root.bind("<Key>",endexp)
	elif currentscreen == 3:
		if condition % 2 != 0:
			group1resp = textentry.get("0.0",END)
		else:
			group2resp = textentry.get("0.0",END)
		forgetwidgets([textentry,topobj,topobj2,botobj,botobj2,
			objlst2,objlst,lastobj,next_button])
		finaltext.place(x=xcent-(finaltextX/2), y=400-(finaltextY/2))
		root.bind("<Key>",endexp)

#------------------------------------------------------------------------------
# # Set up tk screens
#------------------------------------------------------------------------------
# # # #
#query participant for principle of group 1
def firstprinciplescreen():
	global group1resp
	global currentscreen
	group1resp = textentry.get("0.0",END)
	if len(group1resp) < 60:
		wrtmore.place(x=xcent-(wrtmoreX/2), y=640-(wrtmoreY/2))
		currentscreen = 1
	else:
		originalposition = forgetwidgets([wrtmore])
		lastobj.place(x=xcent-(lastobjX/2), y=640-(lastobjY/2))
		currentscreen += 1
		if condition%2 != 0:
			currentscreen += 1
		
# # # # 
#query participant for principle of group 2
def secondprinciplescreen():
	global group2resp
	global currentscreen
	global firstview
	if firstview == 1:	
		textentry.delete("0.0",END)
		forgetwidgets([lastobj, topobj, botobj, objlst])
		topobj2.place(x=xcent-(topobj2X/2), y=150-(topobj2Y/2))			
		botobj2.place(x=xcent-(botobj2X/2), y=400-(botobj2Y/2))
		objlst2[0].place(x=(xcent+400)-(tempX/2), y=200)
		objlst2[1].place(x=xcent-(tempX/2), y=200)
		objlst2[2].place(x=(xcent-400)-(tempX/2), y=200)
		firstview += 1
	else:
		group2resp = textentry.get("0.0",END)
		if len(group2resp) < 60:
			wrtmore.place(x=xcent-(wrtmoreX/2), y=640-(wrtmoreY/2))
			currentscreen = 2
		else:
			originalposition = forgetwidgets([wrtmore])
			lastobj.place(x=xcent-(lastobjX/2), y=640-(lastobjY/2))
			currentscreen += 1


#------------------------------------------------------------------------------
# # Set up display objects
#------------------------------------------------------------------------------
# # # #
#create tk window
root = tk.Tk()
if gethostname() in ['klab1','klab2','klab3']:
	root.attributes('-fullscreen', True)
	x, y = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry("%dx%d+0+0" % (x, y))
else:
	root.geometry("%dx%d+0+0" % (1440, 900))
	x, y = 1440, 900
xcent, ycent = x/2, y/2
root.call('wm', 'attributes', '.', '-topmost', '1')
root.bind("<F12>", close_window)
root.bind("<Button-1>",eraseTxt)
currentscreen = 1
clickcount=0

#------------------------------------------------------------------------------
# # # #
#Screen advance button
next_button = Button(root,text="Next",width=10,
    height=3,font='Arial 18',command=screenadvance)
buttonX = next_button.winfo_reqwidth()
buttonY = next_button.winfo_reqheight()
next_button.place(x=xcent-(buttonX/2),y=y*.75)

#------------------------------------------------------------------------------
# # # # 
#Create text for first screen
# first bit of instructs
topinstructs = (
"Here are the passages that you put into bin one:")
topobj = screentext=Label(root,text=topinstructs,anchor="center",
    font='Arial 18', wraplength=850)    
topobjX = topobj.winfo_reqwidth()
topobjY = topobj.winfo_reqheight()
topobj.place(x=xcent-(topobjX/2), y=150-(topobjY/2))

# second bit
botinstructs = (
"Please use the space below to explain the principle that was "
"common to each passage that you put in bin one.")
botobj = screentext=Label(root,text=botinstructs,anchor="center",
    font='Arial 18', wraplength=775)    
botobjX = botobj.winfo_reqwidth()
botobjY = botobj.winfo_reqheight()
botobj.place(x=xcent-(botobjX/2), y=400-(botobjY/2))

#instruct to write more
writemoreinstructs = (
"Your response was quite short. Please be as thorough as you can"
" with your response.")
wrtmore = screentext=Label(root, text=writemoreinstructs, anchor="center",
	font='Arial 18', wraplength=800)
wrtmoreX = wrtmore.winfo_reqwidth()
wrtmoreY = wrtmore.winfo_reqheight()

#confirm instructs
lastinstructs = (
"Press next again to confirm you're ready to move on.")
lastobj = screentext=Label(root, text=lastinstructs, anchor="center",
	font='Arial 18', wraplength=850)
lastobjX = lastobj.winfo_reqwidth()
lastobjY = lastobj.winfo_reqheight()

# # # #
#Get cards from group 1 
g1cards = []
for i in cards:
	if i[-1] == 0:
		for j in targetcards:
			if j[0] == i[2]:
				g1cards.append(j[1])
#Place cards
objlst = []
for card in g1cards:
	tempobj=Label(root,text=card,anchor=NE, justify=LEFT,
		font='Arial 10', wraplength=375)
	tempX = tempobj.winfo_reqwidth()
	tempY = tempobj.winfo_reqheight()
	objlst.append(tempobj)
	if g1cards.index(card) == 0:
		objlst[g1cards.index(card)].place(x=(xcent+400)-(tempX/2), y=200)
	elif g1cards.index(card) == 1:
		objlst[g1cards.index(card)].place(x=xcent-(tempX/2), y=200)
	elif g1cards.index(card) == 2:
		objlst[g1cards.index(card)].place(x=(xcent-400)-(tempX/2), y=200)


#------------------------------------------------------------------------------
# # # # 
#Create stuff for second screen
firstview = 1
group2resp = ''
# first bit of instructs
topinstructs2 = (
"Here are the passages that you put into bin two:")
topobj2 = screentext=Label(root,text=topinstructs2,anchor="center",
    font='Arial 18', wraplength=850)    
topobj2X = topobj2.winfo_reqwidth()
topobj2Y = topobj2.winfo_reqheight()


# second bit
botinstructs2 = (
"Please use the space below to explain the principle that was "
"common to each passage that you put in bin two.")
botobj2 = screentext=Label(root,text=botinstructs2,anchor="center",
    font='Arial 18', wraplength=775)    
botobj2X = botobj2.winfo_reqwidth()
botobj2Y = botobj2.winfo_reqheight()


# # # #
#Get cards from group 2
g2cards = []
for i in cards:
	if i[-1] == 1:
		for j in targetcards:
			if j[0] == i[2]:
				g2cards.append(j[1])
#Place cards
objlst2 = []
for card in g2cards:
	tempobj=Label(root,text=card,anchor=NE, justify=LEFT,
		font='Arial 10', wraplength=375)
	tempX = tempobj.winfo_reqwidth()
	tempY = tempobj.winfo_reqheight()
	objlst2.append(tempobj)

#------------------------------------------------------------------------------
# # # #
# final screen
finaltext = screentext=Label(root,text=exittext,anchor="center",
    font='Arial 18', wraplength=775)    
finaltextX = finaltext.winfo_reqwidth()
finaltextY = finaltext.winfo_reqheight()

#------------------------------------------------------------------------------
# # # #
#create box for response entry
textentry=Text(root,height=10,width=60,wrap=WORD)  
textentryX = textentry.winfo_reqwidth()
textentryY = textentry.winfo_reqheight()
textentry.place(x=xcent-(textentryX/2),y=ycent-5)
textentry.insert(END,"Enter answer here")


#------------------------------------------------------------------------------
# # Run principle query
# # # #
root.mainloop()


#save data
taskdata = (
['Group 1 Response: ', group1resp],
['Group 2 Response: ', group2resp])

for thing in taskdata:
	for titleordata in thing:
		data.append([titleordata])


