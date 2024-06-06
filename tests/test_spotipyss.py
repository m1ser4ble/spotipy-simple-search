"""test file for spotipyss"""
import pytest

import spotipyss

# def test_object_creation():
#    sss = spotipyss.SpotipySS(client_id='client_id', client_secret='client_secret', language='ko')
#    assert sss is not None

_KEY_TO_URI = (
    # entry format : (track, artist), uri
    (
        ("GOSSIP (feat. Tom Morello)", "Måneskin, Tom Morello"),
        "https://open.spotify.com/track/4GvPlSOKfN7aXEuGW8zKUx?si=d53d31b408484af8",
    ),
)


@pytest.mark.parametrize("key_to_uri", _KEY_TO_URI)
def test_search(id, secret, key_to_uri):
    """test the main feature"""
    # pylint: disable=redefined-builtin
    sss = spotipyss.SpotipySS(client_id=id, client_secret=secret, language="ko")
    (track, artist), uri = key_to_uri
    track = sss.search(track, artist)

    assert track.spotify_uri() == uri
