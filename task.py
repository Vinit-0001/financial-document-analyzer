from crewai import Task
from agents import financial_analyst, investment_advisor, risk_assessor

# --- TASK DEFINITIONS ---
# Task 1: Financial Analysis
# This task is assigned to the financial_analyst agent.
# It focuses on reading the document and performing a detailed analysis.
analyze_document = Task(
    description="""Read the financial document provided at the file path: '{file_path}'.
    Your primary goal is to conduct a thorough analysis of this document. Extract key financial metrics such as revenue, 
    net income, profit margins, and earnings per share (EPS). Identify any significant trends, strengths, weaknesses, 
    opportunities, and threats (SWOT analysis) based on the data.
    
    Do not provide any investment advice or risk assessment; your focus is purely on objective financial analysis.
    """,
    expected_output="""A detailed and well-structured financial analysis report.
    The report should include:
    1. A summary of the document's key highlights.
    2. A list of extracted key financial metrics with their values.
    3. An analysis of financial trends observed in the document.
    4. A brief SWOT analysis (Strengths, Weaknesses, Opportunities, Threats).
    
    The final output should be a clean, readable text document that will be used by other specialists.
    """,
    agent=financial_analyst,
    # The output of this task will not be part of the final output,
    # but will be available in the context for the subsequent tasks.
    output_file="financial_analysis.txt"
)

# Task 2: Investment Recommendation
# This task is assigned to the investment_advisor agent.
# It depends on the context from the financial analysis task.
recommend_investment = Task(
    description="""Using the financial analysis report provided in the context, develop a strategic investment recommendation.
    Evaluate the company's growth potential, competitive positioning, and overall market sentiment.
    Consider the user's query: '{query}' when framing your recommendation.
    
    Your final recommendation should be clear, actionable, and supported by evidence from the financial analysis.
    """,
    expected_output="""A concise investment advisory report.
    The report should contain:
    1. A summary of the key financial health indicators.
    2. An evaluation of the investment potential (e.g., growth prospects, valuation).
    3. A clear investment recommendation: "Buy", "Hold", or "Sell".
    4. A justification for your recommendation, referencing specific data points from the analysis.
    """,
    agent=investment_advisor,
    context=[analyze_document],
    output_file="investment_recommendation.txt"
)

# Task 3: Risk Assessment
# This task is assigned to the risk_assessor agent.
# It also depends on the context from the initial analysis.
assess_risk = Task(
    description="""Based on the provided financial analysis, conduct a comprehensive risk assessment.
    Identify potential market, credit, operational, and liquidity risks associated with the company.
    Use web search tools to find current market conditions or news that could impact the company's risk profile.
    
    Provide a balanced view, avoiding sensationalism. Your assessment must be objective and data-driven.
    """,
    expected_output="""A structured risk assessment report.
    The report should detail:
    1. A list of identified risks, categorized by type (Market, Credit, etc.).
    2. An analysis of the potential impact and likelihood of each risk.
    3. A concluding summary of the company's overall risk profile.
    """,
    agent=risk_assessor,
    context=[analyze_document],
    output_file="risk_assessment.txt"
)
