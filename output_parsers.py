from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field , root_validator

class Summary(BaseModel):
    
    summary: str = Field(description = "summary")
    facts: List[str] = Field(description = "interesting facsts about them")
    
    def to_dict(self) -> Dict[str,Any] :
        return {"summary": self.summary, "facts": self.facts}
    

summary_parser = PydanticOutputParser(pydantic_object=Summary)
    
    