"""simple example for usage"""
import argparse
import spotipyss


def search():
    """simple search func"""
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

    client_id = "1"
    client_secret = "2"

    ss = spotipyss.SpotipySS(
        client_id=client_id,
        client_secret=client_secret,
    )
    track = ss.search(track, artist)

    print(f"album_name : {track.album_name()}")
    print(f"uri : {track.spotify_uri()}")


if __name__ == "__main__":
    search()
