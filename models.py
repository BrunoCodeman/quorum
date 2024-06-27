
from dataclasses import dataclass
from enum import Enum

@dataclass
class Legislator:
    id:int
    name:str

@dataclass
class Bill:
    id:int
    title:str
    primary_sponsor:int

@dataclass
class Vote:
    id:int
    bill_id:int

class VoteChoice(Enum):
    """
    Choices for voting
    """
    YES = 1
    NO = 2

@dataclass
class VotedResult:
    id:int
    legislator_id:int
    vote_id:int
    vote_type:VoteChoice


