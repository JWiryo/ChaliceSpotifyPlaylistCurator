from chalicelib.Constants import constants

class SpotifyToken(object):

    def __init__(self):
        self.username = constants.USERNAME
        self.client_id = constants.CLIENT_ID
        self.client_secret = constants.CLIENT_SECRET
        self.redirect_url = constants.REDIRECT_URL
        self.scope = constants.SCOPE
        self.playlist_id = constants.PLAYLIST_ID

##### Below executions only done once to get initial access token and refresh token
# user = SpotifyToken()
# token = util.prompt_for_user_token(username=user.username, scope=user.scope,
#                                    client_id=user.client_id, client_secret=user.client_secret,
#                                    redirect_uri=user.redirect_url)
