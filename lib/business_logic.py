import csv
from typing import Dict, List
from lib.models import Bill, Legislator, LegislatorSupport, Vote, VoteResult, VoteType, VotedBill
from . import __read_and_convert__, bills_filepath,legislators_filepath, votes_filepath, vote_results_filepath

def get_bills_list()->List[Bill]:
    """
    Gets the list of Bills in the CSV file

    Returns:
        The list of Bills
    """
    return __read_and_convert__(bills_filepath, Bill)

def get_legislators_list()->List[Legislator]:
    """
    Gets the list of Legislators in the CSV file

    Returns:
        The list of Legislators
    """
    return __read_and_convert__(legislators_filepath, Legislator)

def get_votes_list()->List[Vote]:
    """
    Gets the list of Votes in the CSV file

    Returns:
        The list of Votes
    """
    return __read_and_convert__(votes_filepath, Vote)

def get_vote_results_list()->List[VoteResult]:
    """
    Gets the list of VoteResults in the CSV file

    Returns:
        The list of VoteResults
    """
    return __read_and_convert__(vote_results_filepath, VoteResult)
    
def get_legislator_support(legislators:List[Legislator], 
                           vote_results:List[VoteResult]) -> List[LegislatorSupport]:
    """
    Builds a list of LegislatorSupport, containing the data about supports and opposes of a legislator to a bill.
    Parameters:
    -   legislators: A list of the Legislators which positions should be searched
    -   vote_results: A list of VoteResults of the bills

    Returns:
        A list of LegislatorSupport with data about how many projects were supported or opposed by each legislator
    """
    supports:List[LegislatorSupport] = []
    for l in legislators:
        support = LegislatorSupport(legislator=l,num_opposed_bills=0,num_supported_bills=0)
        for vr in vote_results:
            if vr.legislator_id == l.id:
                if vr.vote_type == VoteType.YES:
                    support.num_supported_bills+=1
                if vr.vote_type == VoteType.NO:
                    support.num_opposed_bills+=1
        supports.append(support)
    return supports

def get_voted_bills(bills:List[Bill], votes:List[Vote], vote_results:List[VoteResult]) -> List[VotedBill]:
    """
    Builds a list of VotedBills, containing information about the support and oppose to the bills

    Parameters:
    - bills: The bills voted by the legislators
    - votes: The votes of the bills
    - vote_results: the results of the votes

    Returns:
    A list of VotedBills with information about who's the sponsor, general support and opposition
    """
    voted_bills: List[VotedBill] = []
    for bill in bills:
        voted = VotedBill(bill=bill,supporter_count=0,opposer_count=0)
        for v in votes:
            if v.bill_id == bill.id:
                for vr in vote_results:
                    if v.id == vr.vote_id:
                        if vr.vote_type == VoteType.YES:
                            voted.supporter_count+=1
                        if vr.vote_type == VoteType.NO:
                            voted.opposer_count+=1
        voted_bills.append(voted)
    return voted_bills

def generate_bills_report_csv(bills_report_file_path:str):
    """
    Generates a CSV report containing data about the support and opposition of the bills
    
    Parameters:
    - bills_report_file_path: The file path where the CSV file must be generated
    """

    bills = get_bills_list()
    votes = get_votes_list()
    vote_results = get_vote_results_list()
    supports = get_voted_bills(bills=bills, votes=votes, vote_results=vote_results)
    field_names=['id','title', 'supporter_count',
                'opposer_count', 'primary_sponsor']
    __write_content__(bills_report_file_path,supports, field_names)
        
def generate_legislators_report_csv(legislators_report_file_path:str):
    """
    Generates a CSV report containing data about how the legislators voted
    
    Parameters:
    - bills_report_file_path: The file path where the CSV file must be generated
    """
    vote_results = get_vote_results_list()
    legislators = get_legislators_list()
    supports = get_legislator_support(legislators=legislators, vote_results=vote_results)
    field_names=['id','name', 'num_supported_bills', 'num_opposed_bills']
    __write_content__(legislators_report_file_path, supports, field_names)


def __write_content__(filepath:str, lst:List, field_names:List[str]):
    """
    Write a list of ojects to a CSV file.
    Parameters:
    - file_path: The file path where the CSV file must be generated
    - lst: The list of objects to be saved as CSV
    - field_names: the names of the fields to be used in the CSV and also the keys of the objects to be inserted
    """
    with open(filepath,'w') as csv_file:
        fieldnames=lst[0].__dict__.keys()
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        for l in lst:
            data = {}
            for field in field_names:
                data[field] = getattr(l, field)
            writer.writerow(data)
    

