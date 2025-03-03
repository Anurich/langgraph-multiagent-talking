
from langchain_core.messages import AIMessage
def area_hopping(area_name: str):
    """ use when need to see different places in the area """
    return f"""
    The places to visit in {area_name} are:
    1. Ram jhula 
    2. Bridge gate
    """
