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

@app.post("/voice-agent")
async def voice_agent(file: UploadFile=File(...)):
        
        with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as tmp:
            tmp.write(await file.read())
            tmp_path =tmp.name
            
        audio_file = open(tmp_path,"rb")
        transcript = client.audio.transcriptions.create(
            model='whisper-1',
            file=audio_file
        )
        text = transcript.text
        
        prompt = f"""
        summarize the following text and extract action items.
        
        Text:
        {text}
        """
        
        response = client.completions.chat.create(
            "model
        )