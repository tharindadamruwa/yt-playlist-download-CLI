import yt_dlp
from tqdm import tqdm

# Function to download a single video from a playlist
def download_video(url):
    ydl_opts = {
        'format': 'bestaudio[height<=360]+bestaudio/best[height<=360]',  # 360p quality
        'outtmpl': 'Download/Chem/%(title)s.%(ext)s',  # Save with video title in 'Download/Chem'
        'noplaylist': True,  # Download videos one by one, not as a playlist
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Save in MP4 format
        }],
        'progress_hooks': [progress_hook],  # Hook for progress bar
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Progress hook function to show the progress bar
def progress_hook(d):
    if d['status'] == 'downloading':
        pbar.update(d['downloaded_bytes'] - pbar.n)
    elif d['status'] == 'finished':
        pbar.set_description("Download complete")

# Input playlist URL from user
playlist_url = input("Enter the YouTube playlist URL: ")

# Initialize progress bar
pbar = tqdm(unit='B', unit_scale=True, desc="Downloading", total=100)

# Download the playlist one by one
with yt_dlp.YoutubeDL({'extract_flat': True}) as ydl:
    result = ydl.extract_info(playlist_url, download=False)
    if 'entries' in result:
        for entry in result['entries']:
            video_url = entry['url']
            print(f"Downloading: {entry['title']}")
            download_video(video_url)

# Close progress bar
pbar.close()