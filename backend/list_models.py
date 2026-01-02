from google import genai

# 🔥 TEMPORARY: put your Gemini API key here directly
client = genai.Client(api_key="AIzaSyBv4-d7_WjWcp2krsns2mGcPvNsM2fPAAY")  # Replace with your real key

# List all available models for your key
models = client.models.list()

for m in models:
    print(m.name)  # Only print the name
