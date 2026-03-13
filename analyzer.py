import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text):

    prompt = f"""
    Analyze the following resume and provide:

    1. Job Match Score (0-100)
    2. Missing Skills
    3. Resume Improvement Tips

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text