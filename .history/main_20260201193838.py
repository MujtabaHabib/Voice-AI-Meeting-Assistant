from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins =['*'],
    allow_methods = ['*'],
    allow_headers = ['*'] 
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/voice-agent"):
    async def voice_agent(file=UploadFile(file(...)))