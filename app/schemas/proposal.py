from pydantic import BaseModel
from typing import List

class ProposalCreate(BaseModel):
    text: str
    
class ProposalCard(BaseModel):
    card_title: str
    proposal_category: str
    recommended_tool: str
    introduction_hint: str
    
class ProposalResult(BaseModel):
    proposals: List[ProposalCard]
    