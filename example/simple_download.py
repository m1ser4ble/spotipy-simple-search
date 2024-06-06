#!/usr/bin/env python
import argparse
import spotipyss


def search():
    parser = argparse.ArgumentParser(
        prog="simple_download",
        description="simple download from spotify with track name and artist name.",
    )
    parser.add_argument(
        "--artist",
        action="store",
        type=str,
        default="",
        help="artist name of the music to download",
    )
    parser.add_argument(
        "--track",
        action="store",
        type=str,
        default="",
        help="track name of the music to download",
    )

    args = parser.parse_args()
    track = args.track
    artist = args.artist

    client_id = "b00a0d09652b4e1083850f6222ac8df3"
    client_secret = "f1a5696d83554e27a280b1e09b1429ce"

    ss = spotipyss.SpotipySS(
        client_id=client_id,
        client_secret=client_secret,
    )
    track = ss.search(track, artist)

    print(f'album_name : {track['album']['name']}')
    print(f'uri : {track['external_urls']['spotify']}')


if __name__ == "__main__":
    search()
