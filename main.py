#Retrieve the required libraries 
from fastapi import FastAPI
from graph import agent_app
from pydantic import BaseModel

#Application definition 
app = FastAPI()

#Definition of future inputs 
class ChatRequest(BaseModel):
    query: str
    session_id: str

#Creating the endpoint 
@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    # Setting up a session in PostgreSQL 
    config = {"configurable": {"thread_id": req.session_id}}
    
    inputs = {"messages": [("user", req.query)]}
    final_output = await agent_app.ainvoke(inputs, config)
    
    return {"response": final_output["messages"][-1].content} #Return the output 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080) #Server setup( Reilway) 
