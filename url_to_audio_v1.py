import os
import yt_dlp

# Example output directory
output_directory = 'C:/Users/maxzh/Downloads'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


# Set the environment variables for ffmpeg and ffprobe
os.environ["PATH"] += os.pathsep + 'C:/Users/maxzh/AppData/Local/ffmpeg'

def download_audio_from_urls(urls):
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == '__main__':
    urls = [


"https://www.youtube.com/watch?v=1_wAxATd3Uk&t=39s",
        # Add more URLs as needed
    ]
    download_audio_from_urls(urls)
