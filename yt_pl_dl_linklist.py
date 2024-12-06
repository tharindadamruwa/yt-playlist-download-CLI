import yt_dlp
import sys
import traceback

# Custom terminal-style progress bar with green (for completed) and yellow (for remaining) colors
def custom_progress_bar(downloaded_bytes, total_bytes):
    bar_length = 40  # Length of the progress bar
    GREEN = '\033[1;92m'  # ANSI code for green text (bold)
    YELLOW = '\033[1;93m'  # ANSI code for yellow text (bold)
    RESET = '\033[0m'   # ANSI code to reset color

    # Calculate the percentage of progress
    percent = float(downloaded_bytes) / total_bytes
    completed = int(percent * bar_length)  # Number of '#' symbols to represent progress
    remaining = bar_length - completed    # Remaining part of the bar

    # Build the progress bar with green and yellow parts
    bar = f"{GREEN}{'#' * completed}{RESET}{YELLOW}{'*' * remaining}{RESET}"

    # Print the progress bar with percentage
    sys.stdout.write(f"\r|{bar}| {percent * 100:.1f}%")
    sys.stdout.flush()

# Progress hook function to show the real-time progress
def progress_hook(d):
    if d['status'] == 'downloading':
        # Call the custom progress bar with current downloaded bytes and total bytes
        custom_progress_bar(d['downloaded_bytes'], d['total_bytes'])
    elif d['status'] == 'finished':
        sys.stdout.write("\nDownload complete!\n")

# Function to download a single video
def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestaudio[height<=360]+bestaudio/best[height<=360]',  # 360p quality
            'outtmpl': 'Download/Chem/%(title)s.%(ext)s',  # Save with video title in 'Download/Chem'
            'noplaylist': True,  # Download videos one by one
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Save in MP4 format
            }],
            'progress_hooks': [progress_hook],  # Hook for progress bar
            'quiet': True,  # Prevent extra output
            'noprogress': True,  # Suppress yt-dlp's default progress output
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        sys.stdout.write(f"\nError downloading {url}: {e}\n")
        # Print traceback for debugging
        traceback.print_exc()

# Function to read URLs from a file and return a list of URLs
def read_video_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines()]
        return urls
    except FileNotFoundError:
        sys.stdout.write(f"Error: The file {file_path} was not found.\n")
        return []
    except Exception as e:
        sys.stdout.write(f"Error reading file {file_path}: {e}\n")
        traceback.print_exc()
        return []

# Input the path of the file containing the video URLs
file_path = input("Enter the path of the file containing YouTube video URLs: ")

# Read the video URLs from the file
video_urls = read_video_urls_from_file(file_path)

# Check if there were any issues reading the file
if not video_urls:
    sys.exit("No video URLs to download. Exiting...")

# Download each video one by one
for video_url in video_urls:
    print(f"Downloading: {video_url}")
    download_video(video_url)