"""test file for spotipyss"""
import pytest

import spotipyss

# def test_object_creation():
#    sss = spotipyss.SpotipySS(client_id='client_id', client_secret='client_secret', language='ko')
#    assert sss is not None

_KEY_TO_URI = (
    # entry format : (track, artist), {uri1,uri2}
    (
        ("GOSSIP (feat. Tom Morello)", "Måneskin, Tom Morello"),
        {
            "https://open.spotify.com/track/4GvPlSOKfN7aXEuGW8zKUx",
            "https://open.spotify.com/track/44Xyja7xYPlVC6v2CeweSi",
        },
    ),
    (
        ("marigold", "aimyon"),
        {
            "https://open.spotify.com/track/5NqGfELjcdvRIUuhgZJ34W",
        },
    ),
    (
        ("파이팅 해야지 (Feat. 이영지)", "부석순 (SEVENTEEN)"),
        {
            "https://open.spotify.com/track/7eBpUuPnDTfbeP1P4P93CS",
        },
    ),
    (
        ("나는 아픈 건 딱 질색이니까", "(여자)아이들"),
        {"https://open.spotify.com/track/5kt0nWRnFWEeBUyLWSYnkd"},
    ),
    (("취중고백", "김민석"), {"https://open.spotify.com/track/0hqngwyh8WnPuYlLYHRQqp"}),
    # (("그대가 내 안에 박혔다(그내박)", "순순희(기태)"), {}),
    (
        ("손오공", "세븐틴 (SEVENTEEN)"),
        {"https://open.spotify.com/track/3AOf6YEpxQ894FmrwI9k96"},
    ),
    (
        ("첫 만남은 계획대로 되지 않아", "TWS (투어스)"),
        {"https://open.spotify.com/track/0aZG8KWrpRnsGL0loUkfSj"},
    ),
)


@pytest.mark.parametrize("key_to_uri", _KEY_TO_URI)
def test_search(id, secret, key_to_uri):
    """test the main feature"""
    # pylint: disable=redefined-builtin
    sss = spotipyss.SpotipySS(client_id=id, client_secret=secret, language="ko")
    (track, artist), uri = key_to_uri
    track = sss.search(track=track, artist=artist)

    assert track.spotify_uri() in uri
