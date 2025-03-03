from utils.prompts.agent_prompts import SITE_PROMPT
from langgraph.prebuilt import create_react_agent
from utils.utility import make_handoff_tool
from specialised_agents.tools.area_tool import area_hopping


class AREA:
    def __init__(self, llm):
        self.model = llm
        self.send_to_restaurant_agent = make_handoff_tool(agent_name="resturant_agent")
        self.send_to_bar_agent= make_handoff_tool(agent_name="bar_agent")
        self.__createagent__()

        
    def __createagent__(self):
        self.react_area_agent = create_react_agent(
            model= self.model, 
            tools= [area_hopping, self.send_to_bar_agent, self.send_to_restaurant_agent],
            name="area_agent",
            prompt=SITE_PROMPT
        )
    
    
    def __getagent__(self):
        return self.react_area_agent
    