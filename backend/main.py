from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

# 🔥 TEMPORARY: put your Gemini API key here directly
GEMINI_API_KEY = "AIzaSyBv4-d7_WjWcp2krsns2mGcPvNsM2fPAAY"

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Initialize FastAPI
app = FastAPI()

# Enable CORS for all origins (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class ChatRequest(BaseModel):
    message: str

# /chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    try:
        # Call Gemini API
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",  # ✅ Correct model
            contents=req.message
        )
        # Return the AI reply
        return {"reply": response.text}
    except Exception as e:
        return {"error": str(e)}
