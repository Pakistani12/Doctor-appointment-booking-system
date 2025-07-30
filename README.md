# Hospital Chatbot with RAG + Agent (LangGraph + LangChain + FastAPI)
Medical Chatbot (LangChain + LangGraph + FastAPI) for Doctor appointment booking
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
hospital_medical_chatbot/
├── main.py                ← FastAPI app (chatbot backend)
├── agent_graph.py         ← LangGraph workflow (RAG + booking agent)
├── tools.py               ← Doctor finder, booking, Twilio SMS
├── rag.py                 ← Load & retrieve from WHO docs (PDF)
├── data/
│   └── WHO_Clinical_Guidelines.pdf ← Medical doc for RAG
├── .env                   ← API keys (OpenAI, Twilio)
├── requirements.txt
└── README.md              ← Documentation
```



