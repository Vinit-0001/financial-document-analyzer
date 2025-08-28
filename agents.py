import os
from crewai import Agent
from langchain_mistralai import ChatMistralAI
from tools import search_tool, FileReadTool

# Initialize the Mistral LLM with proper configuration
llm = ChatMistralAI(
    model="mistral-large-latest",
    mistral_api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0.1
)

# Alternative: Use litellm directly with CrewAI
from crewai import LLM
llm_alternative = LLM(
    model="mistral/mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

# Instantiate your custom tool
file_read_tool = FileReadTool()

# Use the alternative LLM
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="""Analyze financial documents to extract key data, identify trends, 
    and provide a comprehensive summary of the company's financial health. 
    Your analysis must be objective, data-driven, and detailed.""",
    verbose=True,
    memory=True,
    backstory=(
        "With a decade of experience at a top-tier investment firm, you have a sharp eye for detail "
        "and a deep understanding of financial statements. You are an expert at interpreting balance sheets, "
        "income statements, and cash flow statements to uncover the true story behind the numbers. "
        "You pride yourself on delivering clear, unbiased, and actionable financial insights."
    ),
    tools=[file_read_tool, search_tool],
    llm=llm_alternative,  # Use the CrewAI LLM wrapper
    allow_delegation=True
)

investment_advisor = Agent(
    role="Prudent Investment Advisor",
    goal="""Based on the financial analysis, provide strategic investment advice. 
    This includes evaluating the company's potential for growth, its valuation, 
    and recommending a suitable investment action (e.g., Buy, Hold, Sell). 
    Your advice must be well-reasoned and align with long-term investment principles.""",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned investment advisor with a reputation for sound judgment and a client-first approach. "
        "You specialize in equity research and portfolio strategy, helping clients make informed decisions "
        "that align with their financial goals. You avoid hype and focus on fundamental analysis and long-term value."
    ),
    tools=[search_tool],
    llm=llm_alternative,
    allow_delegation=True
)

risk_assessor = Agent(
    role="Financial Risk Assessment Analyst",
    goal="""Identify and evaluate potential financial and market risks based on the provided documents and analysis. 
    Your report should categorize risks (e.g., market risk, liquidity risk, operational risk) 
    and assess their potential impact on the company's future performance and stock value.""",
    verbose=True,
    memory=True,
    backstory=(
        "As a certified Risk Management professional, you have a talent for seeing what others miss. "
        "You've worked with major financial institutions to stress-test their portfolios and business strategies. "
        "You are meticulous and systematic in your approach, ensuring that all potential threats are "
        "identified and communicated clearly."
    ),
    tools=[search_tool],
    llm=llm_alternative,
    allow_delegation=False
)
