import os
import uuid
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from dotenv import load_dotenv
from crew_processor import process_document_with_crew

load_dotenv()

app = FastAPI(title="Financial Document Analyzer API v3 (Simplified)")

# In-memory storage for job results
jobs = {}

@app.post("/analyze/")
async def analyze_document_endpoint(
    query: str = Form("Provide a detailed analysis, recommendation, and risk assessment."),
    file: UploadFile = File(...)
):
    """Uploads a file and processes it with CrewAI agents."""
    try:
        # Save uploaded file locally
        file_path = f"data/uploaded_{uuid.uuid4()}_{file.filename}"
        os.makedirs("data", exist_ok=True)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Generate a job_id
        job_id = str(uuid.uuid4())

        # Store initial job status
        jobs[job_id] = {
            "job_id": job_id,
            "status": "processing",
            "file_path": file_path,
            "query": query,
            "result": None
        }

        try:
            # Process with CrewAI
            result = await process_document_with_crew(file_path, query)
            
            jobs[job_id].update({
                "status": "completed",
                "result": result
            })
            
            return {
                "status": "success",
                "message": "Analysis completed successfully.",
                "job_id": job_id,
                "result": result
            }
            
        except Exception as e:
            jobs[job_id].update({
                "status": "failed",
                "result": {"error": str(e)}
            })
            raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status/{job_id}")
async def get_job_status(job_id: str):
    """Endpoint to get status/result of an analysis job."""
    job = jobs.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
