# Financial Document Analyzer

A professional financial document analysis system using CrewAI agents to provide comprehensive investment recommendations, risk assessments, and financial insights.

---

## 🐛 Bugs Found and Fixed

### Critical Issues Identified

#### `agents.py`
1. **Undefined LLM variable** – Fixed by properly importing and configuring Mistral LLM  
2. **Unprofessional agent descriptions** – Rewrote with professional, accurate roles  
3. **Incorrect tool syntax** – Changed from `tool=` to `tools=`  
4. **References to undefined tools** – Created proper `FileReadTool` implementation  
5. **Joke/sarcastic descriptions** – Replaced with professional, accurate descriptions  
6. **Missing imports** – Added all required imports  

#### `main.py`
1. **Missing imports** – Added Crew, Process, and other required imports  
2. **Function name conflict** – Renamed crew function to avoid endpoint conflict  
3. **Incomplete crew setup** – Proper crew configuration with all agents and tasks  
4. **Missing error handling** – Added comprehensive try-catch blocks  
5. **Undefined references** – Fixed all agent and task references  

#### `tasks.py`
1. **Unprofessional task descriptions** – Rewrote with clear, professional objectives  
2. **Undefined agent references** – Fixed agent imports and references  
3. **Non-existent tools** – Implemented proper CrewAI tools  
4. **Encouraging misinformation** – Tasks now focus on accurate analysis  
5. **Poor expected outputs** – Clear, structured output requirements  

#### `tools.py`
1. **Undefined `Pdf` class** – Implemented using PyPDF2/pypdf  
2. **Incorrect tool structure** – Proper CrewAI `BaseTool` inheritance  
3. **Missing tool implementations** – Full working implementations  
4. **Missing imports** – All required imports added  

---

## 🚀 Features

- **Multi-Agent Analysis**: Financial Analyst, Investment Advisor, and Risk Assessor  
- **PDF Document Processing**: Automatic extraction and analysis of financial documents  
- **Web Search Integration**: Real-time market data and news analysis  
- **REST API**: FastAPI-based endpoints for easy integration  
- **Comprehensive Reports**: Structured analysis, recommendations, and risk assessments  

---

## 📋 Requirements

- Python 3.8+  
- Mistral API Key  
- Serper API Key (for web search)  

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/financial-document-analyzer
cd financial-document-analyzer

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Choose one LLM provider
OPENAI_API_KEY=your_openai_api_key_here
# OR
MISTRAL_API_KEY=your_mistral_api_key_here

# Web search (optional but recommended)
SERPER_API_KEY=your_serper_api_key_here

mkdir data

uvicorn main:app --reload

GET /

{
  "message": "Financial Document Analyzer API is running",
  "endpoints": {...}
}

POST /analyze/

curl -X POST "http://127.0.0.1:8000/analyze/" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@financial_report.pdf" \
  -F "query=Provide detailed investment recommendation"

{
  "status": "success",
  "message": "Analysis completed successfully",
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "result": {
    "financial_analysis": "Detailed financial metrics and trends...",
    "investment_recommendation": "Strategic investment advice...",
    "risk_assessment": "Comprehensive risk evaluation...",
    "crew_output": "Combined analysis results..."
  }
}

GET /status/{job_id}

{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "completed",
  "result": {...}
}

```

Agent Roles

Senior Financial Analyst

1) Role: Extract and analyze key financial metrics
2) Capabilities: Revenue analysis, profit margins, EPS, SWOT analysis
3) Tools: File reading, web search

Investment Advisor

1) Role: Provide strategic investment recommendations
2) Capabilities: Growth evaluation, competitive analysis, buy/hold/sell recommendations
3) Tools: Web search for market sentiment

Risk Assessment Analyst

1) Role: Identify and evaluate financial risks
2) Capabilities: Market risk, credit risk, operational risk assessment
3) Tools: Web search for current market conditions

**PROJECT STRUCTURE**

financial-document-analyzer/
├── main.py              # FastAPI application
├── agents.py            # CrewAI agent definitions  
├── tasks.py             # Task definitions for agents
├── tools.py             # Custom tools for file reading
├── crew_processor.py    # CrewAI workflow execution
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── README.md            # This documentation
└── data/                # Uploaded files directory

**Development**

Testing
# Run the application in development mode
uvicorn main:app --reload --log-level debug

# Test with curl
curl -X POST "http://127.0.0.1:8000/analyze/" \
  -F "file=@test_document.pdf" \
  -F "query=Test analysis"


🚨 Error Handling

The system includes comprehensive error handling for:
  
 1) Invalid file formats
 2) API rate limits
 3) LLM failures
 4) File processing errors
 5) Network connectivity issues
