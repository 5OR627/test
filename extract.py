import os

from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_path):
    video=VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

extract_audio('downloaded_video.mp4', 'extracted_audio.mp3')