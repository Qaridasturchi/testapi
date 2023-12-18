from spotipy import *


def main():
    track_name = input("Enter the track name: ")
    limit = int(input("Enter the limit: "))

    # Use the first function to search for the track on Spotify
    track_urls = SearchFromSpotify(track_name, limit)

    # Use the second function to download the music
    audio_urls = DownloadMusic(track_urls)

    print("Downloaded audio URLs:")
    for audio_info in audio_urls:
        print(f"Name: {audio_info['name']}, URL: {audio_info['url']}")

if name == "main":
    main()
