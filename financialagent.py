from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import openai

import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")



##web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",    
    model=Groq(id="llama-3.2-1b-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown= True, 


)

##Finance Agent 
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.2-1b-preview"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions=["Use Tables to Display the data"],
    show_tools_calls=True,
    markdown= True, 


)

##MultModal Agent

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Use Tables to display the data"],
    show_tools_calls=True,
    markdown= True, 

)

##Finally Call both the Agents to see the data.
multi_ai_agent.print_response("Amber Enterprises vs Peers ",stream=True)
