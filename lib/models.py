
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
    @property
    def id(self) ->int:
        return self.legislator.id
    @property
    def name(self) ->str:
        return self.legislator.name

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
    YES = '1'
    NO = '2'

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
    def id(self) ->int:
        return self.bill.id
    @property
    def title(self) ->int:
        return self.bill.title
    @property
    def primary_sponsor(self) ->int:
        return self.bill.sponsor_id


