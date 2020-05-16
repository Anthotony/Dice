#sets values to add to later
dicelist = []
dienumlist = []
numdicelist = []
roll_list = []
dieroll = 0
die = 0
twotypewhile = 'y'
modtotal = 0
total = 0
indexx = 0
indexy = 0
import random
index_x = 0
numdice = 0

#asks if multiple types of dice are wanted
twotype = input('Do you want more than one type of die? y/n\n')
while twotype.lower() not in ['n', 'no', 'yes', 'y']:
    twotype = input('Please reinput yes or no\n')
if twotype.lower() in ['y', 'yes']:
    while twotypewhile.lower() in ['y', 'yes']:
        dienumadd = input('How many sides?\n')
        while int(dienumadd) < 2:
            dienumadd = input('Please reinput the number of sides.\n')
        dienumlist.append(int(dienumadd))
        numdiceadd = input('How many times do you want to roll the D' + str(dienumadd) + '?\n')
        while int(numdiceadd) < 1:
            numdiceadd = input('Please reinput the number of sides.\n')
        numdicelist.append(int(numdiceadd))
        twotypewhile = input('Do you want more types of dice? y/n\n')
        while twotypewhile.lower() not in ['n', 'no', 'yes', 'y']:
            twotypewhile = input('Please reinput yes or no\n')
elif twotype.lower() in ['n', 'no']:
    numdice = input('How many dice would you like to roll?\n')
    numdice = int(numdice)
    while numdice < 1:
        numdice = input('Please reinput the number of dice\n')
        numdice = int(numdice)
    dienum = input('How many sides do you want on this die?\n')
    dienum = int(dienum)
    while dienum < 2:
        dienum = input('Please reinput the number of dice\n')
        dienum = int(dienum)

#if you only added 1 set to where it holds multiple this converts it to single
if len(dienumlist) == 1:
    dienum = dienumlist[0]
    numdice = numdicelist[0]
    dienum = int(dienum)
    numdice = int(numdice)

#if they specify they are creating characters, this code is run to produce 6 stats
if numdice == 4 and dienum == 6:
    cc = input('Are you making a character? y/n\n')
    while cc not in ['n', 'no', 'yes', 'y']:
        cc = input('Are you making a character? y/n\n')
    if cc.lower() in ['yes', 'y']:
        stat = 6
        while stat >= 1:
            y = 4
            while y >= 1:
                x = random.randint(1, dienum)
                dicelist.append(x)
                y -= 1
            dicelist.sort()
            dicelist.pop(0)
            total = 0
            for roll in dicelist:
                    x = roll
                    total = total + x
            print(dicelist, total)
            dicelist = []
            stat -= 1
        exit()

#if there is no character, a bonus may apply, that goes here
if len(dienumlist) > 1:
    for num in dienumlist:
        mod = input("Mod for D" + str(num) + '\n')
        modtotal += int(mod)
else:
    mod = input('Modifiers/Damage Bonus\n')

#rolls for multiple types of dice
if len(dienumlist) > 1:
    for rollamount in numdicelist:
        while rollamount >= 1:
            roll = random.randint(1, dienumlist[die])
            roll_list.append(roll)
            rollamount -= 1
        die += 1

#rolls multiple dice and places them in a list
while numdice > 1 and len(dicelist) != numdice:
    roll = random.randint(1, dienum)
    dicelist.append(roll)

#rolls for only 1 die
if numdice == 1:
    dieroll += random.randint(1, dienum)

#totals list of dice
for roll in dicelist:
    total = total + int(roll)
for roll in roll_list:
    total = total + int(roll)

#names and tells you which dice is rolling
if len(dienumlist) > 1:
    while indexx < len(numdicelist):
        numdice = numdicelist[indexy]
        dienum = dienumlist[indexy]
        print("Rolling" + str(numdice) + "D" + str(dienum) + "...")
        indexx += 1
        indexy += 1
else:
    print("Rolling D" + str(dienum) + '...')

#pause for 1 second for style
import time
time.sleep(0.5)

#adds mod
rollandmod = dieroll + int(mod)
rollandmod = str(rollandmod)
mod_total = total + int(mod)
mod_total = str(mod_total)
multiplemod = total + modtotal

#print totals
if len(dienumlist) > 1:
    while index_x < len(numdicelist):
        howmany = numdicelist[index_x]
        die = dienumlist[index_x]
        roll = roll_list[0:howmany]
        print(str(howmany) + 'D' + str(die) + ' rolls = ' + str(roll))
        index_x += 1
        del roll_list[0:howmany]
    print('Overall total = ' + str(multiplemod))
elif dienum == 20 and dieroll == 20 and numdice == 1:
    print("20 + mod = " + str(rollandmod) + ", Critical Success")
elif dienum == 20 and dieroll == 1 and numdice == 1:
    print("1 + mod = " + str(rollandmod) + ", Critical Failure")
elif numdice > 1:
    print(str(dicelist) + " + mod = " + str(mod_total))
elif mod == 0:
    print(str(dieroll))
else:
    print(str(dieroll) + " + mod = " + str(rollandmod))
