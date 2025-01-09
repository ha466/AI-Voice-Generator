# Text-to-Speech API

This project provides a FastAPI-based web service for generating audio files from text using different voices.

## Features

- Generate audio from text using various voices
- Retrieve available voices
- Serve generated audio files

## Requirements

- Python 3.7+
- pip install git+https://github.com/suno-ai/bark.git

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI server:

    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to access the API.

## API Endpoints

- `GET /` - Serve the frontend HTML page
- `GET /voices` - Retrieve a list of available voices
- `POST /generate-audio` - Generate an audio file from text
- `GET /audio/{filename}` - Retrieve a generated audio file

## Environment Variables

To configure the environment variables for using GPU and fast models, modify the `main.py` file:

```python
import os

# Add environment variables for GPU and fast models
os.environ["SUNO_OFFLOAD_CPU"] = "False"
os.environ["SUNO_USE_SMALL_MODELS"] = "False"
os.environ["SUNO_USE_GPU"] = "True"



