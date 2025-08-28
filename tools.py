import os
from crewai.tools import BaseTool
from pypdf import PdfReader
# This is kept from the original file, it provides web search functionality.
# Make sure to have SERPER_API_KEY in your .env file for this to work.
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

class FileReadTool(BaseTool):
    name: str = "File Read Tool"
    description: str = "A tool to read the full content of a file given its file path."
    
    def _run(self, file_path: str) -> str:
        """
        Tool to read the full content from a file path.
        Currently supports PDF files.
        """
        # Ensure the file exists
        if not os.path.exists(file_path):
            return f"Error: File not found at path: {file_path}"
        
        # Check if the file is a PDF
        if file_path.lower().endswith('.pdf'):
            try:
                reader = PdfReader(file_path)
                full_text = ""
                for page in reader.pages:
                    full_text += page.extract_text() + "\n"
                
                # Simple cleaning of the text
                cleaned_text = ' '.join(full_text.split())
                return cleaned_text
            except Exception as e:
                return f"Error reading PDF file: {e}"
        else:
            return "Error: This tool currently only supports reading .pdf files."
