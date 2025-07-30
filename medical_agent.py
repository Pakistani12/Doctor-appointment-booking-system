from langchain.agents.tools import Tool
from db.mysql_connection import insert_appointment

def book_appointment_tool(**kwargs):
    name = kwargs.get("name")
    time = kwargs.get("time")
    insert_appointment(name, time)
    return f"Appointment confirmed for {name} at {time}."

tools = [
    Tool(name="book_appointment", func=book_appointment_tool, description="Book patient appointment"),
]