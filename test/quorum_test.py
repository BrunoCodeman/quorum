import os
import unittest
from lib.business_logic import __read_and_convert__, generate_bills_report_csv, generate_legislators_report_csv, get_legislator_support, get_voted_bills
from lib import bills_filepath, legislators_filepath, votes_filepath, vote_results_filepath
from lib.models import Bill, Legislator, Vote, VoteResult
from test import bills_list, legislators_list,  vote_results_list, votes_list

class QuorumTest(unittest.TestCase):
    
#1. For every legislator in the dataset,how many bills did the legislator support(voted for the bill)? 
# How many bills did the legislator oppose?
    def test_must_get_legislators_by_bill(self):
        expected = get_legislator_support(legislators=legislators_list,vote_results=vote_results_list)
        self.assertIsNotNone(expected)

#2. For every bill in the dataset,how many legislators supported the bill? 
# How many legislators opposed the bill? Who was the primary sponsor of the bill?
    def must_get_bills_by_legislator(self):
        expected = get_voted_bills(bills=bills_list, vote_results=vote_results_list, votes=votes_list)
        self.assertIsNotNone(expected)

    def test_must_read_bills(self):
        bills = __read_and_convert__(bills_filepath, Bill)
        self.assertIsNotNone(bills)
    
    def test_must_read_legislators(self):
        legislators = __read_and_convert__(legislators_filepath, Legislator)
        self.assertIsNotNone(legislators)

    def test_must_read_votes(self):
        votes = __read_and_convert__(votes_filepath, Vote)
        self.assertIsNotNone(votes)

    def test_must_read_vote_results(self):
        results = __read_and_convert__(legislators_filepath, Legislator)
        self.assertIsNotNone(results)

    def test_must_generate_legislators_report_csv(self):
        report_filepath='legislators-support-oppose-count.csv'
        generate_legislators_report_csv(report_filepath)
        file_exists = os.path.isfile(report_filepath)
        self.assertTrue(file_exists)
        #os.remove(report_filepath)
        
    def test_must_generate_bills_report_csv(self):
        report_filepath='bills.csv'
        generate_bills_report_csv(report_filepath)
        file_exists = os.path.isfile(report_filepath)
        self.assertTrue(file_exists)
       # os.remove(report_filepath)
