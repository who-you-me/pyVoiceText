Python library for VoiceText Web API

# Requirements

* Python 2.7 (currently not support 3.x)

# Setup

```
$ pip install pyVoiceText
```

# Usage

```
>>> from pyVoiceText import VoiceText
>>> voice_text = VoiceText("YOUR_API_KEY")
>>> wav = voice_text.fetch("text", "show", "out.wav")
```

