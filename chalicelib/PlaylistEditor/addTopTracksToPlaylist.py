from chalicelib.TokenHelper import getAccessToken
from chalicelib.TokenHelper import refreshAccessToken
from chalicelib.Constants import constants
from spotipy.oauth2 import SpotifyOAuth

import spotipy


def add_top_tracks_to_playlist():
    # Setup Authentications
    user = getAccessToken.SpotifyToken()
    oauth = SpotifyOAuth(client_id=user.client_id, client_secret=user.client_secret,
                         redirect_uri=None)
    access_token = refreshAccessToken.get_new_access_token(oauth)
    sp = spotipy.Spotify(auth=access_token)

    # Get Current Playlist Tracks
    current_playlist_tracks = sp.user_playlist_tracks(constants.USERNAME, constants.PLAYLIST_ID, None, 20, 0, None)

    # Delete all tracks from current playlist
    list_of_tracks_to_delete = []
    for track_to_delete in range(len(current_playlist_tracks['items'])):
        url_of_track_to_delete = current_playlist_tracks['items'][track_to_delete]['track']['uri']
        list_of_tracks_to_delete.append(url_of_track_to_delete)

    sp.user_playlist_remove_all_occurrences_of_tracks(constants.USERNAME, constants.PLAYLIST_ID,
                                                      list_of_tracks_to_delete)

    # Get Current Top Tracks
    list_top_tracks = sp.current_user_top_tracks(20, 0, 'short_term')

    # Add Top Tracks to Playlist
    list_of_track_urls = []
    for track in range(len(list_top_tracks['items'])):
        track_url = list_top_tracks['items'][track]['uri']
        list_of_track_urls.append(track_url)

    sp.user_playlist_add_tracks(constants.USERNAME, constants.PLAYLIST_ID, list_of_track_urls)
