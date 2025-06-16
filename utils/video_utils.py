import ffmpeg
import os

def burn_subtitles(video_path, srt_path, output_path):
    try:
        (
            ffmpeg
            .input(video_path)
            .output(output_path, vf=f"subtitles={srt_path}", vcodec='libx264', acodec='copy')
            .overwrite_output()
            .run(quiet=True)
        )
        return output_path
    except ffmpeg.Error as e:
        return str(e)
