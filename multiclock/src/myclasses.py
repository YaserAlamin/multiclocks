'''
Created on 6 abr. 2022

@author: yrala
'''
import pytz
from datetime import datetime


class cityClock():
    '''
    classdocs
    '''
    
    
    def __init__(self, cityName, cityTimeZone):
        '''
        Constructor
        '''
        self.TTZ = pytz.timezone(cityTimeZone) # the time zone from pytz
        self.city=cityName
        self.cityTimeZone=cityTimeZone
    
    
    def conformClass(self):
        print('the city of ',self.city,' added which has time zone of ',self.cityTimeZone, self.TTZ.strftime('%Z %z'))
    
    
    def outputClock(self):
        datetime_ini = datetime.now(self.TTZ)
        print("Date & Time in ",self.city,"   : ",
        datetime_ini.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

    