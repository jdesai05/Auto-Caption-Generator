import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    return model.transcribe(audio_path, word_timestamps=False)

