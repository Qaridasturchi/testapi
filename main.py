import spotipy,json
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '93dfe93f21fb46aaad10947eadfde562'
client_secret = '36bb6e205ff143c6aeab7c3eb9bafd3a'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def SearchFromSpotify(track_name,limit):
    results = sp.search(q=track_name, type='track', limit=limit)
    track_urls = [item["external_urls"]["spotify"] for item in results["tracks"]["items"]]
    return track_urls
    
# Function to download the music
def DownloadMusic(track_urls):
    # Implement your logic for downloading the music using the provided track URLs
    # This could involve interacting with the Spotify API or another service

    # For demonstration purposes, let's assume a simple structure for audio_info
    audio_urls = [{'name': 'Sample Track 1', 'url': 'http://sample-url-1.com'},
                  {'name': 'Sample Track 2', 'url': 'http://sample-url-2.com'}]

    return audio_urls

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

if __name__ == "__main__":
    main()
