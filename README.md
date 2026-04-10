# voicecontrolledlocalagent
# 🎤 Voice-Controlled Local AI Agent

## 🚀 Project Overview

This project is a **Voice-Controlled AI Agent** that processes audio input, understands user intent using a Large Language Model (LLM), and performs actions like file creation, code generation, and text summarization — all locally.

The system demonstrates a full AI pipeline:

**Audio → Speech-to-Text → Intent Detection → Tool Execution → UI Output**

---

## ✨ Features

### 🎤 Audio Input
- Record voice directly (microphone)
- Upload audio files (.wav, .mp3)

### 🧾 Speech-to-Text
- Converts audio into text using Whisper

### 🧠 Intent Detection
- Classifies user intent into:
  - `create_file`
  - `write_code`
  - `summarize`
  - `chat`

### ⚙️ Tool Execution
- Creates files locally
- Generates and writes code into files
- Summarizes text using LLM
- Handles general chat queries

### 🛡️ Safety
- All files are created inside a restricted `output/` directory

### 🖥️ User Interface
- Built with Streamlit
- Displays:
  - Transcription
  - Detected intent
  - Action result
  - History of actions

### ⭐ Bonus Features
- Confirmation button before execution (Human-in-the-loop)
- Dynamic filename extraction from user input
- Session-based history tracking

---

## 🧰 Tech Stack

- **Frontend/UI:** Streamlit  
- **Speech-to-Text:** Whisper  
- **LLM (Intent + Code + Summary):** Ollama (Llama 3)  
- **Backend:** Python  

---

## 📂 Project Structure
voice-ai-agent/
│
├── app.py # Main Streamlit UI
├── stt.py # Speech-to-text logic
├── llm.py # Intent detection + LLM functions
├── tools.py # File, code, and text tools
├── requirements.txt
├── README.md
├── output/ # All generated files (SAFE ZONE)
└── venv/ # Virtual environment (optional)


---

## 🏗️ Architecture

The system follows a modular pipeline:

1. **Audio Input Layer**
   - Accepts input via microphone or uploaded audio file

2. **Speech-to-Text (STT)**
   - Audio is converted into text using Whisper

3. **Intent Detection (LLM)**
   - The transcribed text is passed to a local LLM (Llama 3 via Ollama)
   - The model classifies the intent

4. **Execution Layer (Tools)**
   - Based on the detected intent:
     - File creation
     - Code generation
     - Summarization
     - Chat response

5. **User Interface (UI)**
   - Displays transcription, intent, action, and history

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sankalp04841/voicecontrolledlocalagent.git
cd voice-ai-agent
```
2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
3. Install Dependencies

```bash
pip install streamlit openai-whisper torch ollama
```
4. Install and Run Ollama

Download:
https://ollama.com

Run the model:
```bash
ollama run llama3
```
5. Install FFmpeg (Required for Whisper)

Download:
https://www.gyan.dev/ffmpeg/builds/

Steps:
i)Extract the zip file
ii)Locate the bin folder
iii)Add it to system PATH

Verify installation:
```
ffmpeg -version
```
6. Run the Application
```
streamlit run app.py
```
##  Hardware & Workarounds 
  ## Runs on CPU (no GPU required)
  ## Whisper uses FP32 mode (slower but stable)

## Workarounds:
  ## Used lightweight Whisper models (base / tiny)
  ## Used Ollama for efficient local LLM execution
  ## Restricted file operations to output/ folder for safety
##  Limitations
   ## Slower performance on CPU-only systems
   ## Accuracy depends on audio clarity
   ## LLM intent detection may require normalization

## Future Improvements
   ## Support compound commands (e.g., "summarize and save")
   ## Improve intent classification accuracy
   ## Add persistent memory across sessions
   ## Enhance UI design
