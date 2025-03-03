from utils.prompts.agent_prompts import BAR_PROMPT
from langgraph.prebuilt import create_react_agent
from utils.utility import make_handoff_tool
from specialised_agents.tools.bar_tool import bar_hopping


class BAR:
    def __init__(self, llm):
        self.model =  llm 
        self.send_to_restaurant_agent = make_handoff_tool(agent_name="resturant_agent")
        self.send_to_site_agent= make_handoff_tool(agent_name="area_agent")
        self.__createagent__()

        
    def __createagent__(self):
        self.react_bar_agent = create_react_agent(
            model = self.model, 
            tools= [bar_hopping, self.send_to_restaurant_agent, self.send_to_site_agent],
            name="bar_agent",
            prompt=BAR_PROMPT
        )
    
    
    def __getagent__(self):
        return self.react_bar_agent
    