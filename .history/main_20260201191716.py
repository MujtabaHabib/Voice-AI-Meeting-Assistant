from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import openai
import tempfile
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin =['*'],
    allow_method = ['*'],
    allow_header = ['*'] 
)
