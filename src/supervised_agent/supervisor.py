from specialised_agents.agents.bar_specialist import BAR
from specialised_agents.agents.restuarant_agent import RESTAURANT
from specialised_agents.agents.site_seeing_agent import AREA
from langgraph_supervisor import create_supervisor
from utils.prompts.assistant_prompts import SUPERVISOR_PROMPT
from langchain_core.runnables import RunnableParallel

class  SUPERVISED:
    def __init__(self, llm ):
        self.bar_agent = BAR(llm)
        self.res_agent = RESTAURANT(llm)
        self.area_agent =  AREA(llm)
        
        
        self.supervisor = create_supervisor([self.bar_agent.__getagent__(), \
            self.area_agent.__getagent__(), self.res_agent.__getagent__()],model=llm, prompt=SUPERVISOR_PROMPT, \
                output_mode="full_history")
        
        