# 🎬 Auto Caption Generator

This is a simple yet powerful **auto-captioning tool** built using OpenAI's Whisper model and `ffmpeg`. It allows users to upload a video file and receive a version of the video with **burned-in subtitles**.

> This project runs entirely **locally**, using **Streamlit** for the frontend.

---

## 🚀 Features

- Upload `.mp4`, `.mov`, or `.mkv` video files
- Extract audio from video
- Generate accurate captions using Whisper
- Output subtitles in `.srt` format
- Burn subtitles into the original video using `ffmpeg`
- Streamlit-based user interface
- Download both `.srt` and final subtitled video

---

## 🛠️ Tech Stack

| Tool/Library     | Purpose                                |
|------------------|----------------------------------------|
| `Streamlit`      | Frontend UI                            |
| `openai-whisper` | Speech-to-text transcription           |
| `ffmpeg-python`  | Audio extraction & video rendering     |
| `pysrt`          | Subtitle (.srt) file creation          |
| `uuid`           | Unique file names for session handling |

---

## 📁 Folder Structure
auto_caption_generator/
│
├── app.py # Streamlit app
├── requirements.txt # Python dependencies
├── README.md # This file
│
├── utils/
│ ├── audio_utils.py # Audio extraction
│ ├── whisper_utils.py # Whisper transcription
│ ├── subtitle_utils.py # SRT generation
│ └── video_utils.py # Burn subtitles
│
├── uploads/ # Uploaded input videos/audio
└── output/ # Generated .srt and output video

yaml
Copy
Edit

---

## 💻 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/auto-caption-generator.git
cd auto-caption-generator
(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Install FFmpeg (Required)

Windows: https://ffmpeg.org/download.html

Mac: brew install ffmpeg

Linux: sudo apt install ffmpeg

Make sure it's added to your system PATH.

▶️ Running the App
bash
Copy
Edit
streamlit run app.py
Then open the local server link in your browser (usually http://localhost:8501).

📦 Output
output/*.srt: The subtitle file

output/*_subtitled.mp4: The final video with hardcoded subtitles

Both files are downloadable from the Streamlit app

🧠 Whisper Model Options
In whisper_utils.py, you can switch to a different model like:

python
Copy
Edit
whisper.load_model("tiny")
whisper.load_model("base")     # (default)
whisper.load_model("small")
whisper.load_model("medium")
whisper.load_model("large")    # Most accurate, slowest
🙌 Acknowledgements
OpenAI Whisper

FFmpeg

Streamlit
