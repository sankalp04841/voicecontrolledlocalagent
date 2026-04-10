import streamlit as st
from stt import transcribe
from llm import detect_intent, generate_code, summarize_text
from tools import create_file, write_code, chat

st.set_page_config(page_title="Voice AI Agent", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Voice-Controlled AI Agent")
st.markdown("Speak or upload audio to perform tasks like file creation, code generation, and summarization.")

input_text = st.text_area("Enter text to summarize (optional)")

audio_file = st.file_uploader("Upload audio", type=["wav", "mp3"])
audio_bytes = st.audio_input("Record your voice")

text = ""

if audio_bytes:
    with open("temp.wav", "wb") as f:
        f.write(audio_bytes.read())
    text = transcribe("temp.wav")

elif audio_file:
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())
    text = transcribe("temp.wav")

if text:
    try:
        
        st.subheader("Transcription")
        st.write(text)

    
        intent = detect_intent(text).lower().strip()
        st.subheader("Detected Intent")
        st.write(intent)

        def extract_filename(text):
            words = text.split()
            for word in words:
                if "." in word:
                    return word
            return "file.txt"

        st.subheader("⚡ Ready to Execute")

        if st.button("Confirm Action"):

            if "create_file" in intent:
                filename = extract_filename(text)
                result = create_file(filename)

            elif "write_code" in intent:
                filename = extract_filename(text)
                code = generate_code(text)
                result = write_code(filename, code)

            elif "summarize" in intent:
                content_to_summarize = input_text if input_text else text
                result = summarize_text(content_to_summarize)

            else:
                result = chat(text)

            st.subheader("⚙️ Action Result")
            st.success(result)

    
            st.session_state.history.append({
                "text": text,
                "intent": intent,
                "result": result
            })

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

st.subheader("History")

if st.session_state.history:
    for item in st.session_state.history:
        st.markdown(f"""
        **Text:** {item['text']}  
        **Intent:** {item['intent']}  
        **Result:** {item['result']}
        """)
else:
    st.write("No actions yet.")