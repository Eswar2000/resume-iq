from fastapi import FastAPI, UploadFile
from app.utils.parse_pdf import parse_pdf
from app.agents.resume_extractor import extract_resume_info

app = FastAPI()

@app.post("/screening/")
async def screen_resume(resume: UploadFile):
    resume_text = parse_pdf(resume.file)
    resume_details = extract_resume_info(resume_text)

    return resume_details