import unittest
from lib.business_logic import __read_and_convert__
from lib import bills_filepath, legislators_filepath, votes_filepath, vote_results_filepath
from lib.models import Bill, Legislator, Vote, VoteResult
from test import bills_list, legislators_list,  vote_results_list, votes_list

#1. For every legislator in the dataset,how many bills did the legislator support(voted for the bill)? 
# How many bills did the legislator oppose?
#2. For every bill in the dataset,how many legislators supported the bill? 
# How many legislators opposed the bill? Who was the primary sponsor of the bill?

class QuorumTest(unittest.TestCase):
    
    
    def setUp(self) -> None:
        self.legislator:Legislator = legislators_list[0]

    def must_get_bills_by_legislator(self):
        pass

    def test_must_get_legislators_legislators_by_bill(self):
        pass
    
    def test_must_read_bills(self):
        bills = __read_and_convert__(bills_filepath, Bill)
        self.assertIsNotNone(bills)
    
    def test_must_read_legislators(self):
        legislators = __read_and_convert__(legislators_filepath, Legislator)
        self.assertIsNotNone(legislators)

    def test_must_read_votes(self):
        votes = __read_and_convert__(votes_filepath, Vote)
        self.assertIsNotNone(votes)

    # def test_must_read_vote_results(self):
    #     results = __read_and_convert__(legislators_filepath, Legislator)
    #     self.assertIsNotNone(results)