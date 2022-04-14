'''
Created on 6 abr. 2022

@author: yaser alamin  

clocks for mutliClocks and fining time in different location in the world 

to make set up meeting easier 

'''

import time
from datetime import datetime
# import pytz
# import os

import myclasses

clocks = []  # create empty list for the different time-zones(clocks)

moreClocks = True 

while moreClocks: 
    # to add time zones (clocks)   
    cityName = input('Input the new city name: ')
    timeZone = input('Input the new time-zone: ')
    clocks.append(myclasses.cityClock(cityName, timeZone))
    #  to chose if more clocks needed 
    i = input('input (y) if you want more time-zone clock: ') 
    print(i)
    if i == 'y':
        moreClocks = True 
    else:
        moreClocks = False

while True: 
    ''' 
    print('start ')
    os.system('cls') # Clear Console in if the os windows or change for 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    '''
    clearConsole = lambda: print('\n' * 150)
    clearConsole() 

    localTime = datetime.now()
    
    print("Date & Time  Local   : ",
    localTime.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
    
    for x in clocks:  # for each time zone in that saved in 'clocks' list
        x.outputClock()
        
    time.sleep(1)

