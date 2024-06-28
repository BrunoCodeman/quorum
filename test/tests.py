import unittest
from lib.models import Legislator
from test import legislators_list


class LegislatorsUnitTest(unittest.TestCase):
    
    
    def setUp(self) -> None:
        self.legislator:Legislator = legislators_list[0]

    def must_get_bills_by_legislator(self):
        pass

    def test_must_get_legislators_legislators_by_bill(self):
        pass
    
