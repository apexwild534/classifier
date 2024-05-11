import os
import whisper
from langdetect import detect
from pytube import YouTube

def create_and_open_txt(text, filename):
    with open(filename, "w") as file:
        file.write(text)

def main(url):
    yt = YouTube(url)
    # for age restricted -> yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

    audio_stream = yt.streams.filter(only_audio=True).first()

    output_path = "YoutubeAudios"
    filename = "audio.mp3"
    audio_stream.download(output_path=output_path, filename=filename)

    print(f"Audio downloaded to {output_path}/{filename}")

    model = whisper.load_model("base")
    result = model.transcribe(f"{output_path}/{filename}", fp16=False)
    transcribed_text = result["text"]
    print(transcribed_text)

    language = detect(transcribed_text)
    print(f"Detected language: {language}")

    output_filename = f"output_{language}.txt"
    create_and_open_txt(transcribed_text, output_filename)
    return output_filename

# if __name__ == "__main__":
#     video_url = input("Enter the YouTube video URL: ")
#     main(video_url)
