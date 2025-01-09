from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from bark import SAMPLE_RATE, generate_audio, preload_models
from .voice import generate_prompt, get_available_voices, get_voice_by_id
import scipy.io.wavfile
import os
import uuid

"""
cpu

 # Add environment variables for small models

os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

gpu

# Add environment variables for GPU and fast models

os.environ["SUNO_OFFLOAD_CPU"] = "False"
os.environ["SUNO_USE_SMALL_MODELS"] = "False"
os.environ["SUNO_USE_GPU"] = "True"





 """
os.environ["SUNO_OFFLOAD_CPU"] = "True"
os.environ["SUNO_USE_SMALL_MODELS"] = "True"

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Mount the static files (CSS and JS)
app.mount("/static", StaticFiles(directory="./frontend"), name="static")

# Preload models at startup
preload_models()

class TextInput(BaseModel):
    text: str
    voice_id: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("./frontend/index.html", "r") as f:
        return f.read()

@app.get("/voices")
async def get_voices():
    return get_available_voices()

@app.post("/generate-audio")
async def generate_audio_endpoint(text_input: TextInput):
    try:
        filename = f"output/{str(uuid.uuid4())}.wav"
        
        # Generate prompt with voice ID
        prompt = generate_prompt(text_input.text, text_input.voice_id)
        
        # Generate audio
        audio_array = generate_audio(prompt)
        
        # Save audio file
        scipy.io.wavfile.write(filename, rate=SAMPLE_RATE, data=audio_array)
        
        return {"filename": filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/audio/{filename}")
async def get_audio(filename: str):
    file_path = f"output/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Audio file not found")
