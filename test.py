# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from SimpleMachines import lever
from SimpleMachines import pulley

class TestLeverClass(unittest.TestCase):
    def setUp(self):
        self.lever = lever(10, 25, 5)
        
    def test_initialization(self): 
        self.assertEqual(self.lever.F, 10, 'incorrect F')
        self.assertEqual(self.lever.stdev, 25, 'incorrect P')
        self.assertEqual(self.lever.F_length, 5, 'incorrect F length')
        self.assertEqual(self.lever.stdev, 2, 'incorrect P length')

    def test_calculate_Plength(self):
        self.assertEqual(self.lever.calculate_Plength(), 2, 'calculated P length is not as expected')

    def test_update_lengths(self):
        self.assertEqual(round(self.lever.update_Flength(10), 2), 10, 'F length calculations incorrect')
        self.assertEqual(round(self.lever.update_Plength(4), 2), 12.5, 'population standard deviation incorrect')
        
        
        
class pulley(unittest.TestCase):
    def setUp(self):
        self.pulley = pulley(F = 10, movable = 3)

    def test_initialization(self):
        self.assertEqual(self.pulley.F, 10, 'F value incorrect')
        self.assertEqual(self.pulley.P, 80, 'P value incorrect')
        self.assertEqual(self.pulley.movable, 3, 'p value incorrect')
        self.assertEqual(self.pulley.fixed, 1, 'n value incorrect')

    
    def test_findStrGain(self):
        calc_strgain = self.pulley.findStrGain()
        self.assertEqual(calc_strgain, 8)
    
    def test_calculate_load_distance(self):
        ld = self.lever.calculate_load_distance(16)
        self.assertEqual(round(ld, 2), 2)
        
    def test_replace_stats_with_data(self):
        p, n = self.binomial.replace_stats_with_data()
        self.assertEqual(round(p,3), .615)
        self.assertEqual(n, 13)
        
    def test_pdf(self):
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.01235)
    
        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00472)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two
        
        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)
        
    
if __name__ == '__main__':
    unittest.main()