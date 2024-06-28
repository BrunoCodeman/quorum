
from typing import List
from lib.models import Bill, Legislator, Vote, VoteResult, VoteResult, VoteType

legislators_list:List[Legislator] = [Legislator(1, 'John Doe'), Legislator(2, 'Jane Doe'),
                                      Legislator(3, 'Joseph Doe'), Legislator(4, 'Janice Doe')]

bills_list:List[Bill] = [Bill(1,'The Green Act',1),
                         Bill(2,'Some Dems bill',1),
                         Bill(3,'Some Reps bill',4),
                         Bill(4,'What do you mean by "The people is going to pay the" bill?',2),]

votes_list:List[Vote] = [Vote(1,1),Vote(2,1),Vote(3,1),Vote(4,1), 
                         Vote(5,2), Vote(6,2), Vote(7,2), Vote(8,2),
                         Vote(9,3), Vote(10,3), Vote(11,3), Vote(12,3),
                         Vote(13,4), Vote(14,4), Vote(15,4), Vote(16,4),]

vote_results_list:List[VoteResult] = [VoteResult(1,1,1,VoteType.YES),VoteResult(2,1,2,VoteType.NO),
                                       VoteResult(3,1,3,VoteType.YES),VoteResult(4,1,4,VoteType.NO),
                                       VoteResult(5,2,5,VoteType.YES),VoteResult(6,2,6,VoteType.NO),
                                       VoteResult(7,2,7,VoteType.YES),VoteResult(8,2,8,VoteType.NO),
                                       VoteResult(9,3,9,VoteType.YES),VoteResult(10,3,10,VoteType.NO),
                                       VoteResult(11,3,11,VoteType.YES),VoteResult(12,3,12,VoteType.NO),
                                       VoteResult(13,4,13,VoteType.YES),VoteResult(14,4,14,VoteType.NO),
                                       VoteResult(15,4,15,VoteType.YES),VoteResult(16,4,16,VoteType.NO),]