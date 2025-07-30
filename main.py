from fastapi import FastAPI, Request
from langgraph_flow import build_graph
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
graph_executor = build_graph()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("query")
    name = data.get("name")
    phone = data.get("phone")

    result = graph_executor.invoke({"input": user_input})

    send_sms(phone, result["output"])
    return {"reply": result["output"]}

def send_sms(to, msg):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))
    client.messages.create(body=msg, from_=os.getenv("TWILIO_PHONE"), to=to)