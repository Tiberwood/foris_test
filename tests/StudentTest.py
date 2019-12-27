import unittest
from datetime import datetime
from time import mktime
import os


class StudentTest(unittest.TestCase):
    
    def setUp(self):
        self.student_name = 'Francis'
        self.weekday = 3
        self.begin_hour = '10:34'
        self.end_hour = '18:03'
        self.classroom_code = 'F100'
    
    def test_minutes_difference(self):
        fmt = '%Y-%m-%d %H:%M:%S'
        d1 = datetime.strptime(self.begin_hour, fmt)
        d2 = datetime.strptime(self.end_hour, fmt)
        d1_ts = mktime(d1.timetuple())
        d2_ts = mktime(d2.timetuple())
        result = int(d2_ts - d1_ts) / 60
        self.assertGreater(result, 1)        