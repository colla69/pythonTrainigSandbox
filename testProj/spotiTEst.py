# %%

import os
import spotipy
import spotipy.util as s_util
from json.decoder import JSONDecodeError


class SpotiGetter:

    def __init__(self):
        self.token = ""
        self.spotifyObject = None
        self.username = "pc"
        self.scope = 'user-read-private'
        self.client_id = 'f741539a97c84174b552e8af9040f76a'
        self.client_secret = '9d1d29db4aa9433e816518956352b117'
        self.redirect_uri = 'https://google.com'
        self.login()

    def login(self):
        try:
            token = s_util.prompt_for_user_token(self.username, self.scope, self.client_id, self.client_secret,
                                                 self.redirect_uri)
        except (AttributeError, JSONDecodeError):
            token = s_util.prompt_for_user_token(self.username, self.scope, self.client_id, self.client_secret,
                                                 self.redirect_uri)

        results = self.spotifyObject.search(q='artist:' + "coez", type='artist')
        print(results)


try:
    sg = SpotiGetter()
except Exception as e:
    print(e)