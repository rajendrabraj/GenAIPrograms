import streamlit  as st
import os 

# st.write("Test Program")

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo


web_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    debug_mode=False,
    show_tool_calls=True,
    add_datetime_to_instructions==True,
    add_chat_history_to_messages==True,
    storage=(table_name="agent_sessions",db_file="tmp/agent.db")

)
#Query = input('what is your query?\n')     # \n ---> newline  ---> It causes a line break
#print(Query) 

#Query=st.text_area("What is your query\n")
Query= "Price of Indian Oil Stock"

#web_agent.print_response("Tell me about OpenAI Sora?", stream=True)

# web_agent.print_response(Query, stream=True)
#os.write web_agent.print_response(Query, stream=True)
st.write("Getting results on the screen\n")

st.write (web_agent.print_response(Query, stream=True))
#os.write web_agent.print_response(Query, stream=True)




