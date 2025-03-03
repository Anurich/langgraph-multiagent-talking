from utils.prompts.agent_prompts import RESTAURANT_PROMPT
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent
from utils.utility import make_handoff_tool
from specialised_agents.tools.res_tool import res_hopping


class RESTAURANT:
    def __init__(self, llm):
        self.model =  llm 
        self.send_to_bar_agent = make_handoff_tool(agent_name="bar_agent")
        self.send_to_site_agent= make_handoff_tool(agent_name="area_agent")
        self.__createagent__()

        
    def __createagent__(self):
        self.react_res_agent = create_react_agent(
            model= self.model, 
            tools= [res_hopping, self.send_to_bar_agent, self.send_to_site_agent],
            name="resturant_agent",
            prompt=RESTAURANT_PROMPT
        )
    
    
    def __getagent__(self):
        return self.react_res_agent
    