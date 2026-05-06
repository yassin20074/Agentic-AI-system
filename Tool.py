#Retrieve the required libraries 
from langchain_community.tools.tavily_search import TavilySearchResults
import os
#It needs an APIKey 
search_tool = TavilySearchResults(k=3, ApiKey="******")
tools = [search_tool] 
