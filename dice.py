#input for number of dice, which dice, and any bonuses that apply
numdice = input('How many dice would you like to roll?\n')
numdice = int(numdice)
dienum = input('Which dice would you like to use?\n')
dienum = int(dienum)
dieroll = 0
dicelist = []

#character creation
if numdice == 4 and dienum == 6:
        cc = input('Are you making a character? 1 = yes, 2 = no\n')
        if int(cc) == 1:
                y = 4
                while y >= 1:
                        import random
                        x = random.randint(1, dienum)
                        dieroll = int(x)
                        dicelist.append(x)
                        y -= 1
                dicelist.sort()
                dicelist.pop(0)
                total = 0
                for roll in dicelist:
                        x = roll
                        total = total + x
                print(dicelist, total)
                        import random
                        x = random.randint(1, dienum)
                        dieroll = int(x)
                        dicelist.append(x)
                        y -= 1
                dicelist.sort()
                dicelist.pop(0)
                total = 0
                for roll in dicelist:
                        x = roll
                        total = total + x
                print(dicelist, total)
                exit()

#had to split bonuses for reasons
mod = input('Modifiers/Damage Bonus\n')
mod = int(mod)

#no values for # of dice less than 1
if numdice < 1:
    numdice = input('Please reinput the number of dice\n')
    numdice = int(numdice)

#rolls multiple dice and places them in a list
while numdice > 1 and len(dicelist) != numdice:
    import random
    x = random.randint(1, dienum)
    dicelist.append(x)

#rolls for only 1 die
if numdice == 1:
    import random
    dieroll += random.randint(1, dienum)

#totals list of dice
total = 0
for roll in dicelist:
    x = roll
    total = total + int(x)
#names and tells you which dice is rolling
print('Rolling D' + str(dienum) + '...')

#pause for 1 second.. style
import time
time.sleep(1)

#adds modifier
rollandmod = dieroll + mod
rollandmod = str(rollandmod)
mod_total = total + mod
mod_total = str(mod_total)

#print total
if dienum == 20 and dieroll == 20 and numdice == 1:
    print("20 + mod = " + rollandmod + "Critical Success")
elif dienum == 20 and dieroll == 1 and numdice == 1:
    print("1 + mod = " + rollandmod + ", Critical Failure")
elif numdice > 1:
    print(str(dicelist) + " + mod = " + mod_total)
elif mod == 0:
    print(str(dieroll))
else:
    print(str(dieroll) + " + mod = " + rollandmod)
