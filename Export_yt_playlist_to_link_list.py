from pytube import Playlist

# Function to export video links to a text file
def export_youtube_playlist_links(playlist_url, file_name):
    # Initialize the Playlist object
    playlist = Playlist(playlist_url)

    # Open the file to write the links
    with open(file_name, 'w') as file:
        # Loop through each video in the playlist
        for video in playlist.videos:
            # Write the video URL to the text file
            file.write(video.watch_url + '\n')

    print(f"Video links from the playlist have been exported to {file_name}")

# Example usage
playlist_url = input("Enter the YouTube playlist URL: ")
file_name = input("Enter the name of the text file to save links: ")

export_youtube_playlist_links(playlist_url, file_name)