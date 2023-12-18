from fastapi import FastAPI, HTTPException, Query
from spotipy import *
app = FastAPI()

# Your existing functions
def SearchFromSpotify(track_name, limit):
    # ... (same as before)

def DownloadMusic(UrlList):
    # ... (same as before)

# FastAPI endpoint to search and download music
@app.get("/download-music/")
async def download_music(track_name: str = Query(..., title="Track Name", description="Name of the track to search"),
                         limit: int = Query(..., title="Limit", description="Limit the number of search results")):
    try:
        # Use the first function to search for the track on Spotify
        track_urls = SearchFromSpotify(track_name, limit)

        # Use the second function to download the music
        audio_urls = DownloadMusic(track_urls)

        return {"downloaded_audio_urls": audio_urls}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
