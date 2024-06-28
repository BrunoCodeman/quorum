
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class Legislator:
    id:int
    name:str

@dataclass
class LegislatorSupport:
    legislator:Legislator
    num_supported_bills:int
    num_opposed_bills:int

@dataclass
class Bill:
    id:int
    title:str
    sponsor_id:int

@dataclass
class Vote:
    id:int
    bill_id:int

class VoteType(Enum):
    """
    Choices for voting
    """
    YES = 1
    NO = 2

@dataclass
class VoteResult:
    id:int
    legislator_id:int
    vote_id:int
    vote_type:VoteType

@dataclass
class VotedBill:
    bill:Bill
    supporter_count:int
    opposer_count:int
    @property
    def primary_sponsor(self) ->int:
        ps = self.bill.sponsor_id
        return ps


