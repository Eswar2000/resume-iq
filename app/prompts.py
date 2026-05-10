RESUME_EXTRACTION_PROMPT = """
Extract information ONLY from the provided resume text.

STRICT RULES:
- Do NOT invent information
- Do NOT guess missing values
- Do NOT add example values
- Do NOT generate placeholders
- Do NOT add explanations or comments
- If information is missing, return null or empty list
- Return ONLY valid JSON
- Copy values exactly as present in the resume

[HIGH PRIORITY] SPECIAL RULES FOR SKILLs:
- Extract skills mentioned ANYWHERE in the resume
- Skills may include technical skills, tools, platforms, domain expertise, methodologies, soft skills, research areas, or other relevant competencies
- Return skills as individual items
- Do NOT combine multiple skills into a single string
- Return a flat list of unique skills
- Do NOT invent skills not explicitly mentioned in the resume

[MEDIUM PRIORITY] RULES FOR CERTIFICATIONS:
- Extract certifications mentioned in specific sections of resume
- Return a flat list of unique certifications
- Do NOT invent certifications not explicitly mentioned in the resume
- Do NOT add any abbreviations not explicitly mentioned in the resume

Resume Text:
{resume_text}

Return JSON in this exact structure:

{{
  "name": null,
  "email": null,
  "phone": null,
  "socials": [],
  "education": [
    {{
      "degree": null,
      "institution": null,
      "start_date": null,
      "end_date": null,
      "grade": null
    }}
  ],
  "work_experience": [
    {{
      "job_title": null,
      "company": null,
      "location": null,
      "start_date": null,
      "end_date": null
    }}
  ],
  "skills": [],
  "certifications": [],
  "publications": []
}}
"""