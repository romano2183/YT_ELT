import requests
import json

API_KEY = "AIzaSyBcvLhKGuEydkzNS3HihrKlYaV2kg20a5M"
CHANNEL_HANDLE = "MrBeast"
maxResults = 50

def get_playlist_id():

    try:

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # print(response)

        data = response.json()
        #print(json.dumps(data, indent=4))

        channel_items = data["items"][0] 
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        print(channel_playlistId)

        return channel_playlistId

    except requests.exceptions.RequestException as e:
        raise e

def get_video_ids():
    try:
        based_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId=UUX6OQ3DkcsbYNE6H8uQQuVA&key=AIzaSyBcvLhKGuEydkzNS3HihrKlYaV2kg20a5M"

        response = requests.get(based_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        return response.json()
    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    print("get playlist_id will be executed")
    get_playlist_id() 
else:
    print("get playlist_id will not be executed")