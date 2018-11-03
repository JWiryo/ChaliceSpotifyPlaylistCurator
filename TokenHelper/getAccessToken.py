import spotipy.util as util
from Constants import constants

class SpotifyToken(object):

    def __init__(self):
        self.username = constants.USERNAME
        self.client_id = constants.CLIENT_ID
        self.client_secret = constants.CLIENT_SECRET
        self.redirect_url = constants.REDIRECT_URL
        self.scope = constants.PLAYLIST_MODIFY_PUBLIC_SCOPE
        self.playlist_id = constants.PLAYLIST_ID


user = SpotifyToken()
token = util.prompt_for_user_token(username=user.username, scope=user.scope,
                                   client_id=user.client_id, client_secret=user.client_secret,
                                   redirect_uri=user.redirect_url)
