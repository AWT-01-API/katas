import unittest
from src.kevinsanchez.task3_11_06_2018.ExpandedForm import ExpandedForm

"""
test for expanded class.
"""
class TestExpandedForm(unittest.TestCase):

    """
    setup for the test.
    """
    def setUp(self):
        self.eForm = ExpandedForm()

    """
    test method expand.
    """
    def test_expand(self):
        self.assertEqual("10 + 2", self.eForm.expand(12))
        self.assertEqual("40 + 2", self.eForm.expand(42))
        self.assertEqual("70000 + 300 + 40 + 2", self.eForm.expand(70342))
