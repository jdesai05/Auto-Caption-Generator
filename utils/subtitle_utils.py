import pysrt

def seconds_to_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return pysrt.SubRipTime(hours, minutes, secs, millis)

def generate_srt(transcription_result, output_path):
    subs = pysrt.SubRipFile()
    for i, segment in enumerate(transcription_result['segments']):
        start = seconds_to_srt_time(segment['start'])
        end = seconds_to_srt_time(segment['end'])
        text = segment['text'].strip()
        subs.append(pysrt.SubRipItem(index=i+1, start=start, end=end, text=text))
    subs.save(output_path, encoding='utf-8')
    return output_path
