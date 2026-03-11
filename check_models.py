import google.generativeai as genai

genai.configure(api_key="AIzaSyB9C1SvYz80IZbp4LsghLifgtR1iVN7ewc")

for model in genai.list_models():
    print(model.name)