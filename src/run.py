from langchain_openai import ChatOpenAI

from supervised_agent.supervisor import SUPERVISED
api_keys = ""
model = ChatOpenAI(model="gpt-4o-mini", api_key=api_keys)


workflow = SUPERVISED(model)
app = workflow.supervisor.compile()

# png_graph = app.get_graph().draw_mermaid_png()
# with open("my_graph.png", "wb") as f:
#     f.write(png_graph)
    

result = app.invoke({
    "messages": [
        {
            "role": "user",
            "content": " best bar london ?"
        }
    ]
})

for m in result["messages"]:
    m.pretty_print()