import openai

client = openai.OpenAI(api_key = '')

def transcribe_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="srt",
            language="zh"
        )
        return transcript

subtitles = transcribe_audio("extracted_audio.mp3")

with open("subtitles.srt", "w", encoding="utf-8") as subtitles_file:
    subtitles_file.write(subtitles)