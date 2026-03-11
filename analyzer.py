import google.generativeai as genai

# configure API key
genai.configure(api_key="AIzaSyB9C1SvYz80IZbp4LsghLifgtR1iVN7ewc")

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