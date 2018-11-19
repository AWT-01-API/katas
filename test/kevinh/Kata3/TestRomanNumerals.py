from src.kevinh.Kata3.RomanNumerals import RomanNumerals
import unittest


class TestFactorial(unittest.TestCase):
    def test_to_roman(self):
        self.assertEquals(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
        self.assertEquals(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
        self.assertEquals(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
        self.assertEquals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
        self.assertEquals(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')

    def test_from_roman(self):
        self.assertEquals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
        self.assertEquals(RomanNumerals.from_roman('I'), 1, 'I should == 1')
        self.assertEquals(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
        self.assertEquals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
        self.assertEquals(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')