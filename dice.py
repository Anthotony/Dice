dienum = input('Which die would you like to use?\n')
dienum = int(dienum)
mod = input('Modifiers/Damage Bonus')
mod = int(mod)

import random
dieroll = random.randint(1, dienum)

if dienum == 20:
    print('Rolling D20...')
else:
    print('Rolling...')

import time
time.sleep(1)

rollandmod = dieroll + mod
rollandmod = str(rollandmod)

if dienum == 20 and dieroll == 20:
    print("20, total " + rollandmod + "Critical Success")
elif dienum == 20 and dieroll == 1:
    print("1, total " + rollandmod + ", Critical Failure")
else:
    print(str(dieroll) + 'total' + rollandmod)
