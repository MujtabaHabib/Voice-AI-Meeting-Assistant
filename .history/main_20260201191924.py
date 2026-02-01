from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import openai
import tempfile
import 
from dotenv import load_dotenv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins =['*'],
    allow_methods = ['*'],
    allow_headers = ['*'] 
)

client = OpenAI(api_key=)