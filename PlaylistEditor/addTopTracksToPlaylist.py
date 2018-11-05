from TokenHelper.getAccessToken import SpotifyToken
from TokenHelper.refreshAccessToken import get_new_access_token
from spotipy.oauth2 import SpotifyOAuth

import spotipy
import Constants.constants as constants


def add_top_tracks_to_playlist():
    # Setup Authentications
    user = SpotifyToken()
    oauth = SpotifyOAuth(client_id=user.client_id, client_secret=user.client_secret,
                         redirect_uri=None)
    access_token = get_new_access_token(oauth)
    sp = spotipy.Spotify(auth=access_token)

    # Get Current Top Tracks
    list_top_tracks = sp.current_user_top_tracks(20, 0, 'short_term')
    track_urls_list = []
    for track in range(len(list_top_tracks['items'])):
        track_url = list_top_tracks['items'][track]['uri']
        track_urls_list.append(track_url)

    # Add Top Tracks to Playlist
    sp.user_playlist_add_tracks(constants.USERNAME, constants.PLAYLIST_ID, track_urls_list)
