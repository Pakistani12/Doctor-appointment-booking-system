# Hospital Chatbot with RAG + Agent (LangGraph + LangChain + FastAPI)
A real-world healthcare chatbot that combines Retrieval-Augmented Generation (RAG), LangGraph agents, FastAPI, MySQL, Twilio (for SMS), and a Streamlit UI.
## **Features**
- Medical questions (via RAG over WHO PDFs)
- Appointment booking (Agent with calendar + Twilio SMS)

## **Installation**
1-Create a virtual environment and install dependencies:
```sh
python -m venv venv
venv/Scripts/activate  
pip install -r requirements.txt
```

### Setup
1. Add your `.env` keys for OpenAI and Twilio
2. Place your medical document in `/data/`
3. Run the server:
   ```bash
   uvicorn main:app --reload

## **Project Structure**
```"plaintext"
medical_rag_agent_app/
├── agents/
│   ├── medical_agent.py
│   └── langgraph_flow.py
├── rag/
│   ├── rag_pipeline.py
│   ├── documents/
│   │   └── medical_docs.pdf
│   └── vectorstore/
├── db/
│   └── mysql_connection.py
├── api/
│   └── main.py
├── ui/
│   └── streamlit_ui.py
├── .env
└── requirements.txt
```
## **License**

This project is licensed under the MIT License.


