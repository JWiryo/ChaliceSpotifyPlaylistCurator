from chalice import Chalice
from chalicelib.PlaylistEditor import addTopTracksToPlaylist

app = Chalice(app_name='spotifyAutoPlaylist')
app.debug = True

# Trigger Lambda function every Monday at 00:00 AM (GMT +8)
@app.schedule('cron(0 16 ? * SUN *)')
def generate_top20_tracks_to_playlist(event):
    addTopTracksToPlaylist.add_top_tracks_to_playlist()
    return {'message': 'OK'}
