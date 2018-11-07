from chalice import Chalice
from chalicelib.PlaylistEditor import addTopTracksToPlaylist

app = Chalice(app_name='spotifyAutoPlaylist')
app.debug = True

@app.route('/')
def generate_top20_tracks_to_playlist():
    addTopTracksToPlaylist.add_top_tracks_to_playlist()
    return {'message': 'OK'}
