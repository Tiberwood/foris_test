import unittest

class ReportTest(unittest.TestCase):
    
    def setUp(self):
        self.data = ['David: 104.0 minutes in 1 day\n', 
                     'Marco: 142.0 minutes in 2 days\n', 
                     'Fran: 0 minutes\n'
                     ]
        
    def test_sort_data(self):
        values = self.data
        values.sort()
        #fail
        self.assertEqual(values[0], 'Marco: 142.0 minutes in 2 days\n')
        
    def sortDataValue(self, val):
        value = val.split(' ')
        return value[1]
    
    def test_sort_data_with_key(self):
        values = self.data
        values.sort(key=self.sortDataValue)
        #fail
        self.assertEqual(values[0], 'Marco: 142.0 minutes in 2 days\n')
        
    def test_sort_data_with_key_and_reverse(self):
        values = self.data
        values.sort(key=self.sortDataValue, reverse=True)
        self.assertEqual(values[0], 'Marco: 142.0 minutes in 2 days\n')