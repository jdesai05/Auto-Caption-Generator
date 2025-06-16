import ffmpeg
import os

def extract_audio(video_path, output_audio_path):
    try:
        (ffmpeg
         .input(video_path)
         .output(output_audio_path, ac=1,ar='10000')
         .overwrite_output()
         .run(quiet=True)
        )
        return output_audio_path
    except Exception as e:
        return str(e)
    
    
