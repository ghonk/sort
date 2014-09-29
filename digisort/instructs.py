# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # Instructs Doc

nonalignedinstructions = (
"You are about to read six passages that each demonstrate a different "
" problem situation.  Some of these passages are problems that can"
" be solved using the same general principle or solution strategy.\n\n"
"Your job is to pick out the problem situations that can be solved"
" using the same general principle and put them in the bin on the "
"left.  Please consider the passages carefully to make sure you are"
" satisfied with your sort.\n\nYou will use the mouse to click and "
"drag the passages.  When you have sorted all of the examples into the"
" bins you can end the task by pressing the enter key.\n\nPress the "
"spacebar to continue.")


alignedinstructions = (
"You are about to read six passages that each demonstrate a different"
" problem situation.  These passages can be split into two equal"
" groups where all passages in a group can be solved with "
"the same general principle or solution strategy.\n\nYour job is to "
"group the passages that are solvable using the same general "
"principle in the provided bins.  Please consider the passages "
"carefully to make sure you are satisfied with your sort.\n\nYou"
" will use the mouse to click and drag the passages.  When you have"
" sorted all of the examples into the bins you can end the task by "
"pressing the enter key.\n\nPress the spacebar to continue.")


sortinstructions2alg = (
"Use the mouse to click and drag 3 passages to each bin.  All "
"passages in a bin must share a solution.  Feel free to spread the"
" passages out as you wish while you are working.\n\nYou can press "
"the enter key when you are finished.")

sortinstructions2unr = (
"Use the mouse to click and drag 3 passages to each bin."
"  Feel free to spread the passages out as you wish while you are "
"working.\n\nYou can press the enter key when you are finished.")




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # Problem Statements
baseprobcardset = [
[['Mayans',
"An ancient Mayan practice after a victorious battle was to gather the weapons and clothes of their fallen foes.  The Mayans intended to conquer the enemy's villages after the battle to seize the land for their own.  If the villagers were able to recognize Mayan warriors approaching, they could flee and strike back at a later time.  How did the Mayans prevent this?"],
['Plants',
"Carnivorous plants eat insects.  Insects do not naturally approach these plants; instead the insects are drawn to the scent of rotting animal flesh.  Some carnivorous plants have the ability to emit chemicals into the air that mimic particular smells.  How do the plants get their food?"],
['Queen',
"The Queen knew to be careful, so she had her food sampled by the royal taster before she would partake.  However, her enemies came to know that the queen had an insatiable appetite for a rare type of nut.  These enemies also learned that the royal baker was sympathetic to their cause.  What might the conspirators do to assassinate the queen?"]],
# # # # convergence cards
[['DDOS',
"Internet attacks are a serious problem for online websites.  Such attacks can occur when one or more individuals are dissatisfied with a group or organization that has a presence online.  Attackers often try to knock their target's website out of service by overwhelming it with too much information.  Most major websites are now equipped to block communications from any one computer that sends an unreasonable amount of information.  However, attacks of this kind can still be launched using a new strategy.  What strategy do the attackers use?"],
['Commander',
"A tank corps commander and his forces remained loyal to the civilian government after it had lost power.  The key to the commander's plan to restore the government was to capture the military headquarters: a compound situated in the middle of a lake and reachable only by way of pontoon bridges to the north, south, east, and west.   The bridges were so unstable that only one tank could cross at a time without causing a collapse.  The commander knew he needed as many tanks as possible to arrive at the same time in order to successfully take the headquarters.  What plan can the commander follow to successfully capture the compound?"],
['Oil Well',
"An oil well exploded and caught fire.  The result was a blazing inferno that resisted all efforts to control.  Elite firefighters were dispatched.  They knew the only hope was to spray a huge amount of fire retardant foam against the fire in one knockout punch.  When they arrived they saw the flaw in their plan:  they had plenty of hoses, but none were wide enough to deliver the amount of foam that would be required.  How can the firefighters change their plan to extinguish the blaze?"]
]]

# # # # contrast cards
contprobcardset = [
# # # # unrelated
[['Store',
"Two women who run a beachside gift shop make almost all of their money during the summer season.  Business during the summer months is fast-paced and exciting so it's always a surprise when the weather cools and business slows.  Unfortunately, the women have expenses all year long that require having funds on hand. This forces them to seek an alternative source of income when business slows.  What do they do to make sure they have enough money throughout the year despite only bringing in income during the summertime?"],
['Flight',
"All birds have the ability to fly, with the exception of a few species like ostriches and penguins.  Flight allows birds to migrate long distances, nest in places that ground dwellers cannot reach and protect themselves from predators.  In order to fly, the body of a bird must be relatively lightweight.  Bones are the heaviest part of an organism, and ordinary bones would make flight incredibly difficult.  How can birds have bones and still be able to fly?"],
['Phones',
"Cellular telephone calls require a set of conditions to be met in order to transmit a person's voice from one phone to another.  One of the biggest reasons that calls fail is because the phone falls out of range from a cell tower.  This happens when the signal is blocked.  Signals are often blocked by mountains or large buildings.  It is also very difficult to transmit signals to users in underground locations like subway stations.  How might cellphone providers decrease the frequency of dropped calls?"]
],
# # # # virus aligned contrasts
[['Viceroy',
"The viceroy butterfly is a nontoxic creature that has no natural defenses.  Monarch butterflies have deadly toxins and distinctive patterns that mark the toxicity and scare predators from eating them.  If the viceroy cannot evolve toxins, how does it make predators fear it like the monarch butterfly?"],
['Artillery',
"During the war a large contingent of soldiers were stranded in an area vulnerable to an attack from the sky.  They had no defenses to protect themselves from air attack.  The soldiers did have several broken anti-aircraft weapons that would appear to be functional from the cockpit of a plane.  What can the soldiers do to minimize the possibility of being attacked from the air?"],
['Birds',
"Certain rare species of birds have the ability to mimic the sounds of the predators that live in their environment.  These birds have no natural defenses to counter the attacks of predators.  What can the birds do to protect themselves when predators are nearby?"]
],
# # # # convergence aligned contrasts
[['Waitstaff',
"A town in the western U.S. has an annual festival that draws many thousands of people who patronize the local restaurants and businesses.  This can easily overwhelm the restaurants since they are not accustomed to being completely packed and having lines out the door.  The restaurants need more employees, but they cannot afford the cost of having these additional employees during times of year when they are not needed.  What can the restaurant owners do to address this problem?"],
['Bank',
"A bank must keep a certain amount of money on hand for customers who come in to make withdrawals.  The bank prefers to minimize their cash on hand in order to maximize investment of deposited money and reduce the risk of robbery.  However, if customers request more money than the bank has available, it could be a disaster.  The bank manager noticed that customers tend to withdraw more cash on Fridays (weekend spending money) and became justifiably nervous about running low.   What can the bank do to make certain that there will always be enough cash available?"],
['PubTrans',
"Regions with large populations are faced with complex and critical transportation issues.  Providing reliable public transportation is necessary because traffic conditions would become a nightmare if everyone chose to get around by car.  If there are not enough trains and buses in service during peak usage, the long waits and restricted routes cause people to give up on public transportation.  However, city and county governments face budget shortfalls and must save money wherever they can.  Considering these constraints, how do public transportation agencies handle this problem?"]
]]
# # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # Solution Statements

basesolcardset = [
[['Mayans',
"An ancient Mayan practice after a victorious battle was to gather the weapons and clothes of their fallen foes.  The Mayans intended to conquer the enemy's villages after the battle to seize the land for their own.  If the villagers were able to recognize Mayan warriors approaching, they could flee and strike back at a later time. To avoid this the Mayans dressed in the clothing of the deceased and invaded enemy territory to guarantee complete victory."],
['Plants',
"Carnivorous plants eat insects.  Insects do not naturally approach these plants; instead the insects are drawn to the scent of rotting animal flesh.  Some carnivorous plants have the ability to emit chemicals into the air that mimic particular smells.   Maggots are drawn towards the stench of their regular feeding ground - a dead corpse - and are then devoured by the plant."],
['Queen',
"The Queen knew to be careful, so she had her food sampled by the royal taster before she would partake.  However, her enemies came to know that the Queen had an insatiable appetite for a rare type of nut.  The enemies influenced Her Majesty's favorite baker to send the Queen a precious chocolate containing the rare nut filling and also a deadly poison.  The Queen joyously popped the treat in her mouth all at once.  The treat would be her last."]],
# # # # contrast cards
[['DDOS',
"Internet attacks are a serious problem for online websites.  Such attacks can occur when one or more individuals are dissatisfied with a group or organization that has a presence online.  Attackers often try to knock their target's website out of service by overwhelming it with too much information.  Most major websites are now equipped to block communications from any one computer that sends an unreasonable amount of information.  However, to overcome this protection, attacks of this kind can still be launched using a new strategy:  the attackers coordinate to send a moderate amount of information from many different computers all at the same time."],
['Commander',
"A tank corps commander and his forces remained loyal to the civilian government after it had lost power.  The key to the commander's plan to restore the government was to capture the military headquarters: a compound situated in the middle of a lake and reachable only by way of pontoon bridges to the north, south, east, and west.   The bridges were so unstable that only one tank could cross at a time without causing a collapse.  The commander knew he needed as many tanks as possible to arrive at the same time in order to successfully take the headquarters.  He solved the problem by dividing his forces so he could position tanks at each bridge and send them in together at his signal."],
['Oil Well',
"An oil well exploded and caught fire.  The result was a blazing inferno that resisted all efforts to control.  Elite firefighters were dispatched.  They knew the only hope was to spray a huge amount of fire retardant foam against the fire in one knockout punch.  When they arrived they saw the flaw in their plan:  they had plenty of hoses, but none were wide enough to deliver the amount of foam that would be required.  To address this, they stationed each firefighter in a circular formation around the well.  By turning on all the hoses together, they could deliver a massive amount of foam at once to extinguish the blaze."]
]]

# # # # contrast cards
contsolcardset = [
# # # # unrelated
[['Store',
"Two women who run a beachside gift shop make almost all of their money during the summer season.  Business during the summer months is fast-paced and exciting so it's always a surprise when the weather cools and business slows.  Unfortunately, the women have expenses all year long that require having funds on hand. This forces them to seek an alternative source of income when business slows.  In order to account for their expenses, the women rent out the store for special events and parties during the months that are too cold for beach-goers."],
['Flght',
"All birds have the ability to fly, with the exception of a few species like ostriches and penguins.  Flight allows birds to migrate long distances, nest in places that ground dwellers cannot reach and protect themselves from predators.  In order to fly, the body of a bird must be relatively lightweight.  Bones are the heaviest part of an organism, and ordinary bones would make flight incredibly difficult. Birds can fly because their bones are much lighter than those of animals that do not fly."],
['Phones',
"Cellular telephone calls require a set of conditions to be met in order to transmit a person's voice from one phone to another.  One of the biggest reasons that calls fail is because the phone falls out of range from a cell tower.  This happens when the signal is blocked.  Signals are often blocked by mountains or large buildings.  It is also very difficult to transmit signals to users in underground locations like subway stations.  Cellphone providers address this problem by building cellphone towers where they are most needed."]
],
# # # # virus aligned
[['Viceroy',
"The viceroy butterfly is a nontoxic creature that has no natural defenses.  Monarch butterflies have deadly toxins and distinctive patterns that mark the toxicity and scare predators from eating them.  Because the patterns on the viceroy are similar to that of the monarch, it's predators believe it to be a Monarch and therefore avoid it."],
['Artillery',
"During the war a large contingent of soldiers were stranded in an area vulnerable to an attack from the sky.  They had no defenses to protect themselves from air attack.  The soldiers did have several broken anti-aircraft weapons that would appear to be functional from the cockpit of a plane.  They decided to set up the broken weaponry to appear as though it was functional.  When a fighter plane passed over the camp, it went into evasive maneuvers and the men below were spared."],
['Birds',
"Certain rare species of birds have the ability to mimic the sounds of the predators that live in their environment.  These birds have no natural defenses to counter the attacks of predators.  When these birds come in contact with a predator, they make this noise and the predator flees the area, mistakenly thinking that a rattlesnake is nearby."]
],
# # # # convergence aligned
[['Waitstaff',
"A town in the western U.S. has an annual festival that draws many thousands of people who patronize the local restaurants and businesses.  This can easily overwhelm the restaurants since they are not accustomed to being completely packed and having lines out the door.  The restaurants need more employees, but they cannot afford the cost of having these additional employees during times of year when they are not needed.  The restaurant owners solve this problem by recruiting wait staff who are willing to work only during the busy season."],
['Banks',
"A bank must keep a certain amount of money on hand for customers who come in to make withdrawals.  The bank prefers to minimize their cash on hand in order to maximize investment of deposited money and reduce the risk of robbery.  However, if customers request more money than the bank has available, it could be a disaster.  The bank manager noticed that customers tend to withdraw more cash on Fridays (weekend spending money) and became justifiably nervous about running low.   In order to make certain that there was always enough cash available, the bank began to keep more cash on hand on Fridays than during the rest of the week."],
['PubTrans',
"Regions with large populations are faced with complex and critical transportation issues.  Providing reliable public transportation is necessary because traffic conditions would become a nightmare if everyone chose to get around by car.  If there are not enough trains and buses in service during peak usage, the long waits and restricted routes cause people to give up on public transportation.  However, city and county governments face budget shortfalls and must save money wherever they can.  The best approach to this problem is to allocate additional trains and buses only during rush hour periods."]
]]
# # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


princtext = (
"Thanks for completing the sort.  Now we are going to ask you some follow up "
"questions about the activity.  Please answer the questions as thoroughly as "
"you can.\n\nPress the enter key to begin.")

exittext = 'Thank you for participating in this experiment.\n\
Please inform your experimenter that you are ready\n\
to move on to the next study.'

