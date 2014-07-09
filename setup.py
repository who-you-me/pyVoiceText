from setuptools import setup

version = "0.1.0"
name = "pyVoiceText"
short_description = "VoiceText API wrapper"
long_description = """\
Python library for VoiceText Web API

Requirements
------------
* Python 2.7 (currently not support 3.x)

Setup
-----
::

    $ pip install pyVoiceText

Usage
-----
::

    >>> from pyVoiceText import VoiceText
    >>> voice_text = VoiceText("YOUR_API_KEY")
    >>> wav = voice_text.fetch("text", "show", "out.wav")
"""

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: Japanese",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Topic :: Multimedia :: Sound/Audio"
]

setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=classifiers,
    author="Hisao Soyama",
    author_email="hisao.soyama@gmail.com",
    url="https://github.com/who-you-me/pyVoiceText",
    license="MIT License",
    install_requires=["requests"],
    py_modules=["pyVoiceText"]
)
