import asyncio
import os
import time
from crewai import Crew, Process
from task import analyze_document, recommend_investment, assess_risk

async def process_document_with_crew(file_path: str, query: str):
    """
    Process a document using CrewAI agents and tasks with retry logic.
    """
    max_retries = 3
    retry_delay = 60  # seconds
    
    for attempt in range(max_retries):
        try:
            # Create the crew with the defined tasks
            crew = Crew(
                agents=[
                    analyze_document.agent,
                    recommend_investment.agent, 
                    assess_risk.agent
                ],
                tasks=[analyze_document, recommend_investment, assess_risk],
                process=Process.sequential,
                verbose=True
            )
            
            # Execute the crew with the provided inputs
            inputs = {
                'file_path': file_path,
                'query': query
            }
            
            # Run the crew
            result = crew.kickoff(inputs=inputs)
            
            # Read and combine results
            combined_result = {}
            
            output_files = [
                ("financial_analysis", "financial_analysis.txt"),
                ("investment_recommendation", "investment_recommendation.txt"),
                ("risk_assessment", "risk_assessment.txt")
            ]
            
            for key, filename in output_files:
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8') as f:
                        combined_result[key] = f.read()
                    os.remove(filename)
            
            combined_result["crew_output"] = str(result)
            return combined_result
            
        except Exception as e:
            error_msg = str(e).lower()
            if "rate" in error_msg or "capacity" in error_msg or "quota" in error_msg:
                if attempt < max_retries - 1:
                    print(f"Rate limit hit, waiting {retry_delay} seconds before retry {attempt + 1}/{max_retries}")
                    await asyncio.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                    continue
            raise Exception(f"CrewAI processing failed after {attempt + 1} attempts: {str(e)}")
    
    raise Exception("Max retries exceeded due to rate limits")
