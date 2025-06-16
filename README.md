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
