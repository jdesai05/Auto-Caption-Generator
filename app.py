import streamlit as st
import os
import uuid

from utils.audio_utils import extract_audio
from utils.whisper_utils import transcribe_audio
from utils.subtitle_utils import generate_srt
from utils.video_utils import burn_subtitles

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

st.title("🎬 Auto Caption Generator (Local Whisper + ffmpeg)")
st.write("Upload a video and get back a version with burned-in subtitles.")

uploaded_file = st.file_uploader("📁 Upload a video", type=["mp4", "mov", "mkv"])
if uploaded_file:
    file_id = str(uuid.uuid4())
    video_path = os.path.join(UPLOAD_DIR, f"{file_id}.mp4")
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())
    st.video(video_path)

    st.success("✅ Video uploaded successfully.")

    audio_path = os.path.join(UPLOAD_DIR, f"{file_id}.wav")
    with st.spinner("🔊 Extracting audio..."):
        extract_audio(video_path, audio_path)

    with st.spinner("🧠 Transcribing using Whisper..."):
        result = transcribe_audio(audio_path)
        st.success("✅ Transcription complete.")
        st.text_area("📝 Transcript Preview", result["text"], height=200)

    srt_path = os.path.join(OUTPUT_DIR, f"{file_id}.srt")
    with st.spinner("🧾 Generating subtitles..."):
        generate_srt(result, srt_path)
        st.success("✅ Subtitle file (.srt) created.")
        with open(srt_path, "rb") as srt_file:
            st.download_button("⬇️ Download Subtitle File (.srt)", srt_file, file_name="captions.srt")

    burned_path = os.path.join(OUTPUT_DIR, f"{file_id}_subtitled.mp4")
    with st.spinner("🔥 Burning subtitles into video..."):
        burn_result = burn_subtitles(video_path, srt_path, burned_path)

