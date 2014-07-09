#-*- coding: utf-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth

class VoiceText(object):
    VERSION = "v1"
    URL = "https://api.voicetext.jp/%s/tts" % VERSION

    def __init__(self, key):
        self.key = key

    def fetch(self, text, speaker, out=None, emotion=None,
              emotion_level=1, pitch=100, speed=100, volume=100):
        params = {
            "text": text,
            "speaker": speaker,
            "pitch": pitch,
            "speed": speed,
            "volume": volume
        }
        if emotion:
            params["emotion"] = emotion
            params["emotion_level"] = emotion_level

        wave = self._request(params)
        if out:
            self.save(wave, out)
            return True

        return wave

    def _request(self, params):
        auth = HTTPBasicAuth(self.key, "")
        resp = requests.post(self.URL, params=params, auth=auth)

        if resp.status_code == 200:
            return resp.content
        else:
            content = json.loads(resp.content)
            message = content["error"]["message"]
            raise Exception("%s: %s" % (resp.status_code, message))

    def save(self, wave, out):
        with open(out, "wb") as f:
            f.write(wave)
