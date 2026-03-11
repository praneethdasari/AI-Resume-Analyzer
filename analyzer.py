import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyDz3YJ9ap0Y2WZ2ffWKLpFnf7YgQxi-xs0"))

# choose working model from your list
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