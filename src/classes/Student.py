'''
Created on 24-12-2019

@author: tiberwood
'''
from time import mktime
from datetime import datetime

class Student:
    '''
    classdocs
    '''


    def __init__(self, name, hour_begin, hour_end, classroom):
        '''
        Constructor
        '''
        self.__name = name
        self.__hour_begin = hour_begin
        self.__hour_end = hour_end
        self.__classroom = classroom
        
    def getMinutesPerDay(self):
        fmt = '%H:%M'
        d1 = datetime.strptime(self.__hour_begin, fmt)
        d2 = datetime.strptime(self.__hour_end, fmt)
        d1_ts = mktime(d1.timetuple())
        d2_ts = mktime(d2.timetuple())
        result = int(d2_ts - d1_ts) / 60
        return result
        